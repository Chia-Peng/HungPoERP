from PySide6 import QtWidgets, QtGui, QtCore

from views.mainView import Ui_MainWindow
from controllers.materialCalculationCtrl import materialCalculationController


class mainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        materialCalculationController.showUI(self)
