import math
from PySide6 import QtWidgets

from views.materialCalculationView import Ui_MainWindow
from model.materialCalculation import materialCalculation


class materialCalculationController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # init
        self.density = "0.85"
        self.unitPrice = '10'
        self.type = 'a'
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
        self.updateResult()

    # 選擇材質，變更密度
    def cboMaterialChanged(self):
        print(self.ui.material_ComboBox.currentText())
        self.ui.density_Label.setText(self.density)
        self.ui.unitPrice_Label.setText(self.unitPrice)

    # 選擇樣式
    def cboStyleChanged(self):
        self.selectStyle = self.ui.style_ComboBox.currentText()
        print(self.ui.style_ComboBox.currentText())
        # add img
        imgName = self.ui.style_ComboBox.currentText()
        self.ui.image_Label.setPixmap(
            materialCalculation.getstyleImage(imgName))
        # show Detailed Options
        self.detailedOptions(self.selectStyle)

    def updateResult(self):
        print('updateResult' + self.type)
        if(self.type == 'a'):
            item_1 = int(self.ui.typeA_ComboBox_1.currentText())
            item_2 = 0
            item_3 = int(self.ui.typeA_LineEdit_1.text())
        elif(self.type == 'b'):
            item_1 = int(self.ui.typeB_ComboBox_1.currentText())
            item_2 = int(self.ui.typeB_ComboBox_2.currentText())
            item_3 = int(self.ui.typeB_LineEdit_1.text())
        elif(self.type == 'c'):
            item_1 = int(self.ui.typeC_ComboBox_1.currentText())
            item_2 = int(self.ui.typeC_LineEdit_1.text())
            item_3 = int(self.ui.typeC_LineEdit_2.text())

        # 計算體積
        total = materialCalculation.volumeCalculation(
            item_1, item_2, item_3, self.selectStyle)

        # 計算重量
        total = materialCalculation.weightCalculation(
            total, self.density, self.unitPrice)
        #
        total = math.ceil(total)
        self.ui.total_Label.setText(str(total))

    def detailedOptions(self, style):
        self.ui.specTypeA.hide()
        self.ui.specTypeB.hide()
        self.ui.specTypeC.hide()
        self.uiDisconnect()
        self.clearData()

        if(style == '圓棒' or style == '六角棒'):
            print('切換TypeA')
            self.ui.specTypeA.show()
            self.type = 'a'
            # show label name
            if(style == '圓棒'):
                self.ui.typeA_Label_1.setText('外徑 :')
                self.ui.typeA_Label_2.setText('長度(L) :')
            elif(style == '六角棒'):
                self.ui.typeA_Label_1.setText('對邊長 :')
                self.ui.typeA_Label_2.setText('長度(L) :')
            # signal connect
            self.ui.typeA_ComboBox_1.currentIndexChanged.connect(
                self.updateResult)
            self.ui.typeA_LineEdit_1.textEdited.connect(self.updateResult)
            # add Data
            self.ui.typeA_ComboBox_1.addItems(
                materialCalculation.getComboBoxList("styleSize"))

        elif(style == '圓管'):
            print('切換TypeB')
            self.type = 'b'
            self.ui.specTypeB.show()
            # show label name
            self.ui.typeB_Label_1.setText('外徑 :')
            self.ui.typeB_Label_2.setText('內徑 :')
            self.ui.typeB_Label_3.setText('長度(L) :')
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
            self.type = 'c'
            self.ui.specTypeC.show()
            # show label name
            self.ui.typeC_Label_1.setText('厚度(t) :')
            self.ui.typeC_Label_2.setText('長度 :')
            self.ui.typeC_Label_3.setText('寬度 :')
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
