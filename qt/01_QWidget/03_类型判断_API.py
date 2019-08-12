from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('类型判断_API')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        for o in objs:
            print(o.isWidgetType())  # 类型判断
            print(o.inherits("QWidget"))  # 类型判断


if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())