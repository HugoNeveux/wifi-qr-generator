# coding: utf8

from ui.qrDialogui import Ui_Dialog
from PySide6.QtWidgets import QDialog


class QRDialog(QDialog):
    def __init__(self, img):
        QDialog.__init__(self, parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        pix = img.pixmap()
        self.ui.qrCodeLabel.setPixmap(pix)

