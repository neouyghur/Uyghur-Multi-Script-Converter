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
         u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ', u'ئ']
        cts_group1 = [u'a', u'e',  u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ', u"'"]
        map1 = dict(zip(uas_group1, cts_group1))
        change = True # For control EMZE, u'ئ'
        uly = herp = '' #text[pos]
        pos = 0
        size = len(text)
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                uly += herp
            except:
                print 'Unexpected Character, please check the results!'
                print herp
            herp = text[pos]
            #print herp
            pos += 1 # go to next position
            if herp in uas_group1:
                # todo: we should add dict map here
                herp = map1[herp]
                if herp == u"'" and change == True:
                    herp = ""
                change = False
            else:
                herp = self.U2LSBelge(herp)
                change = True
        uly += herp
        return uly

    # Todo: change these codes
    def CT2UA(self, text):
        # This group characters have similar properties
        text = text.lower()
        uas_group1 = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل',\
         u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ', u'ئ']
        cts_group1 = [u'a', u'e',  u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',\
         u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ', u"'"]
        map1 = dict(zip(cts_group1, uas_group1))
        uly = ''
        pos = 0
        size = len(text)
        herp = '' #text[pos]
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                uly += herp
            except:
                print 'Unexpected Character, please check the results!'
                print herp
            herp = text[pos]
            pos += 1
            if herp in cts_group1:
                herp = map1[herp]
            else:
                herp = self.LS2UBelge(herp)

        uly += herp
        uly = self.revise_UAS(uly)
        return uly

    def LA2UA(self, text):
        return self.CT2UA(self.LA2CT(text))

    def UA2LA(self, text):
        return self.CT2LA(self.UA2CT(text))


    def CT2LA(self, text):

        text = text.replace(u'ng', u"n'g")
        text = text.replace(u'ñ', u"ng")
        text = text.replace(u'ç', u'@h')
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


    def revise_UAS(self, text):

        text = text.replace(u' ا', u' ئا')
        text = text.replace(u' ە', u' ئە')
        text = text.replace(u' ې', u' ئې')
        text = text.replace(u' ى', u' ئى')
        text = text.replace(u' و', u' ئو')
        text = text.replace(u' ۇ', u' ئۇ')
        text = text.replace(u' ۆ', u' ئۆ')
        text = text.replace(u' ۈ', u' ئۈ')

        return text 


    # Uyghur punctuation to Latin punctuation
    def U2LSBelge(self, herp):
        ret = herp
        if herp == u'؟':
            ret = u'?'
        elif herp == u'،':
            ret = u','
        elif herp == u'؛':
            ret = u';'
        elif herp == u'٭':
            ret = u'*'
        elif herp == u'“' or herp == u'„' or herp == u'&#8220;' or herp == u'&#8222;':
            ret = u'«'
        elif herp == u'”' or herp == u'‟' or herp == u'&#8221;' or herp == u'&#8223;':
            ret = u'»'
        else:
            ret = herp.encode('utf-8')
        return ret

    # Latin punctuation to Uyghur punctuation
    def LS2UBelge(self, herp):
        ret = herp
        if herp == u'?':
            ret = u'؟'
        elif herp == u',':
            ret = u'،'
        elif herp == u';':
            ret = u'؛'
        elif herp == u'*':
            ret = u'٭'
        # if herp == u'“' or herp == u'„' or herp == u'&#8220;' or herp == u'&#8222;':
        #     ret = u'«'
        # if herp == u'”' or herp == u'‟' or herp == u'&#8221;' or herp == u'&#8223;':
        #     ret = u'»'
        elif herp == u'“«':
            ret = u'“'
        elif herp == u'”»':
            ret = u'”'
        else:
            ret = herp.encode('utf-8')
        return ret

    def whatisthis(self, s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"


    # # UAS to CLS (uyghur ereptin uyghur latingha almashturush)
    # def UA2LA(self, text):
    #     # This group characters have similar properties
    #     uas_group1 = [u'ا', u'ە' , u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د' ,u'ر', u'ز', u'ژ', u'س',\
    #     u'ش', u'ف', u'ڭ', u'ل', u'لا', u'م', u'ھ' , u'و', u'ۇ',  u'ۆ', u'ۈ', u'ۋ',  u'ې', u'ى', u'ي']
    #     cts_group1 = [ 'a',  'e',   'b',  'p',  't',  'j', 'ch',  'x' , 'd',  'r',  'z', 'zh',  's',\
    #      'sh',  'f', 'ng',  'l',  'la',  'm',  'h',  'o',   'u',   'ö',  'ü',  'w',   'é',  'i',  'y']
    #     uas_group2 = [u'ق', u'ك']
    #     cts_group2 = [  'q', 'k']
    #     map1 = dict(zip(uas_group1, cts_group1))
    #     map2 = dict(zip(uas_group2, cts_group2))
    #     aldiN = False
    #     skip = True
    #     uly = ''
    #     pos = 0
    #     size = len(text)
    #     herp = '' #text[pos]
    #     while (pos < size):
    #         # To control unexpected non-unicode characters
    #         try:
    #             uly += herp
    #         except:
    #             print 'Unexpected Character, please check the results!'
    #             print herp
    #         herp = text[pos]
    #         pos += 1
    #         if herp == u'ئ':
    #             aldiN = False
    #             if(skip == True):
    #                 herp = ''
    #             else:
    #                 herp = '’'
    #             continue
    #         elif herp in uas_group1:
    #             # todo: we should add dict map here
    #             herp = map1[herp]
    #             aldiN = False
    #             skip = False
    #             continue
    #         elif herp == u'غ':
    #             if(aldiN == True):
    #                 herp = '’gh'
    #             else:
    #                 herp = 'gh'
    #             aldiN = False # todo: why here is different than 'g'
    #             continue
    #         elif herp == u'گ':
    #             if(aldiN == True):
    #                 herp = '’g'
    #             else:
    #                 herp = 'g'
    #             skip = False
    #             aldiN = False
    #             continue
    #         elif herp in uas_group2:
    #             herp = map2[herp]
    #             skip = False
    #             continue
    #         elif herp == u'ن':
    #             herp = 'n'
    #             skip = False
    #             aldiN = True
    #             continue
    #         else:
    #             herp = self.U2LSBelge(herp)
    #             skip = True
    #             aldiN = False
    #             continue
    #     uly += herp
    #     return uly


    # # Todo: change these codes
    # def LA2UA(self, text):
    #     # This group characters have similar properties
    #     text = text.lower()
    #     # uas_group1 = [u'ا', u'ە' , u'ب', u'پ', u'ت', u'ج', u'چ',  u'خ',  u'د', u'ر', u'ز', u'ژ',  u'س', u'ش',\
    #     #  u'ف', u'ڭ', u'ل',  u'لا', u'م', u'ھ' , u'و', u'ۇ',  u'ۆ', u'ۈ', u'ۋ',  u'ې', u'ې', u'ى', u'ي']
    #     # las_group1 = [u'a', u'e',  u'b', u'p', u't', u'j', u'ch', u'x' , u'd', u'r', u'z', u'zh', u's', u'sh',\
    #     #  u'f', u'ng', u'l', u'la', u'm', u'h',  u'o', u'u',  u'ö', u'ü', u'w', u'é',  u'ë', u'i', u'y']
    #     # # This group characters have similar properties
    #     # uas_group2 = [u'ق', u'ك']
    #     # las_group2 = [u'q', u'k']

    #     uas_group1 = [u'ا', u'ە' , u'ب', u'پ', u'ت', u'ج', u'چ',  u'خ',  u'د', u'ر', u'ز', u'ژ',  u'س', u'ش',\
    #      u'ف', u'ڭ', u'ل',  u'لا', u'م', u'ھ' , u'و', u'ۇ',  u'ۆ', u'ۈ', u'ۋ',  u'ې', u'ې', u'ى', u'ي']
    #     las_group1 = [u'a', u'e',  u'b', u'p', u't', u'j', u'ch', u'x' , u'd', u'r', u'z', u'zh', u's', u'sh',\
    #      u'f', u'ng', u'l', u'la', u'm', u'h',  u'o', u'u',  u'ö', u'ü', u'w', u'é',  u'ë', u'i', u'y']
    #     # This group characters have similar properties
    #     uas_group2 = [u'ق', u'ك']
    #     las_group2 = [u'q', u'k']

    #     map1 = dict(zip(las_group1, uas_group1))
    #     map2 = dict(zip(las_group2, uas_group2 ))
    #     aldiN = False
    #     skip = True
    #     uly = ''
    #     pos = 0
    #     size = len(text)
    #     herp = '' #text[pos]
    #     while (pos < size):
    #         # To control unexpected non-unicode characters
    #         try:
    #             uly += herp
    #         except:
    #             print 'Unexpected Character, please check the results!'
    #             print herp
    #         #print uly
    #         #print pos
    #         #print 'text: ' + uly
    #         herp = text[pos]
    #         #print herp
    #         pos += 1
    #         if herp == u'’':
    #             aldiN = False
    #             if(skip == True):
    #                 herp = ''
    #             else:
    #                 herp = u'ئ'
    #             continue
    #         elif herp in las_group1:
    #             # todo: we should add dict map here
    #             herp = map1[herp]
    #             aldiN = False
    #             skip = False
    #             continue
    #         elif herp == u'gh':
    #             if(aldiN == True):
    #                 herp = u'غ'
    #             else:
    #                 herp = u'غ'
    #             aldiN = False # todo: why here is different than 'g'
    #             continue
    #         elif herp == u'g':
    #             if(aldiN == True):
    #                 herp = u'گ'
    #             else:
    #                 herp = u'گ'
    #             skip = False
    #             aldiN = False
    #             continue
    #         elif herp in las_group2:
    #             herp = map2[herp]
    #             skip = False
    #             continue
    #         elif herp == u'n':
    #             herp = u'ن'
    #             skip = False
    #             aldiN = True
    #             continue
    #         else:
    #             herp = self.LS2UBelge(herp)
    #             skip = True
    #             aldiN = False
    #             continue
    #     uly += herp

    #     uly = self.revise_UAS(uly)

    #     return uly