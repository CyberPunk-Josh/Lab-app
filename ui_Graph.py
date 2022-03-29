# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GraphmxBBiS.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(805, 569)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 761, 491))
        self.label.setPixmap(QPixmap(u"../../../../../../../Pictures/Saved Pictures/WhatsApp Image 2022-01-01 at 6.45.12 PM (2).jpeg"))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 30, 631, 24))
        font = QFont()
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 761, 491))
        self.label_3.setPixmap(QPixmap(u"../../../../../../Pictures/Saved Pictures/WhatsApp Image 2022-01-01 at 6.45.12 PM (2).jpeg"))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00famero critico de Reynolds para fluidos Pl\u00e1stico de Bingham", None))
        self.label_3.setText("")
    # retranslateUi

