from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('鼠标案例')
        self.resize(500, 500)
        self.move(400, 200)
        self.setMouseTracking(True)
        self.labal = QLabel(self)
        self.labal.move(100, 100)
        self.labal.setText("测试测试")
        self.labal.setStyleSheet("background-color: cyan;")

    def mouseMoveEvent(self, mv):
        print(mv.localPos())
        # labal = self.findChild(QLabel)
        self.labal.move(mv.localPos().x(),mv.localPos().y())

app = QApplication(sys.argv)

window = Window()


window.show()

sys.exit(app.exec_())