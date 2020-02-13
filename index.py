import sys, os

# Файлы для работы
# import root
from main_widget_ui import *
from about_me_ui import *
from direction_ui import *
import deep_learning as color
# Для работы с библиотекой
from PySide2 import QtWidgets, QtCore, QtGui
from PIL import Image
import webbrowser
import re
import os

path = os.getcwd()

#  Всплывающее меню для вывода основной информации
# class AboutMe(QtWidgets.QDialog):
#     def __init__(self):
#         super(CustomDialog, self).__init__(*args, **kwargs)
#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)
#         self.setWindowTitle("About me")
def save_log(text=None):
    from datetime import datetime
    date = datetime.today()
    filename = "log-%d-%d-%d.txt"  % (date.day, date.month, date.year)
    print(filename)
    with open("./log/" + filename, 'w') as file:
        file.write(text)
        file.close()


class Direction(QtWidgets.QDialog):
    def __init__(self):
        super(Direction, self).__init__()
        self.ui = Direction_Dialog()
        self.ui.setupUi(self)

class AboutMe(QtWidgets.QDialog):
    def __init__(self):
        super(AboutMe, self).__init__()
        self.ui = About_me_Dialog()
        self.ui.setupUi(self)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.fname = None
        self.edit_image = None
        self.ui.setupUi(self)
        # There is save or open file
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpen.setShortcut('Ctrl+O')

        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave.setShortcut('Ctrl+S')

        self.ui.actionSave_as.triggered.connect(self.save_as_file)
        self.ui.actionSave_as.setShortcut('Shift+Ctrl+S')
        self.ui.pushButton_2.clicked.connect(self.save_log)
        #The color mode
        self.ui.actionSepia.triggered.connect(self.translate_to_sepia)
        self.ui.actionNegative.triggered.connect(self.translate_to_negative)
        self.ui.actionBlack_white.triggered.connect(self.translate_to_bw)
        self.ui.actionGray.triggered.connect(self.translate_to_gray)
        self.ui.actionWhite_black.triggered.connect(self.translate_to_wb)
        self.ui.actionNorm.triggered.connect(self.normal_mode)
        # The deep learning
        self.ui.actionFind_Fac.triggered.connect(self.find_face)
        self.ui.actionDetect_text.triggered.connect(self.detect_text)

        self.ui.actionFind_Face.triggered.connect(self.example_face)
        self.ui.actionDetect_text_2.triggered.connect(self.example_text)
        # The menu with help
        self.ui.actionAbout_me.triggered.connect(self.about_me)
        # the direction
        self.ui.action_3.triggered.connect(self.direction)
        # the open url for help
        self.ui.action_4.triggered.connect(self.open_browser)

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.DontUseNativeDialog

        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', path, "*.jpg;;*.png;;*.jpeg;;*.drg", option=options)[0]
        if file != "":
            self.fname = file

        self.ui.lineEdit.setText(self.fname)
        self.ui.label_3.setPixmap(QtGui.QPixmap(self.fname).scaled(261, 361))

    def save_log(self):
        from datetime import datetime
        date = datetime.today()
        filename = "log-%d-%d-%d.txt"  % (date.day, date.month, date.year)
        text = self.ui.lineEdit.toPlainText()
        with open("./log/" + filename, 'w') as file:
            file.write(text)
            file.close()
    def save_file(self):
        if self.fname != None:
            if self.edit_image == None:
                file = Image.open(self.fname)
            else :
                file = Image.open(self.edit_image)
            file.save("./" + sefl.edit_image)

    def save_as_file(self):
        if self.fname != None or self.edit_image != None:
            if self.edit_image == None:
                file = Image.open(self.fname)
            else :
                file = Image.open(self.edit_image)

            getFile = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as file', path, "*.jpg;;*.png;;*.jpeg;;*.drg;; * (other)")
            if getFile[1] == "other":
                name = getFile[0]
            else :
                filename = str(getFile[0]).split(".")
                name = filename[0] + getFile[1]
                name = name.replace("*", "")
            file.save(name, format="jpeg")
        else:
            self.ui.lineEdit.setText("We don't have file")

    def about_me(self):
        aboutme_dialog = AboutMe()
        aboutme_dialog.setModal(True)
        aboutme_dialog.show()
        aboutme_dialog.exec()

    def open_browser(self):
        webbrowser.open_new("https://vk.com/")
        webbrowser.open_new_tab("https://github.com/")

    def direction(self):
        direction__dialog = Direction()
        direction__dialog.setModal(True)
        direction__dialog.show()
        direction__dialog.exec()

    def translate_to_negative(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            PIL_picture = color.ColorMode(self.fname)
            self.edit_image = PIL_picture.negative()
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("\nSuccesfull load")

    def translate_to_bw(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            PIL_picture = color.ColorMode(self.fname)
            self.edit_image = PIL_picture.black_white()
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("\nSuccesfull load")
    def translate_to_wb(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            PIL_picture = color.ColorMode(self.fname)
            self.edit_image = PIL_picture.white_black()
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("\nSuccesfull load")

    def translate_to_gray(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            PIL_picture = color.ColorMode(self.fname)
            self.edit_image = PIL_picture.gray()
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("\nSuccesfull load")

    def translate_to_sepia(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            PIL_picture = color.ColorMode(self.fname)
            self.edit_image = PIL_picture.sepia()
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("Succesfull load")

    def normal_mode(self):
        if self.fname == None:
            self.ui.lineEdit.setText("Error:File not load")
        else:
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.fname).scaled(261, 361))

    def find_face(self):
        if self.fname == None :
            self.ui.lineEdit.setText("Error:File not load")
        else :
            self.edit_image, faces = color.deep_find_face(self.fname)
            self.ui.label_3.setPixmap(QtGui.QPixmap(self.edit_image).scaled(261, 361))
            self.ui.lineEdit.setText("\nFaces: " + faces)

    def detect_text(self):
        if self.fname == None:
            self.ui.lineEdit.setText("Error:File not load")
        else:
            import pytesseract
            text = pytesseract.image_to_string(Image.open(self.fname), lang="eng+rus")
            if text == "":
                self.ui.lineEdit.setText("Text not find")
            else :
                self.ui.lineEdit.setText("" + text)
    def example_face(self):
        self.fname = "./Picture/Ben_face.jpg"
        self.ui.label_3.setPixmap(QtGui.QPixmap(self.fname).scaled(261, 361))

    def example_text(self):
        self.fname = "./Picture/SB_ru.jpg"
        self.ui.label_3.setPixmap(QtGui.QPixmap(self.fname).scaled(261, 361))




if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    application = mywindow()
    application.setWindowTitle("Dragon")
    application.show()

    sys.exit(app.exec_())

# from PyQt5 import QtWidgets, uic
# import sys

# app = QtWidgets.QApplication([])
# win = uic.loadUi("main_widget.ui") # расположение вашего файла .ui

# win.show()
# sys.exit(app.exec())
