from PySide6 import QtWidgets, QtGui, QtCore

from views.materialCalculationView import Ui_MainWindow
from model.materialCalculation import materialCalculation


class materialCalculationController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # MainWindow Title
        self.setWindowTitle("材料計算")
        # add combobox
        self.ui.cboMaterial.addItems(
            materialCalculation.getComboBoxList("MaterialList"))
        self.ui.cboStyle.addItems(
            materialCalculation.getComboBoxList("styleList"))
        self.ui.cboStyle_D.addItems(
            materialCalculation.getComboBoxList("styleList_D"))
        self.ui.cboStyle_d.addItems(
            materialCalculation.getComboBoxList("styleList_d"))

        self.ui.cboMaterial.currentIndexChanged.connect(
            self.cboMaterialChanged)
        self.ui.cboStyle.currentIndexChanged.connect(self.cboStyleChanged)
        self.ui.cboStyle_D.currentIndexChanged.connect(self.updateResult)
        self.ui.cboStyle_d.currentIndexChanged.connect(self.updateResult)
        self.ui.lineEdit_L.textEdited.connect(self.updateResult)
        self.cboStyleChanged()
        self.updateResult()

    def cboMaterialChanged(self):
        pass

    def cboStyleChanged(self):
        # add img
        imgName = self.ui.cboMaterial.currentText()
        self.ui.styleImage.setPixmap(
            materialCalculation.getstyleImage(imgName))

    def updateResult(self):
        print('display')
        D = int(self.ui.cboStyle_D.currentText())
        d = int(self.ui.cboStyle_d.currentText())
        L = int(self.ui.lineEdit_L.text())
        total = materialCalculation.calculate(D, d, L)
        self.ui.label_Total.setText('%d' % total)
