# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(352, 260)
        self.usernameLabel = QLineEdit(Form)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(70, 80, 221, 31))
        font = QFont()
        font.setPointSize(10)
        self.usernameLabel.setFont(font)
        self.passwordLabel = QLineEdit(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(70, 130, 221, 31))
        self.passwordLabel.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 190, 81, 31))
        self.pushButton_2.setFont(font)
        self.alterButton = QPushButton(Form)
        self.alterButton.setObjectName(u"alterButton")
        self.alterButton.setGeometry(QRect(70, 190, 71, 31))
        self.alterButton.setFont(font)
        self.titleLabel = QLabel(Form)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(110, 30, 131, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.titleLabel.setFont(font1)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 190, 81, 31))
        self.pushButton_3.setFont(font)

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.login)
        self.alterButton.clicked.connect(Form.update_password)
        self.passwordLabel.returnPressed.connect(Form.login)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.usernameLabel.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.passwordLabel.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.alterButton.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.titleLabel.setText(QCoreApplication.translate("Form", u"\u672c\u5730\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

