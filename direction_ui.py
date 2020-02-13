# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'direction.ui'
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

class Direction_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(656, 410)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 151, 51))
        self.label.setMinimumSize(QSize(151, 51))
        self.label.setMaximumSize(QSize(151, 51))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 110, 651, 301))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042d\u0442\u043e \u043a\u0440\u0430\u0442\u043a\u0438\u0439 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 Dragon. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 Dragon \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u043b\u0430\u0441\u044c \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u0448\u043a\u043e\u043b\u044c\u043d\u043e\u0433\u043e"
                        " \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0438 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u043e\u043a\u0430\u0437\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u043c\u0430\u0448\u0438\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0438 \u0440\u0430\u0431\u043e\u0442\u0435 \u0441 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f\u043c\u0438. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">\u0412\u0435\u0440\u0441\u0438\u044f 0.1</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p"
                        ">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. \u0420\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0432 \u0446\u0432\u0435\u0442\u043e\u0432\u043e\u0439 \u0440\u0435\u0436\u0438\u043c \u0421\u0435\u043f\u0438\u0430, \u041d\u0435\u0433\u0430\u0442\u0438\u0432, \u0421\u0435\u0440\u044b\u0439, \u0427\u0435\u0440\u043d\u043e-\u0411\u0435\u043b\u044b\u0439, \u0411\u0435\u043b\u043e-\u0427\u0435\u0440\u043d\u044b\u0439.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d"
                        "\u0435\u043d\u0438\u044f \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. \u0420\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043b\u0438\u0446\u0430 \u043d\u0430 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438, \u0435\u0441\u043b\u0438 \u0442\u0430\u043a\u043e\u0432\u043e \u0438\u043c\u0435\u0435\u0442\u0441\u044f \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 opencv.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. \u0420\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d"
                        "\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 tesseract</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0431\u044b\u043b\u0430 \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0430 \u043d\u0430 python 3</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043b\u0438\u0441\u044c \u0441\u043b"
                        "\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438: PIL, opencv, pytesseract, pyside2, QT5, numpy</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a: \u0414\u0435\u043d\u0438\u0441 \u041c\u0443\u0441\u0442\u0430\u0444\u0438\u043d</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b"
                        " \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430 github: https://github.com/DenisCompany</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441\u043e \u043c\u043d\u043e\u0439 \u043c\u043e\u0436\u043d\u043e \u0447\u0435\u0440\u0435\u0437 \u043c\u0435\u043d\u044e Help-&gt;asks</p></body></html>", None))
    # retranslateUi
        self.textEdit.setReadOnly(True)
