from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('测试live代码快捷模板的使用')
window.resize(500,500)
window.move(400,200)

labal = QLabel(window)
labal.setText("测试")
labal.move(200,200)

window.show()

sys.exit(app.exec_())