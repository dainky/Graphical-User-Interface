# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(500, 300)
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")
        self.lblFirst.setStyleSheet(u"background-color: blue; color: white;")

        self.gridLayout.addWidget(self.lblFirst, 0, 0, 1, 1)

        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName(u"entFirst")

        self.gridLayout.addWidget(self.entFirst, 0, 1, 1, 1)

        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName(u"lblLast")
        self.lblLast.setStyleSheet(u"background-color: blue; color: white;")

        self.gridLayout.addWidget(self.lblLast, 1, 0, 1, 1)

        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName(u"entLast")

        self.gridLayout.addWidget(self.entLast, 1, 1, 1, 1)

        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName(u"lblEmail")

        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1)

        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName(u"entEmail")

        self.gridLayout.addWidget(self.entEmail, 2, 1, 1, 1)

        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName(u"lblPhone")

        self.gridLayout.addWidget(self.lblPhone, 3, 0, 1, 1)

        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName(u"entPhone")

        self.gridLayout.addWidget(self.entPhone, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.lblFrPerson)

        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setFrameShape(QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName(u"btnS")
        self.btnS.setMinimumSize(QSize(80, 0))
        self.btnS.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btnS)

        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName(u"btnR")
        self.btnR.setMinimumSize(QSize(80, 0))
        self.btnR.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btnR)

        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName(u"btnQ")
        self.btnQ.setMinimumSize(QSize(80, 0))
        self.btnQ.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btnQ)


        self.verticalLayout.addWidget(self.fraButtons)

        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("root", u"Personal Information", None))
        self.lblFirst.setText(QCoreApplication.translate("root", u"*First Name:", None))
        self.lblLast.setText(QCoreApplication.translate("root", u"*Last Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("root", u"Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("root", u"Phone:", None))
        self.btnS.setText(QCoreApplication.translate("root", u"Submit", None))
        self.btnR.setText(QCoreApplication.translate("root", u"Reset", None))
        self.btnQ.setText(QCoreApplication.translate("root", u"Quit", None))
    # retranslateUi

