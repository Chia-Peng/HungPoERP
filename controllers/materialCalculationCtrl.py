from PySide6 import QtWidgets, QtGui, QtCore

from views.materialCalculationView import Ui_MainWindow


class materialCalculationController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # add img
        pixmap = QtGui.QPixmap('resources\\img\\styleImage.png')
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.styleImage.setPixmap(pixmap)
        # add combobox
        MaterialList = ['SS400', 'S150C', 'S45C',
                        'SCM415(SCM21)', 'SCM440(SCM4)']
        styleList = ['圓柱', '方管', '鋁擠型', '中空圓管']
        styleList_D = ['10', '20', '30', '40']
        styleList_d = ['5', '10', '15', '20']
        self.ui.cboMaterial.addItems(MaterialList)
        self.ui.cboStyle.addItems(styleList)
        self.ui.cboStyle_D.addItems(styleList_D)
        self.ui.cboStyle_d.addItems(styleList_d)
        self.ui.cboMaterial.currentIndexChanged.connect(self.display)
        self.ui.cboStyle.currentIndexChanged.connect(self.display)
        self.ui.cboStyle_D.currentIndexChanged.connect(self.display)
        self.ui.cboStyle_d.currentIndexChanged.connect(self.display)
        self.ui.lineEdit_L.textEdited.connect(self.display)
        self.display()

    def display(self):
        D = int(self.ui.cboStyle_D.currentText())
        d = int(self.ui.cboStyle_d.currentText())
        L = int(self.ui.lineEdit_L.text())
        total = D*d*L
        self.ui.label_Total.setText('%d' % total)
