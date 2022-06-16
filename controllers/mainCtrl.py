from PySide6 import QtWidgets, QtGui, QtCore

from views.mainView import Ui_MainWindow


class mainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BtnMaterialCalculation.clicked.connect(
            self.screenChange)
        self.ui.BtnMaterialSettings.clicked.connect(
            self.screenChange)
        self.ui.BtnCustomerQuotation.clicked.connect(
            self.screenChange)
        self.ui.BtnQuotationSummary.clicked.connect(
            self.screenChange)
        self.ui.BtnCustomerOrder.clicked.connect(
            self.screenChange)
        self.ui.BtnOrderSummary.clicked.connect(
            self.screenChange)
        self.ui.BtnSupplierInquiry.clicked.connect(
            self.screenChange)
        self.ui.BtnSupplierSummary.clicked.connect(
            self.screenChange)
        self.ui.BtnSupplierPurchasing.clicked.connect(
            self.screenChange)
        self.ui.BtnPurchaseSummary.clicked.connect(
            self.screenChange)
        self.ui.BtnWarehouseManagement.clicked.connect(
            self.screenChange)
        self.ui.BtnCustomerSummary.clicked.connect(
            self.screenChange)

    def screenChange(self):
        from main import main
        objectName = self.sender().objectName()
        main.entryChanged(self, objectName)
