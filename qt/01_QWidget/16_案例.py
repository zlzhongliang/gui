from PyQt5.Qt import *
import sys
#
# class Button(QPushButton):
#     def mousePressEvent(self, *args, **kwargs):
#         print(1)
#         if self.x()==260 and self.y()== 0:
#             print(2)
#             self.parentWidget().setWindowState(Qt.WindowMinimized)
#         elif self.x() == 340 and self.y() == 0:
#             print(3)
#             self.parentWidget().setWindowState(Qt.WindowMaximized)
#         elif self.x() == 420 and self.y() == 0:
#             print(4)
#             self.parentWidget().close()

class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowOpacity(0.9)
        self.resize(500, 500)
        self.move(400, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.button_x = 80
        self.button_y = 40
        self.window_w = self.width()
        self.get_close_button()
        self.get_max_button()
        self.get_min_button()


    def get_close_button(self):
        self.close_btn = QPushButton(self)
        self.close_btn.resize(self.button_x, self.button_y)
        self.close_btn.setText("关闭")
        self.close_btn.pressed.connect(self.close)

    def get_max_button(self):
        self.max_button = QPushButton(self)
        self.max_button.resize(self.button_x, self.button_y)
        self.max_button.setText("最大化")


        def max_nornal():
            if window.isMaximized():
                window.showNormal()
                self.max_button.setText("最大化")
            else:
                window.showMaximized()
                self.max_button.setText('初始状态')

        self.max_button.pressed.connect(max_nornal)

    def get_min_button(self):
        self.min_button = QPushButton(self)
        self.min_button.resize(self.button_x, self.button_y)
        self.min_button.setText("最小化")

        self.min_button.pressed.connect(self.showMinimized)

    def resizeEvent(self, QResizeEvent):
        print(1)
        self.window_w = self.width()
        self.close_btn.move(self.window_w - self.button_x, 0)
        self.max_button.move(self.window_w - self.button_x * 2, 0)
        self.min_button.move(self.window_w - self.button_x * 3, 0)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window()
    window.setWindowTitle('窗口设置')

    window.show()

    sys.exit(app.exec_())