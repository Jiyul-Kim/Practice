from bs4 import BeautifulSoup
import requests

url = 'https://corners.gmarket.co.kr/Bestsellers'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# main category info
main_categoryies = soup.select('ul.by-group li > a')
for main_category in main_categoryies:
    print('https://corners.gmarket.co.kr'+main_category['href'], main_category.get_text())

