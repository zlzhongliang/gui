from PyQt5.Qt import *
import sys
class MyWindow(QWidget):
    def mouseMoveEvent(self, QMouseEvent):
        #  QMouseEvent.localPos(),QMouseEvent.globalPos() 鼠标在屏幕位置和在窗口位置
        print("鼠标移动了",QMouseEvent.localPos(),QMouseEvent.globalPos())
app = QApplication(sys.argv)

window = MyWindow()
window.setWindowTitle('鼠标形状自定义')
window.resize(500,500)
window.move(400,200)


pixmap = QPixmap("11_OWidget__鼠标的形状_3.PNG")  # 自定义鼠标样式的图片路径
new_pixmap = pixmap.scaled(10,10)  # 鼠标样式的大小
cursor = QCursor(new_pixmap,0,0)  # 确定鼠标样式，并确定热点坐标位置，默认为-1，-1（鼠标中心）
window.setCursor(cursor)  # 进入window这个控件后，表现为自定义的鼠标样式

# print(window.cursor().pos())  # 鼠标在整个屏幕窗口的位置
# window.cursor().setPos(0,0)  # 是相对于整个屏幕窗口设置位置
# window.unsetCursor()  # 重置鼠标样式

print(window.hasMouseTracking())  # 是否设置鼠标追踪
window.setMouseTracking(True)  # 设置鼠标追踪

window.show()

sys.exit(app.exec_())