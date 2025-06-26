import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox

class TextViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("텍스트 뷰어")
        self.setGeometry(100, 100, 600, 400)

        # QTextEdit 위젯 생성
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # 메뉴바 생성
        menubar = self.menuBar()
        file_menu = menubar.addMenu("파일")

        # 파일 열기 액션
        open_action = QAction("열기", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", "Text Files (*.txt);;All Files (*)")
        if fname:
            try:
                # 다양한 인코딩 지원: 기본은 utf-8, 실패시 cp949(윈도우 한글) 시도
                try:
                    with open(fname, "r", encoding="utf-8") as f:
                        text = f.read()
                except UnicodeDecodeError:
                    with open(fname, "r", encoding="cp949") as f:
                        text = f.read()
                self.text_edit.setPlainText(text)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 열 수 없습니다:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextViewer()
    viewer.show()
    sys.exit(app.exec_())