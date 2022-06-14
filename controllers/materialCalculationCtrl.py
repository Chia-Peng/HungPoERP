from PySide6 import QtWidgets, QtGui, QtCore

from views.materialCalculationView import Ui_MainWindow


class materialCalculationController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
