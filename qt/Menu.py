from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt继承语法')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        labal = QLabel(self)
        labal.setText('Qt继承的基本语法')
        labal.move(200,200)


if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())

