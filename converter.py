#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License

# kiskartmilar
# uas: uyghur arab yeziqi
# cts: ortaq turk yeziqi

import io
import codecs
import re
import os.path
import sys

class UgScriptConverter:
    # Check if input is Uyghur character
    # Uyghurchimu emesmu
    def isU(self, herp):
        m = re.search('[\u0621-\u06ff]', herp, re.UNICODE) # re.UNICODE is important
        if m == None:
            return False;
        else:
            return True

    # UAS to CTS
    def UA2CT(self, text):
        # This group characters have similar properties
        # uas: uyghur arab yeziqi
        # cts: birleshken turk yeziqi

        uas_group1 = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل',\
         u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ', u'ئ', u'؟', u'،', u'؛',\
         u'٭']
         # following may be not necessary
         #, u'“', u'„', u'&#8220;', u'&#8222;', u'”', u'‟', u'&#8221;', u'&#8223;']

        cts_group1 = [u'a', u'e',  u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ', u"'", u'?', u',', u';',\
         u'*']
         # following may be not necessary
         #, u'«', u'«', u'«', u'«', u'»', u'»', u'»', u'»']

        map1 = dict(zip(uas_group1, cts_group1))
        change = True # For control EMZE, u'ئ'
        output = herp = '' #text[pos]
        pos = 0
        size = len(text)
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                output += herp
            except:
                print 'Unexpected Character, please check the results!'
                print herp
            herp = text[pos]
            #print herp
            pos += 1 # go to next position
            check = herp
            herp = map1.get(herp, herp)
            if herp == u"'":
                if change == True:
                    herp = ""
                change = False

            if check == herp:
                change = True
            else:
                change = False

        output += herp
        return output

    # Todo: change these codes
    def CT2UA(self, text):
        # This group characters have similar properties
        text = text.lower()
        uas_group1 = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل',\
         u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ', u'ئ', u'؟', u'،', u'؛',\
         u'٭']
         #, u'“',  u'”']

        cts_group1 = [u'a', u'e',  u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ', u"'", u'?', u',', u';',\
         u'*']
         #, u'«', u'»']

        map1 = dict(zip(cts_group1, uas_group1))
        output = ''
        pos = 0
        size = len(text)
        herp = '' #text[pos]
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                output += herp
            except:
                print 'Unexpected Character, please check the results!'
                print herp
            herp = text[pos]
            pos += 1
            herp = map1.get(herp, herp)

        output += herp
        output = self.revise_UAS(output)
        return output

    def CT2LA(self, text):
    	text = text.lower()
        text = text.replace(u'ng', u"n'g")
        text = text.replace(u'ñ', u"ng")
        text = text.replace(u'ç', u'@h') # don't modify the the @ sign
        text = text.replace(u'j', u'zh')
        text = text.replace(u'ş', u'sh')
        text = text.replace(u"ğ", u'gh')
        text = text.replace(u"v", u'w')
        text = text.replace(u"é", u'ë')
        text = text.replace(u"ñ", u'ng')
        text = text.replace(u"c", u'j')

        text = text.replace(u'@', u'c')

        return text


    def LA2CT(self, text):
    	text = text.lower()
        # ch ç # zh j # sh ş # gh ğ
        text = text.replace(u"j", u'c')
        text = text.replace(u"ng", u'ñ')
        text = text.replace(u"n'g", u'ng')
        text = text.replace(u"'ng", u'ñ')
        text = text.replace(u'ch', u'ç')
        text = text.replace(u'zh', u'j')
        text = text.replace(u'sh', u'ş')
        text = text.replace(u"'gh", u'ğ')
        text = text.replace(u"gh", u'ğ')
        text = text.replace(u"w", u'v')
        text = text.replace(u"ë", u'é')
        text = text.replace(u'ch', u'ç')

        return text

    def CC2CT(self, text):
    	text = text.lower()

        cts_group1 = [u'a', u'e', u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ']

        ccs_group1 = [u'а', u'ә', u'б', u'п', u'т', u'җ', u'ч', u'х', u'д', u'р', u'з', u'ж', u'с', u'ш', u'ф', u'ң', u'л',\
         u'ла', u'м', u'һ', u'о', u'у', u'ө', u'ү', u'в', u'е', u'и', u'й', u'қ', u'к', u'г', u'н', u'ғ']
        
        for i, j in zip(cts_group1, ccs_group1):
            text = text.replace(j, i)

        return text

    def CT2CC(self, text):
    	text = text.lower()
        cts_group1 = [u'a', u'e', u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ']

        ccs_group1 = [u'а', u'ә', u'б', u'п', u'т', u'җ', u'ч', u'х', u'д', u'р', u'з', u'ж', u'с', u'ш', u'ф', u'ң', u'л',\
         u'ла', u'м', u'һ', u'о', u'у', u'ө', u'ү', u'в', u'е', u'и', u'й', u'қ', u'к', u'г', u'н', u'ғ']

        for i, j in zip(cts_group1, ccs_group1):
            text = text.replace(i, j)

        return text

    def revise_UAS(self, text):
        output = ''
        group1 = [' ', '-', '\n']
        group2 = [u'ا', u'ە', u'ې', u'ى', u'و', u'ۇ', u'ۆ', u'ۈ']
        flag = 1 
        for ichar in text:
            if ichar in group1:
                flag = 1
                output += ichar
            elif ichar in group2:
                if flag:
                    output += u'ئ'
                output += ichar
                flag = 0
            else:
                output += ichar
                flag = 0
        return output


    def LA2UA(self, text):
        return self.CT2UA(self.LA2CT(text))

    def UA2LA(self, text):
        return self.CT2LA(self.UA2CT(text))

    def UA2CC(self, text):
        return self.CT2CC(self.UA2CT(text))

    def CC2UA(self, text):
        return self.CT2UA(self.CC2CT(text))

    def LA2CC(self, text):
        return self.CT2CC(self.LA2CT(text))

    def CC2LA(self, text):
        return self.CT2LA(self.CC2CT(text))

    def whatisthis(self, s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"