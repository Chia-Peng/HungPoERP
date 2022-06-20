from PySide6 import QtWidgets

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
        self.ui.material_ComboBox.addItems(
            materialCalculation.getComboBoxList("MaterialList"))
        self.ui.style_ComboBox.addItems(
            materialCalculation.getComboBoxList("styleList"))

        self.ui.material_ComboBox.currentIndexChanged.connect(
            self.cboMaterialChanged)
        self.ui.style_ComboBox.currentIndexChanged.connect(
            self.cboStyleChanged)

        self.cboMaterialChanged()
        self.cboStyleChanged()
        # self.updateResult()

    def cboMaterialChanged(self):
        print(self.ui.material_ComboBox.currentText())
        pass

    def cboStyleChanged(self):
        selectStyle = self.ui.style_ComboBox.currentText()
        print(self.ui.style_ComboBox.currentText())
        # add img
        imgName = self.ui.style_ComboBox.currentText()
        self.ui.image_Label.setPixmap(
            materialCalculation.getstyleImage(imgName))
        # show Detailed Options
        self.detailedOptions(selectStyle)

    def updateResult(self):
        print('updateResult')
        # D = int(self.ui.cboStyle_D.currentText())
        # d = int(self.ui.cboStyle_d.currentText())
        # L = int(self.ui.lineEdit_L.text())
        # total = materialCalculation.calculate(D, d, L)
        # self.ui.label_Total.setText('%d' % total)

    def detailedOptions(self, style):
        self.ui.specTypeA.hide()
        self.ui.specTypeB.hide()
        self.ui.specTypeC.hide()
        self.uiDisconnect()
        self.clearData()

        if(style == '圓棒' or style == '六角棒'):
            print('切換TypeA')
            self.ui.specTypeA.show()
            # show label name
            if(style == '圓棒'):
                self.ui.typeA_Label_1.setText('外徑:')
                self.ui.typeA_Label_2.setText('長度(L):')
            elif(style == '六角棒'):
                self.ui.typeA_Label_1.setText('對邊長:')
                self.ui.typeA_Label_2.setText('長度(L):')
            # signal connect
            self.ui.typeA_ComboBox_1.currentIndexChanged.connect(
                self.updateResult)
            self.ui.typeA_LineEdit_1.textEdited.connect(self.updateResult)
            # add Data
            self.ui.typeA_ComboBox_1.addItems(
                materialCalculation.getComboBoxList("styleSize"))

        elif(style == '圓管'):
            print('切換TypeB')
            self.ui.specTypeB.show()
            # show label name
            self.ui.typeB_Label_1.setText('外徑:')
            self.ui.typeB_Label_2.setText('內徑:')
            self.ui.typeB_Label_3.setText('長度(L):')
            # signal connect
            self.ui.typeB_ComboBox_1.currentIndexChanged.connect(
                self.updateResult)
            self.ui.typeB_ComboBox_2.currentIndexChanged.connect(
                self.updateResult)
            self.ui.typeB_LineEdit_1.textEdited.connect(self.updateResult)
            # add Data
            self.ui.typeB_ComboBox_1.addItems(
                materialCalculation.getComboBoxList("styleSize"))
            self.ui.typeB_ComboBox_2.addItems(
                materialCalculation.getComboBoxList("styleSize"))

        elif(style == '鈑材'):
            print('切換TypeC')
            self.ui.specTypeC.show()
            # show label name
            self.ui.typeC_Label_1.setText('長度:')
            self.ui.typeC_Label_2.setText('寬度:')
            self.ui.typeC_Label_3.setText('厚度(t):')
            # signal connect
            self.ui.typeC_ComboBox_1.currentIndexChanged.connect(
                self.updateResult)
            self.ui.typeC_LineEdit_1.textEdited.connect(self.updateResult)
            self.ui.typeC_LineEdit_2.textEdited.connect(self.updateResult)
            # add Data
            self.ui.typeC_ComboBox_1.addItems(
                materialCalculation.getComboBoxList("styleSize"))

    def uiDisconnect(self):
        # Type A
        self.ui.typeA_ComboBox_1.disconnect(
            self.ui.typeA_ComboBox_1.currentIndexChanged.connect(self.updateResult))
        self.ui.typeA_LineEdit_1.disconnect(
            self.ui.typeA_LineEdit_1.textEdited.connect(self.updateResult))

        # Type B
        self.ui.typeB_ComboBox_1.disconnect(
            self.ui.typeB_ComboBox_1.currentIndexChanged.connect(self.updateResult))
        self.ui.typeB_ComboBox_2.disconnect(
            self.ui.typeB_ComboBox_2.currentIndexChanged.connect(self.updateResult))
        self.ui.typeB_LineEdit_1.disconnect(
            self.ui.typeB_LineEdit_1.textEdited.connect(self.updateResult))

        # Type C
        self.ui.typeC_ComboBox_1.disconnect(
            self.ui.typeC_ComboBox_1.currentIndexChanged.connect(self.updateResult))
        self.ui.typeC_LineEdit_1.disconnect(
            self.ui.typeC_LineEdit_1.textEdited.connect(self.updateResult))
        self.ui.typeC_LineEdit_2.disconnect(
            self.ui.typeC_LineEdit_2.textEdited.connect(self.updateResult))

    def clearData(self):
        self.ui.typeA_ComboBox_1.clear()
        self.ui.typeB_ComboBox_1.clear()
        self.ui.typeB_ComboBox_2.clear()
        self.ui.typeC_ComboBox_1.clear()
