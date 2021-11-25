import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885";
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 만화 재목 + 링크 가져오기
# cartoons = soup.find_all("td", attrs={"class": "title"})
# for cartoon in cartoons:
#     title = cartoon.a.getText()
#     link = "https://comic.naver.com" + cartoon.a["href"]

#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    total_rates += float(cartoon.find("strong").getText())

print(total_rates / len(cartoons))