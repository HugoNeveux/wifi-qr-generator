from ui.mainWinui import Ui_MainWindow
from PySide6 import QtGui


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_signals()
