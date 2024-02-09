import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage

from consts import *
from picture import k


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.loadInfo()

    def loadInfo(self):
        self.setFixedSize(*SIZE)
        self.setWindowTitle('')
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
        )

        self.pict.resize(W, H)

        ans = k()
        pixmap = QPixmap(QImage(ans))
        pixmap = pixmap.scaled(W, H)
        self.pict.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
