#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

# Original Author: neouyghur
# Mail: osmanjan.t@gmail.com
# Licence: MIT License

This is a simple script to convert Uyghur texts written in different Uyghur scripts. It supports Uyghur Arabic,
Latin Common Turkish scripts, Uyghur Latin Script (also known as computer script), Uyghur Yengi (new) script and Uyghur
Cyrillic script. It is written in Python and uses PyQt5 for GUI. The source script will be converted to common turkic script,
then converted to target script. Therefore, the program is not very efficient but easy to add new scripts.

Abbreviations used in this file:

ULS | Uyghur Latin Script
UYS | Uyghur Yengi (New) Script
CPS | Chinese Pinyin Script
UAS | Uyghur Arabic Script
CTS |Common Turkic Script
UCS | Uyghur Cyrillic Script

'''
import regex as re
import argparse


class UgMultiScriptConverter:
    def __init__(self, source_script, target_script, less_apostrophe=False):
        self.source_script = source_script
        self.target_script = target_script
        self.less_apostrophe = less_apostrophe

        self.__uas_group1 = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ',
                        u'ل', u'لا', u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن',
                        u'غ', u'؟', u'،', u'؛', u'٭']  # u'ئ',
        # following may be not necessary, u'«', u'«', u'«', u'«', u'»', u'»', u'»', u'»']
        self.__cts_group1 = [u'a', u'e', u'b', u'p', u't', u'c', u'ç', u'x', u'd', u'r', u'z', u'j', u's', u'ş', u'f', u'ñ',
                        u'l', u'la', u'm', u'h', u'o', u'u', u'ö', u'ü', u'v', u'é', u'i', u'y', u'q', u'k', u'g', u'n',
                        u'ğ', u'?', u',', u';', u'*']
        self.__ucs_group1 = [u'а', u'ә', u'б', u'п', u'т', u'җ', u'ч', u'х', u'д', u'р', u'з', u'ж', u'с', u'ш', u'ф', u'ң',
                        u'л', u'ла', u'м', u'һ', u'о', u'у', u'ө', u'ү', u'в', u'е', u'и', u'й', u'қ', u'к', u'г', u'н',
                        u'ғ', u'?', u',', u';', u'*']

        # I have to improve this. It is not complete
        # Self.__api_groupd1 = ["ɑ", "æ", "b", "p", "t", "Ǯ", "/t͡ʃ/", "/χ/", "/d/", "/r/", "/z/", "/ʒ/",
        #                       "/s/", "/ʃ/", "/f/", "/ŋ/", "/l/", "/m/", "/h/", "/o/",
        #     "/u/", "/ø/", "/y/", "/w/", "/ɛ/", "/i/", "/j/", "/q/", "/k/", "/ɡ/",
        #     "/n/", "/ʁ/"
        # ]

    def __call__(self, text, source_script=None, target_script=None):
        if source_script:
            self.source_script = source_script.upper()
        else:
            self.source_script = self.source_script.upper()
        if target_script:
            self.target_script = target_script.upper()
        else:
            self.target_script = self.target_script.upper()

        if self.source_script == 'UAS':
            if self.target_script == 'CTS':
                return self.convertUAS2CTS(text)
            elif self.target_script == 'UCS':
                return self.convertUAS2UCS(text)
            elif self.target_script == 'ULS':
                return self.convertUAS2ULS(text)
            elif self.target_script == 'UYS':
                return self.convertUAS2UYS(text)
            elif self.target_script == 'UZBEK':
                return self.convertUAStoUZBEK(text)
            elif self.target_script == self.target_script:
                return text
            else:
                raise ValueError('Target script not supported')

        elif self.source_script == 'ULS':
            if self.target_script == 'CTS':
                return self.convertULS2CTS(text)
            elif self.target_script == 'UCS':
                return self.convertULS2UCS(text)
            elif self.target_script == 'UAS':
                return self.convertULS2UAS(text)
            elif self.target_script == 'UYS':
                return self.convertULS2UYS(text)
            elif self.target_script == self.target_script:
                return text
            else:
                raise ValueError('Target script not supported')

        elif self.source_script == 'CTS':
            if self.target_script == 'UAS':
                return self.convertCTS2UAS(text)
            elif self.target_script == 'UCS':
                return self.convertCTS2UCS(text)
            elif self.target_script == 'ULS':
                return self.convertCTS2ULS(text)
            elif self.target_script == 'UYS':
                return self.convertCTS2UYS(text)
            elif self.target_script == self.target_script:
                return text
            else:
                raise ValueError('Target script not supported')

        elif self.source_script == 'UCS':
            if self.target_script == 'UAS':
                return self.convertUCS2UAS(text)
            elif self.target_script == 'CTS':
                return self.convertUCS2CTS(text)
            elif self.target_script == 'ULS':
                return self.convertUCS2ULS(text)
            elif self.target_script == 'UYS':
                return self.convertUCS2UYS(text)
            elif self.target_script == self.target_script:
                return text
            else:
                raise ValueError('Target script not supported')

        elif self.source_script == 'UYS':
            if self.target_script == 'UAS':
                return self.convertUYS2UAS(text)
            elif self.target_script == 'CTS':
                return self.convertUYS2CTS(text)
            elif self.target_script == 'ULS':
                return self.convertUYS2ULS(text)
            elif self.target_script == 'UCS':
                return self.convertUYS2UCS(text)
            elif self.target_script == self.target_script:
                return text
            else:
                raise ValueError('Target script not supported')
        else:
            raise ValueError('Source script not supported')

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

    # ----------------------------------------------
    # Source script to common turkic script
    def convertUAS2CTS(self, text):
        """
        UAS to CTS
        Parameters
        ----------
        text : str

        Returns
        -------
        text
        """
        text = self._repalce_via_table(text, self.__uas_group1, self.__cts_group1)
        text = self.__revise_CTS(text)
        return text

    def __revise_CTS(self, text):
        """
        revise CTS
        Parameters
        ----------
        text : str

        Returns
            Text
        -------

        """
        # Remove a "U+0626" if it is a beginning of a word
        text = re.sub(r'(\s|^)(\u0626)(\w+)', lambda m: m.group(1) + m.group(3), text)
        # Replace a "U+0626" with "'" if "U+0626" is appeared in a word and its previous character is not in
        # [u'a', u'e', u'é', u'i', u'o', u'u', u'ö', u'ü']
        if self.less_apostrophe:
            text = re.sub(r'(([aeéiouöü])\u0626)', lambda m: m.group()[0], text)
        text = text.replace('\u0626', u"'")
        return text

    def convertULS2CTS(self, text):
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
            .replace(u'ch', u'ç')
        return text

    def convertUYS2CTS(self, text):
        text = text.lower()
        # e:ə c:j ç:q x:h j:ⱬ ş:x ñ:ng ö:ø ü:ü  v:w é:e
        # q:ⱪ ğ:ƣ
        text = text.replace(u"e", u'é') \
            .replace(u"ə", u'e') \
            .replace(u"j", u'c') \
            .replace(u"q", u'ç') \
            .replace(u"ⱬ", u'j') \
            .replace(u"x", u'ş') \
            .replace(u"h", u'x') \
            .replace(u"ⱨ", u'h') \
            .replace(u"ng", u'ñ') \
            .replace(u"ø", u'ö') \
            .replace(u"ü", u'ü') \
            .replace(u"w", u'v') \
            .replace(u"ⱪ", u'q') \
            .replace(u"ƣ", u'ğ')
        return text

    def convertUCS2CTS(self, text):
        text = text.lower()
        text = self._repalce_via_table(text, self.__ucs_group1, self.__cts_group1)
        text = text.replace("я", "ya").replace("ю", "yu")
        return text

    # ----------------------------------------------
    # Common turkic script to target script

    def convertCTS2UAS(self, text):
        """
        CTS to UAS
        Parameters
        ----------
        text : str

        Returns
        -------
          text
        """

        # (?<=[^bptcçxdrzjsşfñllmhvyqkgnğ])[aeéiouöü] (ont type)
        # (?<=[^bptcçxdrzjsşfñllmhvyqkgnğ]|^)[aeéiouöü]

        # Add a "U+0626" before a vowel if it is the beginning of a word or after a vowel
        # for example
        # "ait" -> "U+0626aU+0626it" ئائىت
        # Threre is special case cuñxua which should not be converted to cuñxu'a as it is written in UAS as  جۇڭخۇا
        # We ignore this special case.

        if not self.less_apostrophe:
            text = re.sub(r'(?<=[^aebptcçxdrzjsşfñllamhouöüvéiyqkgnğ]|^)[aeéiouöü]',
                          lambda m: u'\u0626' + m.group(), text)

            def sub(m):
                return m.group(0)[0] + m.group(0)[2]

            text = re.sub(r'[aebptcçxdrzjsşfñllamhouöüvéiyqkgnğ\u0626](\')[aebptcçxdrzjsşfñllamhouöüvéiyqkgnğ\u0626]',
                          sub, text)

            text = self._repalce_via_table(text, self.__cts_group1, self.__uas_group1)
        else:
            text = re.sub(r'(?<=[^bptcçxdrzjsşfñllmhvyqkgnğ]|^)[aeéiouöü]', lambda m: u'\u0626' + m.group(), text)
            # add a "U+0626" before a vowel if it is the beginning of a word or after a vowel but not at the end of the word
            # for example
            # "ait" -> "U+0626aU+0626it" ئائىت
            # cuñxua -> cuñxua. cuñxu'a is wrong جۇڭخۇا
            # text = re.sub(r'(?<=[^bptcçxdrzjsşfñllmhvyqkgnğ]|^)[aeéiouöü](?=[aebptcçxdrzjsşfñllamhouöüvéiyqkgnğ])',
            #               lambda m: u'\u0626' + m.group(), text)
            text = self._repalce_via_table(text, self.__cts_group1, self.__uas_group1)
            # replace "'\u0626" with ""
            text = text.replace(u"'\u0626", '')
            # text = self._revise_UAS(text)
        return text

    def _revise_UAS(self, text):
        return re.sub(r"(^|-|\s|[اەېىوۇۆۈ])([اەېىوۇۆۈ])", lambda m: m.group(1) + "ئ" + m.group(2), text)

    def convertCTS2ULS(self, text):
        text = text.lower()
        text = text.replace(u'ng', u"n'g") \
            .replace(u'sh', u"s'h") \
            .replace(u'ch', u"c'h") \
            .replace(u'zh', u"z'h") \
            .replace(u'gh', u"g'h") \
            .replace(u'ng', u"n'g") \
            .replace(u'nğ', u"n'gh") \
            .replace(u'ñ', u"ng") \
            .replace(u'j', u'zh') \
            .replace(u"c", u'j') \
            .replace(u'ç', u'ch') \
            .replace(u'ş', u'sh') \
            .replace(u"ğ", u"gh") \
            .replace(u"v", u'w')
        return text

    # def convertCTS2UYS(self, text):
    #     text = text.lower()
    #     # don't modify the the @ sign
    #     text = text.replace(u'ng', u"n'g")\
    #         .replace(u'ñ', u"ng")\
    #         .replace(u'ç', u'@h')\
    #         .replace(u'j', u'zh') \
    #         .replace(u'ş', u'sh')\
    #         .replace(u"nğ", u"n'gh")\
    #         .replace(u"ğ", u'gh')\
    #         .replace(u"v", u'w')\
    #         .replace(u"ñ", u'ng') \
    #         .replace(u"c", u'j')\
    #         .replace(u'@', u'c')
    #     return text

    def convertCTS2UYS(self, text):
        text = text.lower()
        text = text.replace(u'ng', u"n'g") \
            .replace(u"e", u'ə') \
            .replace(u'j', u"ⱬ") \
            .replace(u'c', u"j") \
            .replace(u'q', u"ⱪ") \
            .replace(u'ç', u"q") \
            .replace(u'h', u"ⱨ") \
            .replace(u'x', u"h") \
            .replace(u'ş', u"x") \
            .replace(u'ñ', u"ng") \
            .replace(u'ö', u"ø") \
            .replace(u'v', u"w") \
            .replace(u'é', u"e") \
            .replace(u'ğ', u"ƣ")
        return text

    def convertCTS2UZBEK(self, text):
        text = text.lower()
        text = text.replace(u"e", u'a') \
            .replace(u'j', u"j") \
            .replace(u'c', u"j") \
            .replace(u'q', u"q") \
            .replace(u'ç', u"ch") \
            .replace(u'ş', u"sh") \
            .replace(u'ñ', u"ng") \
            .replace(u'ö', u"oʻ") \
            .replace(u'é', u"e") \
            .replace(u'ğ', u"gʻ")
        return text


    def convertCTS2UCS(self, text):
        text = text.lower()
        text = text.replace("ya", "я").replace("yu", "ю")
        text = self._repalce_via_table(text, self.__cts_group1, self.__ucs_group1)
        # return text.replace("'", "")
        return text

    # ----------------------------------------------
    # Uyghur Latin script to target script
    def convertULS2UAS(self, text):
        """
        ULS to UAS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UAS(self.convertULS2CTS(text))

    def convertULS2UCS(self, text):
        """
        ULS to UCS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UCS(self.convertULS2CTS(text))

    def convertULS2UYS(self, text):
        """
        ULS to UCS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UYS(self.convertULS2CTS(text))

    # ----------------------------------------------
    # Uyghur Arabic script to target script

    def convertUAS2ULS(self, text):
        """
        UAS to ULS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2ULS(self.convertUAS2CTS(text))

    def convertUAS2UCS(self, text):
        """
        UAS to CCS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UCS(self.convertUAS2CTS(text))

    def convertUAS2UYS(self, text):
        """
        UAS to UYS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UYS(self.convertUAS2CTS(text))

    # ----------------------------------------------
    # Uyghur Cyrillic script to target script

    def convertUCS2UAS(self, text):
        """
        UCS to UAS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UAS(self.convertUCS2CTS(text))

    def convertUCS2ULS(self, text):
        """
        UCS to ULS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2ULS(self.convertUCS2CTS(text))

    def convertUCS2ULS(self, text):
        """
        UCS to ULS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2ULS(self.convertUCS2CTS(text))

    def convertUCS2UYS(self, text):
        """
        UCS to UYS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UYS(self.convertUCS2CTS(text))

    # ----------------------------------------------
    # Uyghur Yengi script to target script

    def convertUYS2UAS(self, text):
        """
        UYS to UAS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UAS(self.convertUYS2CTS(text))

    def convertUYS2ULS(self, text):
        """
        UYS to ULS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2ULS(self.convertUYS2CTS(text))

    def convertUYS2UCS(self, text):
        """
        UYS to UCS
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UCS(self.convertUYS2CTS(text))

    def convertUAStoUZBEK(self, text):
        """
        UAS to UZBEK
        Parameters
        ----------
        text

        Returns
        -------

        """
        return self.convertCTS2UZBEK(self.convertUAS2CTS(text))


def args_parser():
    parser = argparse.ArgumentParser(description='Convert text from one script to another')
    parser.add_argument('-s', '--source', help='source script', required=True)
    parser.add_argument('-t', '--target', help='target script', required=True)
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)
    parser.add_argument('--la', action='store_true', default=False, help='Removing apostrophe between vowels', required=False)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = args_parser()
    print(args.less_apostrophe)
    with open(args.input, 'r') as f:
        text = f.read()

    converter = UgMultiScriptConverter(args.source, args.target, less_apostrophe=args.apostrophe)
    text = converter(text)
    with open(args.output, 'w') as f:
        f.write(text)

    print("Done")
