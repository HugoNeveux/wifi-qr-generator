#!/usr/bin/python3
# coding: utf8

import sys
import wifiqr
import qrcode
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap, QPainter
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import QFile, Qt
# TODO: add libopengl0 to system requirements


class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self._image = QImage(
            size, size, QImage.Format_RGB16)
        self._image.fill(Qt.white)

    def pixmap(self):
        return QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        painter = QPainter(self._image)
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            Qt.black)

    def save(self, stream, kind=None):
        pass


class QRWindow(QWidget):
    def __init__(self, img):
        super().__init__()

        layout = QVBoxLayout()

        pix = img.pixmap()
        self.lbl = QLabel()
        self.lbl.setPixmap(pix)

        layout.addWidget(self.lbl)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ui_file = QFile("ui/mainwindow.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.custom_ssid_input = self.window.findChild(QLineEdit, 'customSsidInput')
        self.custom_password_input = self.window.findChild(QLineEdit, 'customPasswordInput')

        self.custom_qr_btn = self.window.findChild(QPushButton, 'createQr')
        self.custom_qr_btn.clicked.connect(self.create_custom)

    def create_custom(self):
        ssid = self.custom_ssid_input.text()
        password = self.custom_password_input.text()

        img = wifiqr.generate(ssid, password).make_image(image_factory=Image)
        new_window = QRWindow(img)
        print("New window created")
        new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.window.show()
    sys.exit(app.exec_())
