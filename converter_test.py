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
