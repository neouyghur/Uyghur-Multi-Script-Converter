#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_MainWindow
from converter import UgScriptConverter

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnConvert.clicked.connect(self.btnConvert_clicked)
        self.ui.btnClear.clicked.connect(self.clearAll)
        # self.ui.btnDefault.clicked.connect(self.btnDefault_clicked)
        self.ui.actionInput_File.triggered.connect(self.selectInputFile)
        self.ui.actionOutput_File.triggered.connect(self.setOutputFile)
        self.ui.actionInfo.triggered.connect(self.showInfo)
        # !!! update the apostrophe part
        self.usc = UgScriptConverter(None, None, True)
        self.input_file = None  # Menbe hujjiti
        self.output_file = None  # Nishah hujjiti
        self.isSetFile = False  # Ensure the input file is selected
        # 0 UAS, 1 CTS, 2 3 ULS 4 UCS 5 UYS
        self.id_to_val = {
            0: 'UAS',
            1: 'CTS',
            2: 'ULS',
            3: 'UCS',
            4: 'UYS'
        }
        self.set_default_source_text()

    def btnConvert_clicked(self):
        if self.isSetFile == False:
            src_txt = self.ui.te_src.toPlainText()
        else:
            # This part should change to status bar
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Converting the source file. \nMenbe hujitini aylandurwatimiz.")
            msgBox.exec_()
            inf = open(self.input_file, 'r')
            src_txt, _ = inf.read(), "utf-8"
            inf.close()

        from_val =  self.ui.cb_src.currentIndex()
        to_val =  self.ui.cb_opt.currentIndex()

        # Convert the text
        opt_txt = self.usc(src_txt, self.id_to_val[from_val], self.id_to_val[to_val])

        if self.isSetFile == False:
            self.ui.te_opt.setText(opt_txt)
        else:
            if self.output_file is None:
                self.output_file = os.path.join(os.path.dirname(self.input_file),
                                            ''.join([os.path.basename(self.input_file).split('.')[0], '_',
                                                    self.usc.source_script, '2', self.usc.target_script])\
                                            + self.input_file.split('.')[1])
            of = open(self.output_file, 'w')
            of.write(opt_txt)
            of.close()
            opt_txt = "Converting is done. \n\nCheck file: " + self.output_file
            self.ui.te_opt.setText(opt_txt)

        self.output_file = None
        print("Converting is done.")

    def set_default_source_text(self):
        text = u"ھەممە ئادەم تۇغۇلۇشىدىنلا ئەركىن، ئىززەت-ھۆرمەت ۋە ھوقۇقتا باب-باراۋەر بولۇپ تۇغۇلغان."+\
        u' ئۇلار ئەقىلگە ۋە ۋىجدانغا ئىگە ھەمدە بىر-بىرىگە قېرىنداشلىق مۇناسىۋىتىگە'+\
        u" خاس روھ بىلەن مۇئامىلە قىلىشى كېرەك."
        self.ui.te_src.setText(text)

    def selectFile(self):
        kwargs = {}
        if 'SNAP' in os.environ:
            kwargs['options'] = QtWidgets.QFileDialog.DontUseNativeDialog
        tmp_file, _ = QtWidgets.QFileDialog.getOpenFileName(filter='Text files (*.txt)',
                                           **kwargs)
        # load file wit QtGui
        return tmp_file

    def selectInputFile(self):
        self.input_file = self.selectFile()
        print("Input file is selected.")
        print('Input: ', self.input_file)
        # print('Output: ', self.output_file)
        opt_txt = "Converting based on file is selected. \n\nThe input file is: " + self.input_file + '\n\nPlease set the ' \
                  'source script and target script. You can also set the output file but it is optional.'
        self.ui.te_src.setText(opt_txt)
        self.isSetFile = True

    def setOutputFile(self):
        if self.isSetFile == False:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Please choose the source file. \nMenbe hujitini tallang.")
            msgBox.exec_()
            return
        # Select output directory
        self.output_file = self.selectFile()
        print('Input: ', self.input_file)
        print('Output: ', self.output_file)

    def clearAll(self):
        """Clear all the text in the text editor."""
        self.ui.te_src.clear()
        self.ui.te_opt.clear()


    def showInfo(self):
        """Pop up the info window."""
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Uyghur Multi-Script Converter \n\nVersion: 0.1.0 \n\nAuthor: Osman Tursun \n\n "
                       "Project page: https://github.com/neouyghur/ScriptConverter4Uyghur")
        msgBox.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())