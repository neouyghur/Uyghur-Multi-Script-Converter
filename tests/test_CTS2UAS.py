from umsc.umsc import UgMultiScriptConverter
import pytest

# Pair each input with its expected output
test_data = [
    ("qol", "قول"),
    ("baş", "باش"),
    ("put", "پۇت"),
    ("köz", "كۆز"),
    ("ceñçi", "جەڭچى"),
    ("cudé", "جۇدې"),
    ("san", "سان"),
    ("sey", "سەي"),
    ("é", "ئې"),
    ("şir", "شىر"),
    ("şañxey", "شاڭخەي"),
    ("kitab", "كىتاب"),
    ("veten", "ۋەتەن"),
    ("tomur", "تومۇر"),
    ("kömür", "كۆمۈر"),
    ("éliktir", "ئېلىكتىر"),
    ("veten", "ۋەتەن"),
    ("vyétnam", "ۋيېتنام"),
    ("şincañ", "شىنجاڭ"),
    ("anar", "ئانار"),
    ("encür", "ئەنجۈر"),
    ("orda", "ئوردا"),
    ("uruş", "ئۇرۇش"),
    ("ördek", "ئۆردەك"),
    ("üzüm", "ئۈزۈم"),
    ("élan", "ئېلان"),
    ("inkas", "ئىنكاس"),
    ("inik'ana", "ئىنىكئانا"),
    ("es'et", "ئەسئەت"),
    ("radio", "رادىئو"),
    ("mes'ul", "مەسئۇل"),
    ("qariörük", "قارىئۆرۈك"),
    ("naümid", "نائۈمىد"),
    ("it'éyiq", "ئىتئېيىق"),
    ("cem'iy", "جەمئىي"),
    ("nemengan", "نەمەنگان"),
    ("özxan", "ئۆزخان"),
    ("pasxa", "پاسخا"),
    ("bayrimi", "بايرىمى"),
    ("maarip", "مائارىپ"),
    ("muellim", "مۇئەللىم"),
    ("daire", "دائىرە"),
    ("mueyyen", "مۇئەييەن"),
    ("tebiiy", "تەبىئىي"),
    ("paaliyet", "پائالىيەت"),
    ("ishaq", "ئىسھاق"),
    ("özbékistanğa", "ئۆزبېكىستانغا"),
    ("hingan", "ھىنگان"),
    ("çeklengen", "چەكلەنگەن"),
    ("gañgirap", "گاڭگىراپ"),
    ("başlanğuç", "باشلانغۇچ"),
    ("cem'iyet", "جەمئىيەت"),
    # ('cuñxua', 'جۇڭخۇا'),
    # ('cuñxua', 'جۇڭخۇئا'),
]



@pytest.mark.parametrize("input,expected", test_data)
def test_CTS2UAS(input, expected):
    converter = UgMultiScriptConverter("CTS", "UAS")
    assert converter(input) == expected
