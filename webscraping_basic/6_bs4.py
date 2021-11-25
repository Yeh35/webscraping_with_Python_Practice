import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday";
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 개체에서 처음 발견되는 a element
print(soup.a.attrs) # a element의 속성 정보
print(soup.a["href"])  # a element의 href 속성 정보

print(soup.find("a", attrs={"class": "Nbtn_upload"})) # find는 해당하는 첫번째 element를 찾아옴
print(soup.find(attrs={"class": "Nbtn_upload"})) # 테그를 안적어줘도 해당하는 첫번째 element를 찾아옴

rank01 = soup.find("li", attrs={"class": "rank01"}) 
print(rank01.a.getText())

rank02 = rank01.next_sibling.next_sibling # next_sibling은 다음 테그를 가져옴, 개행이 있는 경우 두번 사용해야할 수도 있다.
print(rank02.a.getText())

rank03 = rank02.next_sibling.next_sibling 
print(rank03.a.getText())

rank02 = rank03.previous_sibling.previous_sibling # previous_sibling은 이전 테그를 가져옴 
print(rank02.a.getText())


rankParent = rank01.parent # 부모 테그를 가져옴
print(rankParent)

rank02 = rank01.find_next_sibling("li")  # next_sibling와 다르게 조건에 맞는 테그로 바로 넘어갈 수 있다.
print(rank02.a.getText())

rank03 = rank02.find_next_sibling("li")
print(rank03.a.getText())

rank02 = rank03.find_previous_sibling("li") # 이전도 가능
print(rank02.a.getText())


ranks = rank01.find_next_siblings("li") # 조건에 맞는 형제 테그를 전부 가져옴
print(ranks)


webtoon = soup.find("a", text="소녀의 세계") # soup을 만들때부터 find로 찾아서 만들 수 있다.
print(webtoon)
