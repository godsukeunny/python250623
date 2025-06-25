# web2.py
 # 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#웹서버에 요청
import urllib.request

f = open("clien.txt", "wt", encoding="utf-8")

# url = "https://www.clien.net/service/board/sold"
for i in range(0, 10):
    url = f"https://www.clien.net/service/board/sold?&od=T31&category=0&po={i}"
    print(url)
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    list = soup.find_all("span", attrs={"data-role": "list-title-text"})
    for tag in list:
        title = tag.text.strip()  # 태그의 텍스트 내용 추출
        print(title)  # 태그의 텍스트 내용 출력
        f.write(title + "\n")

f.close()            

# url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=0"

# data = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(data, "html.parser")
# list = soup.find_all("span", attrs={"data-role": "list-title-text"})
# for tag in list:
#     title = tag.text.strip()  # 태그의 텍스트 내용 추출
#     title = title.replace("\n", " ")  # 줄바꿈 제거
#     print(title)  # 태그의 텍스트 내용 출력

# <span class="subject_fixed" data-role="list-title-text" title="[예약중] 아이패드 미니 7 / 애플 케어 플러스 / 애플펜슬 프로">
#       [예약중] 아이패드 미니 7 / 애플 케어 플러스 / 애플펜슬 프로
# </span>

