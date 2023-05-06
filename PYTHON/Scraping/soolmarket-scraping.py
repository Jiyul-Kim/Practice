import requests
from bs4 import BeautifulSoup
import urllib.request

res = requests.get("https://www.soolmarket.com/goods/goods_list.php?cateCd=014006")
soup = BeautifulSoup(res.content, "html.parser")


items = soup.find_all("div", {"class":"item_cont"})
for item in items:
    item_img = item.find("img")["src"]
    item_name = item.find("strong", {"class":"item_name"}).get_text()
    urllib.request.urlretrieve(item_img,f"D:\Practice\PYTHON\Scraping\soolmarket-scraping-img\{item_name}.jpg")
    # print(items.get_text())