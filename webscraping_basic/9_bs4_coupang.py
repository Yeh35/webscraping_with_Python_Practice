import requests
import re
from bs4 import BeautifulSoup

page = 1
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=" + str(page) + "&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
res = requests.get(url=url, headers=headers)
res.raise_for_status()
print("request finish")

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

for item in items:

    # 쿠팡 추천은 제외
    badges = item.find("div", attrs = {"class": "badges"})
    if badges.img:
        print("광고 상품 제외")
        continue

    name = item.find("div", attrs={"class" : "name"}).get_text() # 제품명

    # apple 제품 제외
    if "Apple" in name:
        print("<Apple> 제품 제외")

    price = item.find("strong", attrs={"class": "price-value"}).getText(), # 가격
    rating = item.find("em", attrs={"class": "rating"}) # 평점
    if rating:
        rating = rating.getText()
    else :
        rating = "평점 없음"
        print("평점 없는 상품 제외")
        continue

    rating_cnt = item.find("span", attrs={"class": "rating-total-count"}) # 평점 수
    if rating_cnt:
        rating_cnt = rating_cnt.getText()[1:-1]
    else :
        rating_cnt = ""
        print("평점 없는 상품 제외")
        continue
    
    # 리뷰 100개 이상, 평점 4.5이상
    if float(rating) < 4.5 or int(rating_cnt) < 100 :
        continue
    
    print(name, print, rating, rating_cnt)
