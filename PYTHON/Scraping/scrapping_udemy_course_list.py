import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.udemy.com/course/the-web-developer-bootcamp-2021-korea/")
soup = BeautifulSoup(res.content, 'html.parser')
# print(res.content)

titles = soup.select("#udemy > div.ud-main-content-wrapper > div.ud-main-content > div > div > div.paid-course-landing-page__container > div.paid-course-landing-page__body > div > div:nth-child(4) > div > div:nth-child(3) > div:nth-child(1) > div.accordion-panel-module--content-wrapper--DIUt_ > div > ul > li:nth-child(1) > div > div > div > div > button > span")
for title in titles:
    print(title.get_text())

# # print(titles)
