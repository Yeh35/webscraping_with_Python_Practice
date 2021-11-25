from selenium import webdriver
from bs4 import BeautifulSoup
import time

interval = 2

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 1080 해상도 만큼 내린다.
# browser.execute_script("window.scrollTo(0, 2080)") 

prev_heigh = browser.execute_script("return document.body.scrollHeight") # 문서 높이

while True:
    # 지정한 위치로 스크롤 내리기 (화면 가장 아래)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

    time.sleep(interval) # 로딩 대기

    curr_heigh = browser.execute_script("return document.body.scrollHeight") # 문서 높이

    print(f"curr_heigh({curr_heigh}), prev_heigh({prev_heigh})")

    if prev_heigh >= curr_heigh :
        break

    prev_heigh = curr_heigh

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(f"영화제목: {title}")
    
print(len(movies))
browser.quit()