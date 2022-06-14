# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materialCalculationView.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 400, 300))
        self.styleImage = QLabel(self.widget)
        self.styleImage.setObjectName(u"styleImage")
        self.styleImage.setGeometry(QRect(0, 0, 400, 300))
        self.specWidget = QWidget(self.centralwidget)
        self.specWidget.setObjectName(u"specWidget")
        self.specWidget.setGeometry(QRect(30, 330, 400, 350))
        self.specLabels = QWidget(self.specWidget)
        self.specLabels.setObjectName(u"specLabels")
        self.specLabels.setGeometry(QRect(0, 0, 200, 350))
        self.label_2 = QLabel(self.specLabels)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 200, 50))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(self.specLabels)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 51, 200, 50))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5 = QLabel(self.specLabels)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 153, 200, 50))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4 = QLabel(self.specLabels)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 102, 200, 50))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6 = QLabel(self.specLabels)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 204, 200, 50))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_8 = QLabel(self.specLabels)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 255, 200, 50))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.specInputWidget = QWidget(self.specWidget)
        self.specInputWidget.setObjectName(u"specInputWidget")
        self.specInputWidget.setGeometry(QRect(200, 0, 200, 350))
        self.cboStyle_d = QComboBox(self.specInputWidget)
        self.cboStyle_d.setObjectName(u"cboStyle_d")
        self.cboStyle_d.setGeometry(QRect(0, 153, 200, 40))
        self.cboStyle = QComboBox(self.specInputWidget)
        self.cboStyle.setObjectName(u"cboStyle")
        self.cboStyle.setGeometry(QRect(0, 51, 200, 40))
        self.cboStyle_D = QComboBox(self.specInputWidget)
        self.cboStyle_D.setObjectName(u"cboStyle_D")
        self.cboStyle_D.setGeometry(QRect(0, 102, 200, 40))
        self.cboMaterial = QComboBox(self.specInputWidget)
        self.cboMaterial.setObjectName(u"cboMaterial")
        self.cboMaterial.setGeometry(QRect(0, 0, 200, 40))
        self.label_Total = QLabel(self.specInputWidget)
        self.label_Total.setObjectName(u"label_Total")
        self.label_Total.setGeometry(QRect(0, 255, 200, 40))
        self.label_Total.setFont(font)
        self.label_Total.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lineEdit_L = QLineEdit(self.specInputWidget)
        self.lineEdit_L.setObjectName(u"lineEdit_L")
        self.lineEdit_L.setGeometry(QRect(0, 204, 200, 40))
        self.lineEdit_L.raise_()
        self.cboStyle_d.raise_()
        self.cboStyle.raise_()
        self.cboStyle_D.raise_()
        self.cboMaterial.raise_()
        self.label_Total.raise_()
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(460, 30, 550, 650))
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 550, 650))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
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
        self.styleImage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1.\u6750\u8cea(Material) :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2.\u6a23\u5f0f(Style) :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4.\u5167\u5f91(d) :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"3.\u5916\u5f91(D) :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"5.\u9577\u5ea6(L) :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"6.\u5408\u8a08(Total) :", None))
        self.label_Total.setText("")
        self.lineEdit_L.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u898f\u683c\u8868", None))
    # retranslateUi

