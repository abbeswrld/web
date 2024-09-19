import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = ''
        uic.loadUi('main.ui', self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())










