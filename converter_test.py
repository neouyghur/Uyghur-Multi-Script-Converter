#!/usr/bin/env python
# -*- coding: utf-8 -*-

from converter import UgScriptConverter

text =  u'ھەممە ئادەم تۇغۇلۇشىدىنلا ئەركىن، ئىززەت-ھۆرمەت ۋە ھوقۇقتا باب-باراۋەر بولۇپ تۇغۇلغان. ئۇلار ئەقىلگە ۋە ۋىجدانغا ئىگە ھەمدە بىر-بىرىگە قېرىنداشلىق مۇناسىۋىتىگە خاس روھ بىلەن مۇئامىلە قىلىشى كېرەك.'
utt = UgScriptConverter()

out_text1 = utt.U2OTToken(text)
out_text2 = utt.U2OTToken_concise(text)

print out_text1 == out_text2

print out_text1
print out_text2



def test():
    # Test function
    # utt = UgScriptConverter()
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
    utt = UgScriptConverter()
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
    # utt = UgScriptConverter()
    #
    # # print str
    # #print 'len:'
    # #print utt.str_len(text)
    # #utt.whatisthis(text)
    # #utt.whatisthis(text.decode('utf-8'))
    # print utt.str_len(text)
    # print utt.U2OTToken(text)


# # Error control
# if len(sys.argv) != 3:
#     print '[Error]: input error'
#     print '[Info] python converter.py <source file>  <target file>'
#     sys.exit()
#
# infile_dir = sys.argv[1] # Input file directory
# outfile_dir = sys.argv[2] # Output file directory
#
# # File control
# if os.path.exists(infile_dir):
#     infile = codecs.open(infile_dir, 'r',  encoding='utf-8')
# else:
#     print "Error: Cannot find the file.\n"
#     sys.exit(1)
#
# outfile = codecs.open(outfile_dir, 'w');
# text = infile.readline()
# utt = UgScriptConverter()
#
# # Read line by line
# while text:
#     try:
#         outfile.write(utt.U2OTToken(text))
#     except:
#         print '[Error] We have unexpected error at:'
#         print text
#     #ofile.write("\n")
#     text = infile.readline()
#
#
#
# # Closing files
# infile.close()
# outfile.close()
