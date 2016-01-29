#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import codecs
import re
import os.path
import sys


class UgScriptConverter:

    # Check if input is Uyghur character
    def isU(self, herp):
        m = re.search('[\u0621-\u06ff]', herp, re.UNICODE) # re.UNICODE is important
        if m == None:
            return False;
        else:
            return True

    # Check if input is Uyghur punctuation
    def U2LSBelge(self, herp):
        ret = herp
        if herp == u'؟':
            ret = u'?'
        if herp == u'،':
            ret = u','
        if herp == u'؛':
            ret = u';'
        if herp == u'٭':
            ret = u'*'
        if herp == u'“' or herp == u'„' or herp == u'&#8220;' or herp == u'&#8222;':
            ret = u'«'
        if herp == u'”' or herp == u'‟' or herp == u'&#8221;' or herp == u'&#8223;':
            ret = u'»'
        else:
            ret = herp.encode('utf-8')
        return ret

    # UAS to CTS
    def UAS2CTS_concise(self, text):
        # This group characters have similar properties
        # uas: uyghur arab yeziqi
        # cts: birleshken turk yeziqi
        uas_group1 = [u'ا', u'ە' , u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د' ,u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل', u'لا', u'م', u'ھ' , u'و', u'ۇ',  u'ۆ', u'ۈ', u'ۋ',  u'ې', u'ى', u'ي']
        cts_group1 = [ 'a',  'e',   'b',  'p',  't',  'c',  'ç',  'x' , 'd',  'r',  'z',  'j',  's',  'ş',  'f',  'ñ',  'l',  'la',  'm',  'h',  'o',   'u',   'ö',  'ü',  'v',   'é',  'i',  'y']
        uas_group2 = [u'ق', u'ك']
        cts_group2 = [  'q', 'k']
        map1 = dict(zip(uas_group1, cts_group1))
        map2 = dict(zip(uas_group2, cts_group2))
        aldiN = False
        skip = True
        uly = ''
        pos = 0
        size = self.str_len(text)
        herp = '' #text[pos]
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                uly += herp
            except:
                print 'Unexpected Character, please check the results!'
                print herp
            #print uly
            #print pos
            #print 'text: ' + uly
            herp = text[pos]
            #print herp
            pos += 1
            if herp == u'ئ':
                aldiN = False
                if(skip == True):
                    herp = ''
                else:
                    herp = '’'
                continue
            elif herp in uas_group1:
                # todo: we should add dict map here
                herp = map1[herp]
                aldiN = False
                skip = False
                continue
            elif herp == u'غ':
                if(aldiN == True):
                    herp = '’ğ'
                else:
                    herp = 'ğ'
                aldiN = False # todo: why here is different than 'g'
                continue
            elif herp == u'گ':
                if(aldiN == True):
                    herp = '’g'
                else:
                    herp = 'g'
                skip = False
                aldiN = False
                continue
            elif herp in uas_group2:
                herp = map2[herp]
                skip = False
                continue
            elif herp == u'ن':
                herp = 'n'
                skip = False
                aldiN = True
                continue
            else:
                herp = self.U2LSBelge(herp)
                skip = True
                aldiN = False
                continue
        uly += herp
        return uly

    # UAS to CTS
    def UAS2CTS(self, text):
        aldiN = False
        skip = True
        uly = ''
        pos = 0
        size = self.str_len(text)
        herp = ''#text[pos]
        while (pos < size):
            # To control unexpected non-unicode characters
            try:
                uly += herp
            except:
                print herp
            #print uly
            #print pos
            #print 'text: ' + uly
            herp = text[pos]
            #print herp
            pos += 1
            if herp == u'ئ':
                aldiN = False
                if(skip == True):
                    herp = ''
                else:
                    herp = '’'
                continue
            elif herp ==  u'ا':
                aldiN = False
                skip = False
                herp = 'a'
                continue
            elif herp == u'ە':
                aldiN = False
                skip = False
                herp = 'e'
                continue
            elif herp == u'ب':
                aldiN = False
                skip = False
                herp = 'b'
                continue
            elif herp == u'پ':
                aldiN = False
                skip = False
                herp = 'p'
                continue
            elif herp == u'ت':
                aldiN = False
                skip = False
                herp = 't'
                continue
            elif herp == u'ج':
                aldiN = False
                skip = False
                herp = 'c'
                continue
            elif herp == u'چ':
                aldiN = False
                skip = False
                herp = 'ç'
                continue
            elif herp == u'خ':
                aldiN = False
                skip = False
                herp = 'x'
                continue
            elif herp == u'د':
                aldiN = False
                skip = False
                herp = 'd'
                continue
            elif herp == u'ر':
                aldiN = False
                skip = False
                herp = 'r'
                continue
            elif herp == u'ز':
                aldiN = False
                skip = False
                herp = 'z'
                continue
            elif herp == u'ژ':
                aldiN = False
                skip = False
                herp = 'j'
                continue
            elif herp == u'س':
                aldiN = False
                skip = False
                herp = 's'
                continue
            elif herp == u'ش':
                aldiN = False
                skip = False
                herp = 'ş'
                continue
            elif herp == u'غ':
                skip = False
                if(aldiN == True):
                    herp = '’ğ'
                else:
                    herp = 'ğ'
                aldiN = False
                continue
            elif herp == u'ف':
                herp = 'f'
                skip = False
                aldiN = False
                continue
            elif herp == u'ق':
                herp = 'q'
                skip = False
                continue
            elif herp == u'ك':
                herp = 'k'
                skip = False
                continue
            elif herp == u'گ':
                if(aldiN == True):
                    herp = '’g'
                else:
                    herp = 'g'
                skip = False
                aldiN = False
                continue
            elif herp == u'ڭ':
                herp = 'ñ'
                skip = False
                aldiN = False
                continue
            elif herp == u'ل':
                herp = 'l'
                skip = False
                aldiN = False
                continue
            elif herp == u'لا':
                herp = 'la'
                skip = False
                aldiN = False
                continue
            elif herp == u'م':
                herp = 'm'
                skip = False
                aldiN = False
                continue
            elif herp == u'ن':
                herp = 'n'
                skip = False
                aldiN = True
                continue
            elif herp == u'ھ':
                herp = 'h'
                skip = False
                aldiN = False
                continue
            elif herp == u'و':
                herp = 'o'
                skip = False
                aldiN = False
                continue
            elif herp == u'ۇ':
                herp = 'u'
                skip = False
                aldiN = False
                continue
            elif herp == u'ۆ':
                herp = 'ö'
                skip = False
                aldiN = False
                continue
            elif herp == u'ۈ':
                herp = 'ü'
                skip = False
                aldiN = False
                continue
            elif herp == u'ۋ':
                herp = 'v'
                skip = False
                aldiN = False
                continue
            elif herp == u'ې':
                herp = 'é'
                skip = False
                aldiN = False
                continue
            elif herp == u'ى':
                herp = 'i'
                skip = False
                aldiN = False
                continue
            elif herp == u'ي':
                herp = 'y'
                skip = False
                aldiN = False
                continue
            else:
                skip = True
                herp = self.U2LSBelge(herp)
                aldiN = False
                continue
            print 'I am here'
        uly += herp
        return uly

    def whatisthis(self, s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"