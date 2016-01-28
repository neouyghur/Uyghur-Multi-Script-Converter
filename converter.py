#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import codecs
import re
import os.path
import sys


class UgTextConverter:

    # Check if input is Uyghur character
    def IsU(self, herp):
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
    def U2OTToken(self, text):
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

    def str_len(self, text):
        #print '!'
        #print text
        #row_l = len(text)
        #print 'size:' + str(row_l)
        #utf8_l = len(text.encode('utf-8'))
        #print utf8_l
        #print '#'
        #return (utf8_l-row_l)/2+row_l
        #return row_l
        #print (text.decode('utf-8'))
        #print 'here'
        return len(text)

    def whatisthis(self, s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"



def test():
    # Test function
    # utt = UgTextConverter()
    # if utt.IsU('ا'):
    #     print 'ok'
    # else:
    #     print 'nok'

    idir = 'large_uyghur_text.txt'
    if os.path.exists(idir):
        ifile = codecs.open(idir, 'r',  encoding='utf-8')
    else:
        print "Error: Cannot find the file.\n"
        sys.exit(1)

    ofile = codecs.open('new.text', 'w');
    # #file = open('uy.text', 'r')
    text = ifile.readline()
    utt = UgTextConverter()
    while text:
        ofile.write(utt.U2OTToken(text))
        #ofile.write("\n")
        text = ifile.readline()
    ifile.close()
    ofile.close()

    # #print type(len(text))
    # #print str(len(text))
    #
    # #text = u"ئوسمان"
    # utt = UgTextConverter()
    #
    # # print str
    # #print 'len:'
    # #print utt.str_len(text)
    # #utt.whatisthis(text)
    # #utt.whatisthis(text.decode('utf-8'))
    # print utt.str_len(text)
    # print utt.U2OTToken(text)


# Error control
if len(sys.argv) != 3:
    print '[Error]: input error'
    print '[Info] python converter.py <source file>  <target file>'
    sys.exit()

infile_dir = sys.argv[1] # Input file directory
outfile_dir = sys.argv[2] # Output file directory

# File control
if os.path.exists(infile_dir):
    infile = codecs.open(infile_dir, 'r',  encoding='utf-8')
else:
    print "Error: Cannot find the file.\n"
    sys.exit(1)

outfile = codecs.open(outfile_dir, 'w');
text = infile.readline()
utt = UgTextConverter()

# Read line by line
while text:
    try:
        outfile.write(utt.U2OTToken(text))
    except:
        print '[Error] We have unexpected error at:'
        print text
    #ofile.write("\n")
    text = infile.readline()



# Closing files
infile.close()
outfile.close()