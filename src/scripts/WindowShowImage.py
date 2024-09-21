import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        pixmap = QPixmap("../resources/images/14.png")

        self.image.setPixmap(pixmap)


    def initUI(self):
        uic.loadUi('../resources/UI/main_v2.ui', self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageWindow()
    ex.show()
    sys.exit(app.exec())
