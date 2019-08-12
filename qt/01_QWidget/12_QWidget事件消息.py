from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pass
    labal.grabkKeyboard()

    def showEvent(self, QShowEvent):
        print("窗口被展示了")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())