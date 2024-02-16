import sys

from PyQt5 import uic
from PyQt5.Qt import QImage
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from consts import *
from util import get_pict


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.z = z
        self.loadInfo()

    def loadInfo(self):
        self.setGeometry(1000, 200, *SIZE)
        self.setWindowTitle('yandex map')
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
        )

        self.pict.resize(W - 20, H - 20)
        self.pict.move(10, 10)
        self.update_pict(z)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp and self.z + d <= 21:
            self.z += d
            self.update_pict(self.z)
            print(self.z)

        if event.key() == Qt.Key_PageDown and self.z - d >= 0:
            self.z -= d
            self.update_pict(self.z)
            print(self.z)

        return

    def update_pict(self, new_z: int):
        path = get_pict(lon, lat, str(new_z))
        pixmap = QPixmap(QImage(path))
        self.pict.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
