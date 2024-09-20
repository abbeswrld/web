import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        pixmap = QPixmap("14.png")

        # Устанавливаем картинку в QLabel
        self.image.setPixmap(pixmap)

    def initUI(self):
        uic.loadUi('main_v2.ui', self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
