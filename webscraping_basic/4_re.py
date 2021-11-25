import re # 정규식 라이브러리

# 정규식 규정
p = re.compile("c..e")  # '.'은 하나의 문자를 의미

m = p.match("caseless") # 주어진 문자열의 처음부터 일치하는지 확인
if m: 
    print(m.group()) # 일치하는 문자열 반환
    print(m.string) # 입력 받은 문자열
    print(m.start())  # 일치하는 문자열의 시작 index
    print(m.end())  # 일치하는 문자열의 마지막 index
    print(m.span())  # 일치하는 문자열의 시작과 마지막 index
else :
    print("매칭되지 않음")

print()

m = p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
if m: 
    print(m.group()) # 일치하는 문자열 반환
    print(m.string) # 입력 받은 문자열
    print(m.start())  # 일치하는 문자열의 시작 index
    print(m.end())  # 일치하는 문자열의 마지막 index
    print(m.span())  # 일치하는 문자열의 시작과 마지막 index
else :
    print("매칭되지 않음")

print()

list = p.findall("good care care") # 일치하는 모든 것을 리스트 형태로 반환
if len(list) > 0: 
    print(list);
else :
    print("매칭되지 않음")