# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_me.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

width, height = 515, 245
class About_me_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(width, height)
        Dialog.setMaximumSize(QSize(width, height))
        Dialog.setMinimumSize(QSize(width, height))
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 491, 222))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 40px;\n"
"align: 'center';\n"
"text: \"PHO\";")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size: 18px\n"
"")

        self.verticalLayout_2.addWidget(self.label_7)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Dragon", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Build: 0.1\n"
"\n"
"", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"This program was developed in 2020 years as a school project by Denis.", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0431\u044b\u043b\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u0414\u0435\u043d\u0438\u0441\u043e\u043c \n"
"\u0434\u043b\u044f \u0448\u043a\u043e\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0432 2020 \u0433\u043e\u0434\u0443", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\n"
"URL github: https://github.com/DenisCompany", None))
    # retranslateUi


#
# if __name__ == '__main__':
#     import sys
#     app = QApplication([])
#
#     form = form()
#     form.show()
