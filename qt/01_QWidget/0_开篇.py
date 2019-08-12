from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('社会我亮哥，人狠话不多')
window.resize(500,500)
window.move(400,200)
label = QLabel(window)
label.setText("hello world")
label.move(200,200)
window2 = QWidget()
window2.show()
window.show()

sys.exit(app.exec_())