# coding: utf8

from ui.qrDialogui import Ui_Dialog
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox


class QRDialog(QDialog):
    def __init__(self, img):
        QDialog.__init__(self, parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.pix = img.pixmap()
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.buttonBox.accepted.connect(self.save_image)
        self.ui.qrCodeLabel.setPixmap(self.pix)

    def save_image(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix(".png")
        save_file_path = file_dialog.getSaveFileName(self, "Save image", "", "Images (*.png *.jpg);;All files (*)")
        self.pix.save(save_file_path[0])
