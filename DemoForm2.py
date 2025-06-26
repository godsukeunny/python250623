# DemoFrom2.py
# DemoFrom2.ui + DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 # 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#웹서버에 요청
import urllib.request

#디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#윈도우 클래스 정의(QDialog,  QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("안녕하세요. 파이썬qt5")

    #슬롯메서드 추가
    def firstClick(self):
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
        self.label.setText("첫번째 버튼이 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼이 클릭했음")
    def thirdClick(self):
        self.label.setText("세번째 버튼이 클릭했음~~")


#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
