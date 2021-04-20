# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 482)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NetworksList = QListWidget(self.groupBox_2)
        self.NetworksList.setObjectName(u"NetworksList")

        self.verticalLayout.addWidget(self.NetworksList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.GenerateFromListButton = QPushButton(self.groupBox_2)
        self.GenerateFromListButton.setObjectName(u"GenerateFromListButton")

        self.horizontalLayout_2.addWidget(self.GenerateFromListButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.customPasswordInput = QLineEdit(self.groupBox)
        self.customPasswordInput.setObjectName(u"customPasswordInput")
        self.customPasswordInput.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.customPasswordInput)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_2)

        self.customSsidInput = QLineEdit(self.groupBox)
        self.customSsidInput.setObjectName(u"customSsidInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.customSsidInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.createQr = QPushButton(self.groupBox)
        self.createQr.setObjectName(u"createQr")

        self.horizontalLayout.addWidget(self.createQr)


        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 32))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.NetworksList, self.GenerateFromListButton)
        QWidget.setTabOrder(self.GenerateFromListButton, self.customSsidInput)
        QWidget.setTabOrder(self.customSsidInput, self.customPasswordInput)
        QWidget.setTabOrder(self.customPasswordInput, self.createQr)

        self.retranslateUi(MainWindow)
        self.customPasswordInput.returnPressed.connect(self.createQr.click)
        self.createQr.clicked.connect(MainWindow.createCustomQR)
        self.customSsidInput.returnPressed.connect(self.customPasswordInput.setFocus)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Registered networks", None))
        self.GenerateFromListButton.setText(QCoreApplication.translate("MainWindow", u"Create QR code for selection", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.customPasswordInput.setText("")
        self.customPasswordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wi-Fi password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SSID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.customSsidInput.setText("")
        self.customSsidInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SSID", None))
        self.createQr.setText(QCoreApplication.translate("MainWindow", u"Create QR code", None))
    # retranslateUi

