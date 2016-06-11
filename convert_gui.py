#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
from mainWindow import Ui_MainWindow
from converter import UgScriptConverter

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btnConvert.clicked.connect(self.btnConvert_clicked)
		self.ui.btnDefault.clicked.connect(self.btnDefault_clicked)

	def btnConvert_clicked(self):
		src_txt =  unicode (self.ui.te_src.toPlainText().toUtf8(), "utf-8")
		opt_txt =  unicode (self.ui.te_opt.toPlainText().toUtf8(), "utf-8")

		from_val =  self.ui.cb_src.currentIndex()
		to_val =  self.ui.cb_opt.currentIndex()

		usc = UgScriptConverter()

		# 0 Uyghur, 1 Latin, 2 Common Turkish
		if from_val == to_val:
			opt_txt = src_txt
		elif from_val == 0: 
			if to_val == 1:
				# Uyghur to Latin
				opt_txt = usc.UA2LT(src_txt)
			elif to_val == 2:
				# Uyghur to Common Turkish
				opt_txt = usc.UA2CT(src_txt)
		elif from_val == 1: 
			if to_val == 0:
				# Latin to Uyghur
				opt_txt = usc.LA2UA(src_txt)
			elif to_val == 2:
				# Latin to Common Turkish
				opt_txt = usc.LA2CT(src_txt)
		elif from_val == 2:
			if to_val == 0:
				# Common Turkish to Uyghur
				opt_txt = usc.CT2UA(src_txt)
			elif to_val == 1:
				# Common Turkish to Latin
				opt_txt = usc.CT2LA(src_txt)

		self.ui.te_opt.setText(opt_txt)
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

	def btnDefault_clicked(self):
		
		ug_text = u"چەتئەل"

		from_val =  self.ui.cb_src.currentIndex()

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
		

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())