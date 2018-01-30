#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

# Original Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License

ULS(Uyghur Latin Script),
UAS(Uyghur Arabic Script),
CTS(Common Turkick Scritp)
UCS(Uyghur Cyrilik Script)


'''
import re
class UgScriptConverter:
    # following may be not necessary , u'“', u'„', u'&#8220;', u'&#8222;', u'”', u'‟', u'&#8221;', u'&#8223;']
    __uas_group1 = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل',
                    u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ', u'ئ',
                    u'؟', u'،', u'؛',
                    u'٭']
    # following may be not necessary, u'«', u'«', u'«', u'«', u'»', u'»', u'»', u'»']
    __cts_group1 = [u'a', u'e', u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ', u'l',
                    u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'ğ', u"'",
                    u'?', u',', u';',
                    u'*']
    __ccs_group1 = [u'а', u'ә', u'б', u'п', u'т', u'җ', u'ч', u'х', u'д', u'р', u'з', u'ж', u'с', u'ш', u'ф', u'ң', u'л',
                    u'ла', u'м', u'һ', u'о', u'у', u'ө', u'ү', u'в', u'е', u'и', u'й', u'қ', u'к', u'г', u'н', u'ғ',u"",
                    u'?', u',', u';',
                    u'*']
    def isPureUyghurScript(herp):
        m = re.search('[\u0621-\u06ff]', herp)
        if m == None:
            return False;
        else:
            return True
    def _repalce_via_table(self,text,tab1,tab2):
        for i, j in zip(tab1, tab2):
            text = text.replace(i, j)
        return text
    def UA2CT(self,text):
        text = self._repalce_via_table(text,self.__uas_group1,self.__cts_group1)
        # is it right?
        text = text.replace("'","")
        return self._repalce_via_table(text,self.__uas_group1,self.__cts_group1)
    def CT2UA(self, text):
        text = self._repalce_via_table(text,self.__cts_group1,self.__uas_group1)
        text = self._revise_UAS(text)
        return text
    def CT2LA(self, text):
        text = text.lower()
        # don't modify the the @ sign
        text = text.replace(u'ng', u"n'g").replace(u'ñ', u"ng").replace(u'ç', u'@h').replace(u'j', u'zh') \
            .replace(u'ş', u'sh').replace(u"ğ", u'gh').replace(u"v", u'w').replace(u"é", u'ë').replace(u"ñ", u'ng') \
            .replace(u"c", u'j').replace(u'@', u'c')
        return text
    def LA2CT(self, text):
        text = text.lower()
        # ch ç # zh j # sh ş # gh ğ
        text = text.replace(u"j", u'c') \
            .replace(u"ng", u'ñ') \
            .replace(u"n'g", u'ng') \
            .replace(u"'ng", u'ñ') \
            .replace(u'ch', u'ç') \
            .replace(u'zh', u'j') \
            .replace(u'sh', u'ş') \
            .replace(u"'gh", u'ğ') \
            .replace(u"gh", u'ğ') \
            .replace(u"w", u'v') \
            .replace(u"ë", u'é') \
            .replace(u'ch', u'ç')
        return text
    def CC2CT(self, text):
        text = text.lower()
        text = self._repalce_via_table(text,self.__ccs_group1,self.__cts_group1)
        #is it right??
        return text.replace("'","")
    def CT2CC(self, text):
        text = text.lower()
        text = self._repalce_via_table(text,self.__cts_group1,self.__ccs_group1)
        return text.replace("'","")
    def _revise_UAS(self,text):
        output = ''
        head = [' ', '-', '\n']
        need_revised = [u'ا', u'ە', u'ې', u'ى', u'و', u'ۇ', u'ۆ', u'ۈ']
        init = text[0]
        if init in need_revised: output += u'ئ'
        for c in text:
            if c in head:
                next = text.find(c) -1
                if next in need_revised:
                    output+=u'ئ'
            output +=c
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

if __name__=="__main__":
    #Test case
    converter = UgScriptConverter()
    ua =  "ئۇيغۇر"
    print("original text: ",ua)
    ct = converter.UA2CT(ua)
    print("UA2CT: ", ct)
    ua = converter.CT2UA(ct)
    print("CT2UA: ", ua)
    la = converter.CT2LA(ct)
    print("CT2LA: ", la)
    ct = converter.LA2CT(la)
    print("LA2CT: ", ct)
    cc = "Уйғур"
    ct = converter.CC2CT(cc)
    print("CC2CT: ", ct)
    cc = converter.CT2CC(ct)
    print("CT2CC: ", cc)