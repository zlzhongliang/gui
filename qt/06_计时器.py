from PyQt5.Qt import *


class MyQObject(QObject):
    def timerEvent(self, evt):
        print(evt,"1")



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计时器')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.obj = MyQObject()
        timer_id = self.obj.startTimer(1000)
        print(11)
        # self.obj.killTimer(timer_id)  # 关闭定时器

if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())