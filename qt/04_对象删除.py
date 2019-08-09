from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('对象删除')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()
        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1被释放了"))
        obj2.destroyed.connect(lambda : print("obj2被释放了"))
        obj3.destroyed.connect(lambda : print("obj3被释放了"))
        # del obj2  # 只是删除了对象的引用，但是对象本身没有被摧毁，依然被obj1引用，所以不会被垃圾回收
        # del self.obj1  # 删除对象引用，obj1没有被引用了，会被垃圾回收
        obj3.deleteLater()  # 整个方法执行完毕后，才会删除对象的引用，并且断开和obj2的关系，最后会被垃圾回收
        print(obj2.children())  # 上面的删除并不会马上执行，所以obj3依然存在



if __name__ == '__main__':
    import sys
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())