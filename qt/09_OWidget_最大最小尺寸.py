from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('最大尺寸-最小尺寸')
# window.resize(500,500)  # 自由尺寸
# window.setFixedSize(500,500)  # 固定尺寸
window.setMaximumSize(200,200)

window.move(400,200)




window.show()

sys.exit(app.exec_())