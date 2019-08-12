from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QWidget')
window.resize(500,500)
window.move(400,200)
window.show()

obj_count = 27
width = 100
hight = 80
tr_count = window.width() / width
for i in range(0,obj_count):
    tr = i // tr_count
    td = i % tr_count

    red = QWidget(window)
    red.resize(80,70)
    red.move(td*width,tr*hight)
    red.setStyleSheet("background-color: red")
    red.show()


sys.exit(app.exec_())