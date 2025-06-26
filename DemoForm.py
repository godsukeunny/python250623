# DemoFrom.py
# DemoFrom.ui + DemoForm.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("안녕하세요. 파이썬qt5")


#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
