from PyQt5.Qt import *
import sys
from Menu import Window

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())