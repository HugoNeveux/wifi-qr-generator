# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(211, 74)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qrCodeLabel = QLabel(Dialog)
        self.qrCodeLabel.setObjectName(u"qrCodeLabel")

        self.verticalLayout.addWidget(self.qrCodeLabel)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(accessibility)
        self.qrCodeLabel.setAccessibleDescription(QCoreApplication.translate("Dialog", u"pix", None))
#endif // QT_CONFIG(accessibility)
        self.qrCodeLabel.setText(QCoreApplication.translate("Dialog", u"QR code", None))
    # retranslateUi

