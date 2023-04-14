import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font

# Gmarket_item_crawling.py

wb = Workbook()
ws = wb.active
ws.column_dimensions['B'].width = 100
ws.column_dimensions['C'].width = 30
ws.column_dimensions['D'].width = 100
ws.append(['랭킹', '제목', '가격', '링크'])



url2 = 'https://corners.gmarket.co.kr/Bestsellers'
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.content, 'html.parser')



for index in range(0, 13):
    if index == 0:
        url = "https://corners.gmarket.co.kr/Bestsellers"    
    elif index <= 9:
        index = '0' + str(index)
        url = "https://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G" + str(index)

sheet_names = soup2.find_all('ul', {'class':'by-group'})
for index, sheet_name in enumerate(sheet_names):
    sheet_name = sheet_name.get_text().replace('/', '')
    # print(sheet_name)
    b = sheet_name.split()
    # print(b)
    for i in b:
        page = "지금은 {} 페이지 입니다.".format(i)
        ws.append([page])

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

            
        bestlists = soup.select_one('div.best-list')
        prodects = bestlists.select('ul > li')

        for index2, prodect in enumerate(prodects):
            title = prodect.select_one('a.itemname').get_text()
            price = prodect.select_one('div.item_price').get_text()
            link = prodect.select_one('a')['href']
            

            ws.append([str(index2 + 1) + '.', title, price , link])
            # excel_sheet.cell(row = index + 2, column = 5).hyperlink = link
            
            print(str(index2 + 1) + '.'
                , title
                , price
                , link)
            
    wb.save('Gmarket_item_crawling.xlsx')
    wb.close()