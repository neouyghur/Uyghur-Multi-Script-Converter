#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Author: neouyghur <osmanjan.t@gmail.com>
# Author: Sitare <https://github.com/saeziae>
# Licence: MIT License

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mainWindow_qt5 import Ui_MainWindow
from converter_py3 import UgScriptConverter


class Main(QMainWindow):
    input_file = ''
    output_file = ''
    isSetFile = False

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnConvert.clicked.connect(self.btnConvert_clicked)
        # self.ui.btnDefault.clicked.connect(self.btnDefault_clicked)
        self.ui.actionInput_File.triggered.connect(self.selectInputFile)
        self.ui.actionOutput_File.triggered.connect(self.setOutputFile)

    def btnConvert_clicked(self):
        if self.isSetFile == False:
            src_txt = self.ui.te_src.toPlainText()
            opt_txt = self.ui.te_opt.toPlainText()
        else:
            msgBox = QMessageBox()
            msgBox.setText(
                "Converting the source file. \nمەنبە ھۇجىتىنى ئايلاندۇرۋاتىمىز.")
            msgBox.exec_()
            inf = open(self.input_file, 'r')
            src_txt = inf.read()
            inf.close()

        from_val = self.ui.cb_src.currentIndex()
        to_val = self.ui.cb_opt.currentIndex()

        usc = UgScriptConverter()

        if from_val == to_val:
            opt_txt = src_txt

        # 0 ULS(Uyghur Latin Script) ULY(Uyghur Latin Yëziqi)
        # 1 UAS(Uyghur Arabic Script) UEY(Uyghur Ereb Yëziqi)
        # 2 CTS(Common Turkic Script) OTA(Ortaq Türkche Alfabet)
        # 3 UCS(Uyghur Cyrillic Script) USY(Uyghur Siril Yëziqi)
        # 4 UNS(Uyghur New Script) UYY(Uyghur Yëngi Yëziqi)
        # 5 TT(Toponymy Transcription) SASM/GNC romanization

        elif from_val == 0:
            if to_val == 1:
                opt_txt = usc.UA2LA(src_txt)
            elif to_val == 2:
                opt_txt = usc.UA2CT(src_txt)
            elif to_val == 3:
                opt_txt = usc.UA2UC(src_txt)
            elif to_val == 4:
                opt_txt = usc.UA2UY(src_txt)
            elif to_val == 5:
                opt_txt = usc.UA2TT(src_txt)
        elif from_val == 1:
            if to_val == 0:
                opt_txt = usc.LA2UA(src_txt)
            elif to_val == 2:
                opt_txt = usc.LA2CT(src_txt)
            elif to_val == 3:
                opt_txt = usc.LA2UC(src_txt)
            elif to_val == 4:
                opt_txt = usc.LA2UY(src_txt)
            elif to_val == 5:
                opt_txt = usc.LA2TT(src_txt)
        elif from_val == 2:
            if to_val == 0:
                opt_txt = usc.CT2UA(src_txt)
            elif to_val == 1:
                opt_txt = usc.CT2LA(src_txt)
            elif to_val == 3:
                opt_txt = usc.CT2UC(src_txt)
            elif to_val == 4:
                opt_txt = usc.CT2UY(src_txt)
            elif to_val == 5:
                opt_txt = usc.CT2TT(src_txt)
        elif from_val == 3:
            if to_val == 0:
                opt_txt = usc.UC2UA(src_txt)
            elif to_val == 1:
                opt_txt = usc.UC2LA(src_txt)
            elif to_val == 2:
                opt_txt = usc.UC2CT(src_txt)
            elif to_val == 4:
                opt_txt = usc.UC2UY(src_txt)
            elif to_val == 5:
                opt_txt = usc.UC2TT(src_txt)
        elif from_val == 4:
            if to_val == 0:
                opt_txt = usc.UY2UA(src_txt)
            elif to_val == 1:
                opt_txt = usc.UY2LA(src_txt)
            elif to_val == 2:
                opt_txt = usc.UY2CT(src_txt)
            elif to_val == 3:
                opt_txt = usc.UY2UC(src_txt)
            elif to_val == 5:
                opt_txt = usc.UY2TT(src_txt)

        if self.isSetFile == False:
            self.ui.te_opt.setText(opt_txt)
        else:
            of = open(self.output_file, 'w', encoding="utf-8")
            of.write(opt_txt)
            of.close()

        isSetFile = False

        print("Converting is done.")

    # This function for testing
    def btnDefault_clicked(self):

        inf = open('default.txt', 'r')
        ug_text = inf.read()
        inf.close()

        from_val = self.ui.cb_src.currentIndex()

        if from_val == 0:
            self.ui.te_src.setText(ug_text)
        elif from_val == 1:
            pass
        elif from_val == 1:
            pass
        elif from_val == 1:
            pass
        elif from_val == 1:
            pass
        else:
            pass

    def selectFile(self):
        tmp_file = (QFileDialog.getOpenFileName())
        return tmp_file[0]

    def selectInputFile(self):
        self.input_file = self.selectFile()
        self.output_file = self.input_file + '_convert.txt'
        print("Input file is selected.")
        print('Input: ', self.input_file)
        print('Output: ', self.output_file)
        self.isSetFile = True

    def setOutputFile(self):
        if self.isSetFile == False:
            msgBox = QMessageBox()
            msgBox.setText(
                "Please choose the source file. \n Menbe hujitini tallang.")
            msgBox.exec_()
            return
        self.output_file = self.selectFile()
        print('Input: ', self.input_file)
        print('Output: ', self.output_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
