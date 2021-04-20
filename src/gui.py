#!/usr/bin/python3
# coding: utf8

import sys
from PySide6.QtWidgets import QApplication
from ui.mainWinClass import MainWin


def main():
    app = QApplication(sys.argv)
    win = MainWin()

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
