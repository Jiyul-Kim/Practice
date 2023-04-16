import re
import requests
from bs4 import BeautifulSoup
import sys
import datetime

# MySecretary_weather_HeadlineNews_ITNews_TodayEnglish.py

nowDate = datetime.datetime.now()

sys.stdout = open(nowDate.strftime('%Y-%m-%d_%H%M_Daily') + '.txt','w', encoding="utf8")



def create_soup(url):
    res= requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%84%9C%EC%9A%B8%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    print("** 네이버 날씨 **")
    # [오늘의 날씨]
    # 어제보다 7.2° 낮아요  비 
    # 현재 온도14.2°  (최저기온13°/최고기온16°)
    # 강수확률  오전 80%  /  오후 80%
    weather = soup.find("p", attrs={"class":"summary"}).get_text()
    now_degree = soup.find("div", attrs={"class":"temperature_text"}).get_text()
    lo_degree = soup.find("span", attrs={"class":"lowest"}).get_text()
    hi_degree = soup.find("span", attrs={"class":"highest"}).get_text()
    am_rainfall = soup.select("span.weather_left")[0].text
    pm_rainfall = soup.select("span.weather_left")[1].text
    chart = soup.select("ul.today_chart_list")[0].text
    chart=chart.lstrip()
    chart=chart.rstrip()
    chart = chart.replace("    ", " /")

    print("[오늘의 날씨]")
    print(weather)
    print(now_degree.lstrip(), "({}/{})".format(lo_degree,hi_degree))
    print("강수확률",am_rainfall,"/",pm_rainfall)
    print('\n')
    print(chart)

def scrape_headline_news():
    print("** 구글 뉴스 **")
    print("[헤드라인 뉴스]")
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"
    soup = create_soup(url)
    headlines = soup.find_all("div", attrs={"class":"XlKvRb"},limit=5)
    for idx,headline in enumerate(headlines):
        title = headline.find("a", attrs={"class":"WwrzSb"})["aria-label"]
        link = headline.find("a", attrs={"class":"WwrzSb"})["href"]
        link = link.replace(".",'')
        link = "https://news.google.com"+link
        print("{}. {}".format(idx+1, title))
        print("링크: ",link)
        print('')

def scrape_IT_news():
    print("** 구글 IT 뉴스 **")
    print("[IT 뉴스]")
    url = "https://news.google.com/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnJieG9DUzFJb0FBUAE?hl=ko&gl=KR&ceid=KR%3Ako"
    soup = create_soup(url)

    headlines = soup.find_all("div", attrs={"class":"XlKvRb"},limit=3)
    for idx,headline in enumerate(headlines):
        title = headline.find("a", attrs={"class":"WwrzSb"})["aria-label"]
        link = headline.find("a", attrs={"class":"WwrzSb"})["href"]
        link = link.replace(".",'')
        link = "https://news.google.com"+link
        print("{}. {}".format(idx+1, title))
        print("링크: ",link)
        print('') 

def scrape_daily_english_sentence():
    print("** 해커스 오늘의 영어 회화 **")
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, idx 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
        
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, idx 기준 0~3까지 잘라서 가져옴

        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news()
    scrape_IT_news()
    scrape_daily_english_sentence()

sys.stdout.close()