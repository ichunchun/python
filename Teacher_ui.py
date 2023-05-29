# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teacher.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 322)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5bfc\u5458\u8bc4\u6d4b\u7ed3\u679c\u5fc5\u987b\u5728\u8f6f\u4ef6\u6839\u76ee\u5f55\u628a\u6587\u4ef6\u6539\u4e3a\uff1a</p><p>excel1\uff0cexcel2\uff0cexcel3\uff0cexcel4\uff0cexcel5\uff0cexcel6</p><p>\u6559\u5e08\u8bc4\u6d4b\u7ed3\u679c\u76f4\u63a5\u9009\u62e9\u6587\u4ef6\u540e\u70b9\u51fb\u5bf9\u5e94\u7684\u6309\u952e\uff1a</p><p>\u7ed3\u679c\u4f1a\u751f\u6210\u5728\u8f6f\u4ef6\u6839\u76ee\u5f55</p><p>\u9886\u5bfc\u8bc4\u6d4b\u7ed3\u679c\u9700\u8981\u628a\u6700\u540e\u7684\u591a\u4f59\u7684\u884c\u5220\u9664\uff0c\u4fdd\u8bc1\u884c\u6570\u662f5\u7684\u500d\u6570\u70b9\u51fb\u5bf9\u5e94\u7684\u6309\u952e\uff1a</p><p>\u7ed3\u679c\u4f1a\u751f\u6210\u5728\u8f6f\u4ef6\u6839\u76ee\u5f55</p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08\u8bc4\u6d4b\u7ed3\u679c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5458\u8bc4\u6d4b\u7ed3\u679c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9886\u5bfc\u8bc4\u6d4b\u7ed3\u679c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

