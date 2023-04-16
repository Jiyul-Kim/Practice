from bs4 import BeautifulSoup
import requests

url = 'https://corners.gmarket.co.kr/Bestsellers'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# main / sub category info
def get_category(category_link, category_name):
    print(category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')

    sub_categories = soup.select('div.navi.group ul li a')
    for sub_category in sub_categories:
        print(category_link, category_name, sub_category.get_text(),'https://corners.gmarket.co.kr'+ sub_category['href'])

# main category info
main_categoryies = soup.select('ul.by-group li > a')
for main_category in main_categoryies:
    get_category('https://corners.gmarket.co.kr'+main_category['href'], main_category.get_text())

# main / sub category info + 상품 정보 스크랩핑
def get_items(html, category_name, sub_category_name):
    items_result_list = list()
    best_item = html.select('div.best-list ul li')
    for item in best_item:
        titles = item.selet_one('a.itemname').get_text()
        org_price = item.select_one('div.o-price').get_text()
        dis_price = item.select_one('div.s-price strong span').get_text()
        dis_percent = item.select_one('div.s-price em').get_text()