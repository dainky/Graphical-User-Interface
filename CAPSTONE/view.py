# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 24, 24, 24)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.inputLabel = QLabel(self.centralwidget)
        self.inputLabel.setObjectName(u"inputLabel")

        self.verticalLayout.addWidget(self.inputLabel)

        self.inputLineEdit = QLineEdit(self.centralwidget)
        self.inputLineEdit.setObjectName(u"inputLineEdit")

        self.verticalLayout.addWidget(self.inputLineEdit)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")

        self.verticalLayout.addWidget(self.convertButton)

        self.resultLabel = QLabel(self.centralwidget)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.resultLabel)

        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLabel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temperature Converter", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature Converter (\u00b0C \u2192 \u00b0F)", None))
        self.titleLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 16px; font-weight: bold;", None))
        self.inputLabel.setText(QCoreApplication.translate("MainWindow", u"Enter temperature in Celsius:", None))
        self.inputLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. 100", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Result will appear here", None))
        self.resultLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 14px; color: #2a6ebb; padding: 8px; border: 1px solid #ccc; border-radius: 4px;", None))
        self.errorLabel.setText("")
        self.errorLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: red;", None))
    # retranslateUi

