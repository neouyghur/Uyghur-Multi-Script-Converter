#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_MainWindow
from converter import UgScriptConverter

class Main(QtWidgets.QMainWindow):
    input_file = '' # Menbe hujjiti
    output_file = '' # Nishah hujjiti
    isSetFile = False # Ensure the input file is selected

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnConvert.clicked.connect(self.btnConvert_clicked)
        # self.ui.btnDefault.clicked.connect(self.btnDefault_clicked)
        self.ui.actionInput_File.triggered.connect(self.selectInputFile)
        self.ui.actionOutput_File.triggered.connect(self.setOutputFile)

    def btnConvert_clicked(self):
        if self.isSetFile == False:
            # src_txt =  unicode(self.ui.te_src.toPlainText().toUtf8(), "utf-8")
            # opt_txt =  unicode(self.ui.te_opt.toPlainText().toUtf8(), "utf-8")
            src_txt = self.ui.te_src.toPlainText()
            opt_txt = self.ui.te_opt.toPlainText()
        else:
            # This part should change to status bar
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Converting the source file. \n Menbe hujitini aylandurwatimiz.")
            msgBox.exec_()
            inf = open(self.input_file, 'r')
            src_txt, _ = inf.read(), "utf-8"
            inf.close()

        from_val =  self.ui.cb_src.currentIndex()
        to_val =  self.ui.cb_opt.currentIndex()

        # !!! update the apostrophe part
        usc = UgScriptConverter(None, None, True)
        # 0 UAS, 1 CTS, 2 3 ULS 4 UCS 5 UYS
        id_to_val = {
            0: 'UAS',
            1: 'CTS',
            2: 'ULS',
            3: 'UCS',
            4: 'UYS'
        }

        opt_txt = usc(src_txt, id_to_val[from_val], id_to_val[to_val])


        # # 0 Uyghur, 1 Latin, 2 Common Turkish
        # if from_val == to_val:
        #     opt_txt = src_txt
        # # Uyghur Arabic
        # elif from_val == 0:
        #     if to_val == 1:
        #         # Uyghur Arabic to Latin
        #         opt_txt = usc.convertUAS2ULS(src_txt)
        #     elif to_val == 2:
        #         # Uyghur to Common Turkish
        #         opt_txt = usc.convertUAS2CTS(src_txt)
        #     elif to_val == 3:
        #         # Uyghur to Cyrilik Turkish
        #         opt_txt = usc.convertUAS2CCS(src_txt)
        # # Latin
        # elif from_val == 1:
        #     if to_val == 0:
        #         # Latin to Uyghur
        #         opt_txt = usc.convertULS2UAS(src_txt)
        #     elif to_val == 2:
        #         # Latin to Common Turkish
        #         opt_txt = usc.convertULS2CTS(src_txt)
        #     elif to_val == 3:
        #         # Latin to Cyrilik
        #         opt_txt = usc.convertLAS2CCS(src_txt)
        # # Common TUrkish
        # elif from_val == 2:
        #     if to_val == 0:
        #         # Common Turkish to Uyghur
        #         opt_txt = usc.convertCTS2UAS(src_txt)
        #     elif to_val == 1:
        #         # Common Turkish to Latin
        #         opt_txt = usc.convertCTS2LAS(src_txt)
        #     elif to_val == 3:
        #         # Common Turkish to Cyrilik
        #         opt_txt = usc.convertCTS2CCS(src_txt)
        # # Cyrilik
        # elif from_val == 3:
        #     if to_val == 0:
        #         # Common Turkish to Uyghur
        #         opt_txt = usc.convertCCS2UAS(src_txt)
        #     elif to_val == 1:
        #         # Common Turkish to Latin
        #         opt_txt = usc.convertCCS2LAS(src_txt)
        #     elif to_val == 2:
        #         # Common Turkish to Cyrilik
        #         opt_txt = usc.convertCTS2CCS(src_txt)

        if self.isSetFile == False:
            self.ui.te_opt.setText(opt_txt)
        else:
            of = open(self.output_file, 'w')
            of.write(opt_txt)
            of.close()

        isSetFile = False

        print("Converting is done.")
        # print from_val
        # print to_val

        # text = u"ھەممە ئادەم تۇغۇلۇشىدىنلا ئەركىن، ئىززەت-ھۆرمەت ۋە ھوقۇقتا باب-باراۋەر بولۇپ تۇغۇلغان."+\
        # u' ئۇلار ئەقىلگە ۋە ۋىجدانغا ئىگە ھەمدە بىر-بىرىگە قېرىنداشلىق مۇناسىۋىتىگە'+\
        # u" خاس روھ بىلەن مۇئامىلە قىلىشى كېرەك."

        # latin_text = u"Hemme adem tughulushidinla erkin, izzet-hörmet we hoquqta bab-barawer "+\
        # u"bolup tughulghan. Ular eqilge we wijdan'gha ige hemde bir-birige qérindashliq munasiwitige "+\
        # u"xas roh bilen muamile qilishi kérek."

        # ct_text = u"Hemme adem tuğuluşidinla erkin, izzet-hörmet ve hoquqta bab-baraver bolup tuğulğan."+\
        # u" Ular eqilge ve vijdanğa ige hemde bir-birige qérindaşliq munasivitige xas roh bilen mu'amile qilişi kérek. ? <<>>"

        # # latin_text = "adem adem"
        # self.ui.te_src.setText(ct_text)
        # usc = UgScriptConverter()

        # # ug_text = usc.CT2UA(ct_text)
        # # self.ui.textEdit_2.setText(ug_text)

        # # sys.exit()

        # ug_text = usc.LA2UA(latin_text)
        # self.ui.te_opt.setText(ug_text)

        # ct_text= usc.LA2CT(latin_text)
        # self.ui.te_opt.setText(ct_text)

    # # This function for testing
    # def btnDefault_clicked(self):
    #
    #     inf = open('default.txt', 'r')
    #     ug_text = unicode (inf.read(), "utf-8")
    #     inf.close()
    #
    #     from_val =  self.ui.cb_src.currentIndex()
    #
    #     if from_val == 0:
    #         self.ui.te_src.setText(ug_text)
    #     elif from_val == 1:
    #         pass
    #     elif from_val == 1:
    #         pass
    #     elif from_val == 1:
    #         pass
    #     elif from_val == 1:
    #         pass
    #     else:
    #         pass

    def selectFile(self):
        tmp_file, _ = QtWidgets.QFileDialog.getOpenFileName()
        # load file wit QtGui
        return tmp_file

    def selectInputFile(self):
        self.input_file = self.selectFile()
        self.output_file = self.input_file + '_convert.txt'
        print("Input file is selected.")
        print('Input: ', self.input_file)
        print('Output: ', self.output_file)
        self.isSetFile = True

    def setOutputFile(self):
        if self.isSetFile == False:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Please choose the source file. \n Menbe hujitini tallang.")
            msgBox.exec_()
            return
        self.output_file = self.selectFile()
        print('Input: ', self.input_file)
        print('Output: ', self.output_file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())