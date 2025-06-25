# web1.py
#웹크롤링을 위한 선언 
from bs4 import BeautifulSoup

#문서를 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())  # 문서 구조를 보기 좋게 출력

# print(soup.find_all("p"))
# print(soup.find("p"))

print(soup.find_all("p", class_="outer-text"))
print(soup.find_all("p", attrs={"class": "outer-text"}))


# for tag in soup.find_all("p"):
#     title = tag.text.strip()  # 태그의 텍스트 내용 추출
#     title = ti:
#     print(tag.text)  # 태그의 텍스트 내용 출력