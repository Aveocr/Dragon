# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
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

width, height = 531, 589
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(width, height)
        MainWindow.setMaximumSize(QSize(width, height))
        MainWindow.setMinimumSize(QSize(width, height))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color:rgb(9, 21, 36);\n"
"width: 320px;\n"
"heigth :500px\n"
"}\n"
"font {\n"
"color: white\n"
"}\n"
"QLabel {\n"
"font-size: 16px;\n"
"color: #fff;\n"
"}")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSepia = QAction(MainWindow)
        self.actionSepia.setObjectName(u"actionSepia")
        self.actionNegative = QAction(MainWindow)
        self.actionNegative.setObjectName(u"actionNegative")
        self.actionBlack_white = QAction(MainWindow)
        self.actionBlack_white.setObjectName(u"actionBlack_white")
        self.actionGray = QAction(MainWindow)
        self.actionGray.setObjectName(u"actionGray")
        self.actionFind_Fac = QAction(MainWindow)
        self.actionFind_Fac.setObjectName(u"actionFind_Fac")
        self.actionDetect_text = QAction(MainWindow)
        self.actionDetect_text.setObjectName(u"actionDetect_text")
        self.actionFind_Face = QAction(MainWindow)
        self.actionFind_Face.setObjectName(u"actionFind_Face")
        self.actionDetect_text_2 = QAction(MainWindow)
        self.actionDetect_text_2.setObjectName(u"actionDetect_text_2")
        self.actionNorm = QAction(MainWindow)
        self.actionNorm.setObjectName(u"actionNorm")
        self.actionWhite_black = QAction(MainWindow)
        self.actionWhite_black.setObjectName(u"actionWhite_black")
        self.actionAbout_me = QAction(MainWindow)
        self.actionAbout_me.setObjectName(u"actionAbout_me")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 40, 261, 361))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QTextEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 450, 511, 101))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 420, 89, 25))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 420, 89, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 533, 22))
        self.menuColor_mode = QMenu(self.menuBar)
        self.menuColor_mode.setObjectName(u"menuColor_mode")
        self.menuColor_mode_2 = QMenu(self.menuColor_mode)
        self.menuColor_mode_2.setObjectName(u"menuColor_mode_2")
        self.menuDeep_Learning = QMenu(self.menuBar)
        self.menuDeep_Learning.setObjectName(u"menuDeep_Learning")
        self.menuExample = QMenu(self.menuDeep_Learning)
        self.menuExample.setObjectName(u"menuExample")
        self.menuHelp_me = QMenu(self.menuBar)
        self.menuHelp_me.setObjectName(u"menuHelp_me")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuColor_mode.menuAction())
        self.menuBar.addAction(self.menuDeep_Learning.menuAction())
        self.menuBar.addAction(self.menuHelp_me.menuAction())
        self.menuColor_mode.addSeparator()
        self.menuColor_mode.addAction(self.menuColor_mode_2.menuAction())
        self.menuColor_mode.addSeparator()
        self.menuColor_mode.addAction(self.actionNorm)
        self.menuColor_mode.addSeparator()
        self.menuColor_mode_2.addAction(self.actionNegative)
        self.menuColor_mode_2.addAction(self.actionSepia)
        self.menuColor_mode_2.addAction(self.actionWhite_black)
        self.menuColor_mode_2.addAction(self.actionBlack_white)
        self.menuDeep_Learning.addAction(self.actionFind_Fac)
        self.menuDeep_Learning.addAction(self.actionDetect_text)
        self.menuDeep_Learning.addSeparator()
        self.menuDeep_Learning.addAction(self.menuExample.menuAction())
        self.menuExample.addAction(self.actionFind_Face)
        self.menuExample.addAction(self.actionDetect_text_2)
        self.menuHelp_me.addAction(self.actionAbout_me)
        self.menuHelp_me.addAction(self.action_3)
        self.menuHelp_me.addAction(self.action_4)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineEdit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionSepia.setText(QCoreApplication.translate("MainWindow", u"Sepia", None))
        self.actionNegative.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.actionBlack_white.setText(QCoreApplication.translate("MainWindow", u"Black-white", None))
        self.actionGray.setText(QCoreApplication.translate("MainWindow", u"Gray", None))
        self.actionFind_Fac.setText(QCoreApplication.translate("MainWindow", u"Find Face", None))
        self.actionDetect_text.setText(QCoreApplication.translate("MainWindow", u"Detect text", None))
        self.actionFind_Face.setText(QCoreApplication.translate("MainWindow", u"Find Face", None))
        self.actionDetect_text_2.setText(QCoreApplication.translate("MainWindow", u"Detect text", None))
        self.actionNorm.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.actionWhite_black.setText(QCoreApplication.translate("MainWindow", u"White-black", None))
        self.actionAbout_me.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"Asks", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"edit mode", None))
        self.label_3.setText("")
        self.lineEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lineEdit.setReadOnly(True)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuColor_mode.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuColor_mode_2.setTitle(QCoreApplication.translate("MainWindow", u"Color mode", None))
        self.menuDeep_Learning.setTitle(QCoreApplication.translate("MainWindow", u"DL", None))
        self.menuExample.setTitle(QCoreApplication.translate("MainWindow", u"Example", None))
        self.menuHelp_me.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
