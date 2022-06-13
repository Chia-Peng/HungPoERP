from PySide6 import QtWidgets, QtGui, QtCore

from views.materialCalculationView import Ui_MainWindow


class materialCalculationController(QtWidgets.QMainWindow):
    def showUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
