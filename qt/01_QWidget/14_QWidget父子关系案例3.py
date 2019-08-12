from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):  # 点击的控件没有设置点击事件，就会穿到父类中
        # print(1)
        local_x = QMouseEvent.x()
        local_y = QMouseEvent.y()
        # print(local_x,local_y)
        labal_flag = self.childAt(local_x,local_y)  # 根据位置找到子控件
        if labal_flag:
            labal_flag.setStyleSheet("background-color: red")


app = QApplication(sys.argv)

window = Window()
window.setWindowTitle('父子关系案例')
window.resize(500,500)
window.move(400,200)

for i in range(1,11):
    labal = QLabel(window)
    labal.setText("标签"+str(i))
    labal.move(40*i,40*i)


window.show()

sys.exit(app.exec_())
