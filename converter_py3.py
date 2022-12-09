#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

# Original Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License
# Contributor: Setare <https://github.com/saeziae>

ULS(Uyghur Latin Script) ULY(Uyghur Latin Yëziqi)
UAS(Uyghur Arabic Script) UEY(Uyghur Ereb Yëziqi)
CTS(Common Turkic Script) OTA(Ortaq Türkche Alfabet)
UCS(Uyghur Cyrillic Script) USY(Uyghur Siril Yëziqi)
UNS(Uyghur New Script) UYY(Uyghur Yëngi Yëziqi)
TT(Toponymy Transcription) SASM/GNC romanization

'''
import re


class UgScriptConverter:
    # following may be not necessary , '“', '„', '&#8220;', '&#8222;', '”', '‟', '&#8221;', '&#8223;']
    __uas_group1 = ['ا', 'ە', 'ب', 'پ', 'ت', 'ج', 'چ', 'خ', 'د', 'ر', 'ز', 'ژ', 'س', 'ش', 'ف', 'ڭ', 'ل',
                    'م', 'ھ', 'و', 'ۇ', 'ۆ', 'ۈ', 'ۋ', 'ې', 'ى', 'ي', 'ق', 'ك', 'گ', 'ن', 'غ', 'ئ',
                    '؟', '،', '؛', '٭', '۔']
    # following may be not necessary, '«', '«', '«', '«', '»', '»', '»', '»']
    __cts_group1 = ['a', 'e', 'b', 'p', 't', 'c', 'ç', 'x', 'd', 'r', 'z', 'j', 's', 'ş', 'f', 'ñ', 'l',
                    'm', 'h', 'o', 'u', 'ö', 'ü', 'v', 'é', 'i', 'y', 'q', 'k', 'g', 'n', 'ğ', "'",
                    '?', ',', ';', '*', '-']
    __ucs_group1 = ['а', 'ә', 'б', 'п', 'т', 'җ', 'ч', 'х', 'д', 'р', 'з', 'ж', 'с', 'ш', 'ф', 'ң', 'л',
                    'м', 'һ', 'о', 'у', 'ө', 'ү', 'в', 'е', 'и', 'й', 'қ', 'к', 'г', 'н', 'ғ', "'",
                    '?', ',', ';', '*', '-']

    def isPureUyghurScript(herp):
        m = re.search('[\u0621-\u06ff]', herp)
        if m == None:
            return False
        else:
            return True

    def _repalce_via_table(self, text, tab1, tab2):
        for i, j in zip(tab1, tab2):
            text = text.replace(i, j)
        return text

    def UA2CT(self, text):
        text = self._repalce_via_table(
            text, self.__uas_group1, self.__cts_group1)
        text = re.sub(r"(^|[aeiouöüëé ])'([aeiouöüëé])",
                      lambda m:  m.group(1) + m.group(2), text)
        return self._repalce_via_table(text, self.__uas_group1, self.__cts_group1)

    def CT2UA(self, text):
        text = self._repalce_via_table(
            text, self.__cts_group1, self.__uas_group1)
        text = self._revise_UAS(text)
        return text

    # Uyghur Latin Yëziqi
    def CT2LA(self, text):
        text = text.lower()
        text = text.replace('ng', "n'g")\
            .replace('ñ', 'ng')\
            .replace('j', 'zh')\
            .replace('c', 'j')\
            .replace('ç', 'ch') \
            .replace('ş', 'sh')\
            .replace('ğ', 'gh')\
            .replace('v', 'w')\
            .replace('é', 'ë')
        return text

    def LA2CT(self, text):
        text = text.lower()
        text = text.replace('ng', 'ñ') \
            .replace("n'g", 'ng') \
            .replace('gh', 'ğ') \
            .replace('ch', 'ç') \
            .replace('j', 'c') \
            .replace('zh', 'j') \
            .replace('sh', 'ş') \
            .replace('w', 'v') \
            .replace('ë', 'é')
        return text

    # Uyghur Yëngi Yëziqi
    def CT2UY(self, text):
        text = text.lower()
        text = text.replace('ng', "n'g")\
            .replace('ñ', 'ng')\
            .replace('e', 'ə')\
            .replace('ö', 'ɵ')\
            .replace('é', 'e')\
            .replace('j', 'ⱬ')\
            .replace('q', 'ⱪ')\
            .replace('h', 'ⱨ')\
            .replace('x', 'h')\
            .replace('c', 'j')\
            .replace('ç', 'q') \
            .replace('ş', 'x')\
            .replace('ğ', 'ƣ')
        return text

    def UY2CT(self, text):
        text = text.lower()
        text = text.replace('ng', 'ñ')\
            .replace("n'g", 'ng')\
            .replace('e', 'é')\
            .replace('ə', 'e')\
            .replace('ö', 'ɵ')\
            .replace('j', 'c')\
            .replace('q', 'ç') \
            .replace('x', 'ş')\
            .replace('h', 'x')\
            .replace('ⱨ', 'h')\
            .replace('ⱬ', 'j')\
            .replace('ⱪ', 'q')\
            .replace('ƣ', 'ğ')
        return text

    # Uyghur Siril Yëziqi
    def UC2CT(self, text):
        text = text.lower()
        text = self._repalce_via_table(
            text, self.__ucs_group1, self.__cts_group1)
        return text

    def CT2UC(self, text):
        text = text.lower()
        text = self._repalce_via_table(
            text, self.__cts_group1, self.__ucs_group1)
        return text

    # (SASM/GNC romanization) Single direction only
    def CT2TT(self, text):
        text = text.lower()
        text = text.replace('e', 'a')\
            .replace('é', 'e')\
            .replace('j', 'J')\
            .replace('q', 'k')\
            .replace('x', 'h')\
            .replace('c', 'j')\
            .replace('ç', 'q') \
            .replace('ş', 'x')\
            .replace('ğ', 'g')\
            .replace('ñ', 'ng')
        text = re.sub(r"J([aeiouöü])", lambda m: "y" + m.group(1), text)
        text = text.replace('J', 'j')
        return text

    def _revise_UAS(self, text):
        return re.sub(r"(^|-|\s|[اەېىوۇۆۈ])([اەېىوۇۆۈ])", lambda m: m.group(1) + "ئ" + m.group(2), text)

    def LA2UA(self, text):
        return self.CT2UA(self.LA2CT(text))

    def LA2UC(self, text):
        return self.CT2UC(self.LA2CT(text))

    def LA2UY(self, text):
        return self.CT2UY(self.LA2CT(text))

    def LA2TT(self, text):
        return self.CT2TT(self.LA2CT(text))

    def UA2LA(self, text):
        return self.CT2LA(self.UA2CT(text))

    def UA2UC(self, text):
        return self.CT2UC(self.UA2CT(text))

    def UA2UY(self, text):
        return self.CT2UY(self.UA2CT(text))

    def UA2TT(self, text):
        return self.CT2TT(self.UA2CT(text))

    def UC2LA(self, text):
        return self.CT2LA(self.UC2CT(text))

    def UC2UA(self, text):
        return self.CT2UA(self.UC2CT(text))

    def UC2UY(self, text):
        return self.CT2UY(self.UC2CT(text))

    def UC2TT(self, text):
        return self.CT2TT(self.UC2CT(text))

    def UY2UA(self, text):
        return self.CT2UA(self.UY2CT(text))

    def UY2LA(self, text):
        return self.CT2LA(self.UY2CT(text))

    def UY2UC(self, text):
        return self.CT2UC(self.UY2CT(text))

    def UY2TT(self, text):
        return self.CT2TT(self.UY2CT(text))


if __name__ == "__main__":
    # Test case
    converter = UgScriptConverter()
    ua = "ھەممە ئادەم تۇغۇلۇشىدىنلا ئەركىن، ئىززەت۔ھۆرمەت ۋە ھوقۇقتا باب۔باراۋەر بولۇپ تۇغۇلغان. ئۇلار ئەقىلگە ۋە ۋىجدانغا ئىگە ھەمدە بىر۔بىرىگە قېرىنداشلىق مۇناسىۋىتىگە خاس روھ بىلەن مۇئامىلە قىلىشى كېرەك."
    print("UEY: ", ua)
    ct = converter.UA2CT(ua)
    print("OTA: ", ct)
    la = converter.CT2LA(ct)
    print("ULY: ", la)
    uc = converter.CT2UC(ct)
    print("USY: ", uc)
    uy = converter.CT2UY(ct)
    print("UYY: ", uy)
    tt = converter.CT2TT(ct)
    print("PY : ", tt)
