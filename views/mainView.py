# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 512, 768))
        self.BtnMaterialCalculation = QPushButton(self.widget)
        self.BtnMaterialCalculation.setObjectName(u"BtnMaterialCalculation")
        self.BtnMaterialCalculation.setGeometry(QRect(20, 51, 150, 50))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 200, 50))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.BtnMaterialSettings = QPushButton(self.widget)
        self.BtnMaterialSettings.setObjectName(u"BtnMaterialSettings")
        self.BtnMaterialSettings.setGeometry(QRect(200, 51, 150, 50))
        self.BtnCustomerQuotation = QPushButton(self.widget)
        self.BtnCustomerQuotation.setObjectName(u"BtnCustomerQuotation")
        self.BtnCustomerQuotation.setGeometry(QRect(20, 150, 150, 50))
        self.BtnQuotationSummary = QPushButton(self.widget)
        self.BtnQuotationSummary.setObjectName(u"BtnQuotationSummary")
        self.BtnQuotationSummary.setGeometry(QRect(200, 150, 150, 50))
        self.BtnCustomerOrder = QPushButton(self.widget)
        self.BtnCustomerOrder.setObjectName(u"BtnCustomerOrder")
        self.BtnCustomerOrder.setGeometry(QRect(20, 220, 150, 50))
        self.BtnOrderSummary = QPushButton(self.widget)
        self.BtnOrderSummary.setObjectName(u"BtnOrderSummary")
        self.BtnOrderSummary.setGeometry(QRect(200, 220, 150, 50))
        self.BtnSupplierInquiry = QPushButton(self.widget)
        self.BtnSupplierInquiry.setObjectName(u"BtnSupplierInquiry")
        self.BtnSupplierInquiry.setGeometry(QRect(20, 300, 150, 50))
        self.BtnSupplierSummary = QPushButton(self.widget)
        self.BtnSupplierSummary.setObjectName(u"BtnSupplierSummary")
        self.BtnSupplierSummary.setGeometry(QRect(200, 300, 150, 50))
        self.BtnSupplierPurchasing = QPushButton(self.widget)
        self.BtnSupplierPurchasing.setObjectName(u"BtnSupplierPurchasing")
        self.BtnSupplierPurchasing.setGeometry(QRect(20, 370, 150, 50))
        self.BtnPurchaseSummary = QPushButton(self.widget)
        self.BtnPurchaseSummary.setObjectName(u"BtnPurchaseSummary")
        self.BtnPurchaseSummary.setGeometry(QRect(200, 370, 150, 50))
        self.BtnWarehouseManagement = QPushButton(self.widget)
        self.BtnWarehouseManagement.setObjectName(u"BtnWarehouseManagement")
        self.BtnWarehouseManagement.setGeometry(QRect(20, 480, 150, 50))
        self.BtnCustomerSummary = QPushButton(self.widget)
        self.BtnCustomerSummary.setObjectName(u"BtnCustomerSummary")
        self.BtnCustomerSummary.setGeometry(QRect(200, 480, 150, 50))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(512, 0, 512, 768))
        self.listView = QListView(self.widget_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 0, 492, 750))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BtnMaterialCalculation.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u8a08\u7b97", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b8f\u5e1bERP", None))
        self.BtnMaterialSettings.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u8a2d\u5b9a", None))
        self.BtnCustomerQuotation.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u5831\u50f9", None))
        self.BtnQuotationSummary.setText(QCoreApplication.translate("MainWindow", u"\u5831\u50f9\u7e3d\u8868", None))
        self.BtnCustomerOrder.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u8a02\u55ae", None))
        self.BtnOrderSummary.setText(QCoreApplication.translate("MainWindow", u"\u8a02\u55ae\u7e3d\u8868", None))
        self.BtnSupplierInquiry.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u8a62\u50f9", None))
        self.BtnSupplierSummary.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u7e3d\u8868", None))
        self.BtnSupplierPurchasing.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u63a1\u8cfc", None))
        self.BtnPurchaseSummary.setText(QCoreApplication.translate("MainWindow", u"\u63a1\u8cfc\u7e3d\u8868", None))
        self.BtnWarehouseManagement.setText(QCoreApplication.translate("MainWindow", u"\u51fa/\u5165\u5eab", None))
        self.BtnCustomerSummary.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u6e05\u55ae", None))
    # retranslateUi

