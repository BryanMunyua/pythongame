from pyqt5 import Qtwidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("PyQt5 Trial out")

    win.show()
    sys.exit(app.exec_())
