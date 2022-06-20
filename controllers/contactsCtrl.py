from PySide6 import QtWidgets, QtGui, QtCore

from views.contactsView import Ui_MainWindow


class contactsController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
