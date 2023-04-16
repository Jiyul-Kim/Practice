from bs4 import BeautifulSoup
import requests
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='wjddms4120**', db='bestproducts2', charset='utf8')
cursor = db.cursor()

url = 'https://corners.gmarket.co.kr/Bestsellers'
res = requests.get(url, timeout=10)
soup = BeautifulSoup(res.content, 'html.parser')


def save_data(item_info):
    sql = """
        SELECT COUNT(*) FROM items WHERE item_code = '{}';
    """.format(item_info['item_code'])
    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0] == 0:
        sql = """
            INSERT INTO items VALUES
            ('{}',
            '{}',
            {},
            {},
            {},
            '{}' 
            ) """.format(item_info['item_code'], item_info['title'], item_info['org_price'], item_info['dis_price'], item_info['dis_percent'], item_info['provider'])
        sql = sql.replace('\n', '')
        print(sql)
        cursor.execute(sql)        
    
    sql = """
        INSERT INTO ranking(main_category, sub_category, item_ranking, item_code) VALUES
        ('{}',
        '{}',
        '{}',
        '{}' 
        ) """.format(item_info['category_name'], item_info['sub_category_name'], str(item_info['ranking']), item_info['item_code'])
    sql = sql.replace('\n', '')
    cursor.execute(sql)
    print(sql)

# main / sub category info
def get_category(category_link, category_name):
    # print(category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')

    get_items(soup, category_name, 'ALL')    

    sub_categories = soup.select('div.navi.group ul li > a')
    for sub_category in sub_categories:
        res = requests.get('https://corners.gmarket.co.kr'+ sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        get_items(soup, category_name, sub_category.get_text())

# main / sub category info + 상품 정보 스크랩핑
def get_items(html, category_name, sub_category_name):
    data_dict = dict()
    items_result_list = list()
    best_item = html.select('div.best-list ul li')
    for index, item in enumerate(best_item):
        ranking = index + 1
        title = item.select_one('a.itemname')
        org_price = item.select_one('div.o-price span:nth-child(2)')
        dis_price = item.select_one('div.s-price strong span')
        dis_percent = item.select_one('div.s-price em')

        # 태그가 없거나, 태그는 있는데 데이터가 없을 경우
        if org_price is None or org_price.get_text() == '':
            org_price = dis_price
        if org_price is not None:
            org_price = org_price.get_text().replace(',', '').replace('원', '')
        if dis_price is None or dis_price.get_text() == '':
            org_price, dis_price = 0, 0
        else:
            dis_price = dis_price.get_text().replace(',', '').replace('원', '')
        if dis_percent is None or dis_percent.get_text() == '':
            dis_percent = 0
        else:
            dis_percent = dis_percent.get_text().replace('%', '')

        product_link = item.select_one('div.thumb > a')
        item_code = product_link.attrs['href'].split('=')[1].replace('&ver','')

        res = requests.get(product_link.attrs['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        provider = soup.select_one("div.item-topinfo_headline > p > span.text__seller > a")
        if provider == None:
            provider = ''
        else:
            provider = provider.get_text()

        data_dict['category_name'] = category_name
        data_dict['sub_category_name'] = sub_category_name
        data_dict['ranking'] = ranking
        data_dict['item_code'] = item_code
        data_dict['provider'] = provider
        data_dict['title'] = title.get_text()
        data_dict['org_price'] = org_price
        data_dict['dis_price'] = dis_price
        data_dict['dis_percent'] = dis_percent
        
        save_data (data_dict)
        # print(data_dict)


# main category info
main_categoryies = soup.select('ul.by-group li > a')
for main_category in main_categoryies:
    get_category('https://corners.gmarket.co.kr'+main_category['href'], main_category.get_text())
