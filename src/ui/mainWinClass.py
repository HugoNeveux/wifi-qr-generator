# coding: utf8

from ui.mainWinui import Ui_MainWindow
from ui.qrDialogClass import QRDialog
from ui.qrCodeImage import Image
from PySide6.QtWidgets import QMainWindow
import wifiqr


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def create_custom_qr(self):
        ssid = self.ui.customSsidInput.text()
        password = self.ui.customPasswordInput.text()

        img = wifiqr.generate(ssid, password).make_image(image_factory=Image)

        qr_dialog = QRDialog(img)
        res = qr_dialog.exec_()
