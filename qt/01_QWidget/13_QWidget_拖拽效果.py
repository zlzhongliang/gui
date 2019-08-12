from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('拖拽效果')
        self.resize(500,500)
        self.setup_ui()
        self.move_flag = False

    def setup_ui(self):
        pass

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 左右键判断
            self.move_flag = True  # 如果设置了鼠标追踪，就必须添加鼠标按下的标记，否则触发移动就会崩溃
            print('鼠标被按下')
            self.mouse_x = QMouseEvent.globalX()
            self.mouse_y = QMouseEvent.globalY()
            # print(self.mouse_x,self.mouse_y)
            self.window_old_x = self.x()
            self.window_old_y = self.y()
            # print(self.window_old_x,self.window_old_y)

    def mouseMoveEvent(self, QMouseEvent):
        if self.move_flag:
            print("鼠标被移动了")
            self.move_x = QMouseEvent.globalX()-self.mouse_x
            self.move_y = QMouseEvent.globalY()-self.mouse_y
            # print(self.move_x,self.move_y)
            self.move(self.window_old_x+self.move_x,self.window_old_y+self.move_y)


    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False
        print("鼠标被释放了")


if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.setMouseTracking(True)
        window.show()
        sys.exit(app.exec())