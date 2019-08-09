from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        self.obj=QObject()

        def destroy_cao(obj):  # obj来自于信号，信号可以将自己传输给槽
            print("被释放了",obj)
        self.obj.destroyed.connect(destroy_cao)  # obj.destroyed（obj被释放的信号） connect（连接） destroy_cao(槽函数)
        # self.obj.destroyed.disconnect(destroy_cao)  # 断开连接
        # self.obj.blockSignals(True)  # 临时阻止连接
        # self.obj.blockSignals(False)  # 恢复连接
        # print(self.obj.receivers(self.obj.destroyed))  # 返回连接数量
        del self.obj  # 释放obj


if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())