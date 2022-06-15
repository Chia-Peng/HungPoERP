# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainView.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
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
        self.widget.setGeometry(QRect(0, 0, 512, 768))
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 51, 150, 50))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 200, 50))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 51, 150, 50))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 150, 150, 50))
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(200, 150, 150, 50))
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 220, 150, 50))
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(200, 220, 150, 50))
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 300, 150, 50))
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(200, 300, 150, 50))
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 370, 150, 50))
        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(200, 370, 150, 50))
        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(20, 480, 150, 50))
        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(200, 480, 150, 50))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u8a08\u7b97", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ERP\u529f\u80fd\u6e2c\u8a66", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u8a2d\u5b9a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u5831\u50f9", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5831\u50f9\u7e3d\u8868", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u8a02\u55ae", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u8a02\u55ae\u7e3d\u8868", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u8a62\u50f9", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u7e3d\u8868", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u5ee0\u5546\u63a1\u8cfc", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u63a1\u8cfc\u7e3d\u8868", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u51fa/\u5165\u5eab", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6236\u6e05\u55ae", None))
    # retranslateUi

