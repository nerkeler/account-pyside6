# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QTextEdit, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 262)
        self.keyEdit = QTextEdit(Form)
        self.keyEdit.setObjectName(u"keyEdit")
        self.keyEdit.setGeometry(QRect(40, 70, 271, 121))
        font = QFont()
        font.setPointSize(10)
        self.keyEdit.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 271, 31))
        self.label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 210, 81, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 210, 81, 31))
        self.pushButton_2.setFont(font)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.confirm)
        self.pushButton_2.clicked.connect(Form.copy)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.keyEdit.setPlaceholderText(QCoreApplication.translate("Form",
                                                                   u"\u8fd9\u662f\u60a8\u7684\u5bc6\u94a5\uff0c\u8bf7\u59a5\u5584\u4fdd\u7ba1\uff01",
                                                                   None))
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"\u8bf7\u59a5\u5584\u4fdd\u7ba1\u597d\u60a8\u7684\u5bc6\u94a5\uff0c\u5207\u52ff\u544a\u77e5\u4ed6\u4eba\uff01",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
    # retranslateUi
