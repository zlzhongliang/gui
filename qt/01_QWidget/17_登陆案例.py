from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登陆')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        labal = QLabel(self)
        labal.setText("标签")
        labal.move(150,50)
        labal.hide()

        text_edit = QLineEdit(self)
        text_edit.move(150,100)
        def text_change(text):
            if len(text):
                button.setEnabled(True)
            else:
                button.setEnabled(False)
        text_edit.textChanged.connect(text_change)

        button = QPushButton(self)
        button.move(150,150)
        button.setText("登陆")
        button.setEnabled(False)
        def button_pressed():
            if text_edit.text() == "password":
                labal.setText("登陆成功")
                labal.show()
            else:
                labal.setText("登陆失败")
                labal.show()
        button.pressed.connect(button_pressed)



if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())