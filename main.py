import sys

from PyQt5 import uic
from PyQt5.Qt import QImage
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from consts import *
from util import get_pict

spn = 0.004


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.loadInfo()

    def loadInfo(self):
        self.setGeometry(1000, 200, *SIZE)
        self.setWindowTitle('yandex map')
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
        )

        self.pict.resize(W, H)
        self.update_pict(spn)

    def keyPressEvent(self, event):
        global spn
        if spn + d < 180 and event.key() == Qt.Key_Up:
            spn = round(spn + d, 3)
            self.update_pict(spn)
            print(spn)

        if spn - d > 0.001 and event.key() == Qt.Key_Down:
            spn = round(spn - d, 3)
            self.update_pict(spn)
            print(spn)

    def update_pict(self, new_spn: float):
        path = get_pict(lon, lat, str(new_spn))
        pixmap = QPixmap(QImage(path))
        self.pict.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
