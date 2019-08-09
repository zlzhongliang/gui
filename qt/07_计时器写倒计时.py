from PyQt5.Qt import *


class MyLabal(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(200,200)
        self.timer_id = self.startTimer(1000)
    def timerEvent(self, *args, **kwargs):
        a = int(self.text())-1
        self.setText(str(a))
        if a == 0:
            print("结束")
            self.killTimer(self.timer_id)

    def set_time(self,time):
        self.setText(str(time))



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('倒计时')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.labal = MyLabal(self)
        self.labal.set_time(100)




if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())