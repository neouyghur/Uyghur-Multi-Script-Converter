from umsc.umsc import UgMultiScriptConverter
import pytest

# Pair each input with its expected output
test_data = [
    ("قول", "qol"),
    ("باش", "baş"),
    ("پۇت", "put"),
    ("كۆز", "köz"),
    ("جەڭچى", "ceñçi"),
    ("جۇدې", "cudé"),
    ("سان", "san"),
    ("سەي", "sey"),
    ("ئې", "é"),
    ("شىر", "şir"),
    ("شاڭخەي", "şañxey"),
    ("كىتاب", "kitab"),
    ("ۋەتەن", "veten"),
    ("تومۇر", "tomur"),
    ("كۆمۈر", "kömür"),
    ("ئېلىكتىر", "éliktir"),
    ("ۋيېتنام", "vyétnam"),
    ("شىنجاڭ", "şincañ"),
    ("ئانار", "anar"),
    ("ئەنجۈر", "encür"),
    ("ئوردا", "orda"),
    ("ئۇرۇش", "uruş"),
    ("ئۆردەك", "ördek"),
    ("ئۈزۈم", "üzüm"),
    ("ئېلان", "élan"),
    ("ئىنكاس", "inkas"),
    ("ئىنىكئانا", "inik'ana"),
    ("ئەسئەت", "es'et"),
    ("رادىئو", "radio"),
    ("مەسئۇل", "mes'ul"),
    ("قارىئۆرۈك", "qariörük"),
    ("نائۈمىد", "naümid"),
    ("ئىتئېيىق", "it'éyiq"),
    ("جەمئىي", "cem'iy"),
    ("نەمەنگان", "nemengan"),
    ("ئۆزخان", "özxan"),
    ("پاسخا", "pasxa"),
    ("بايرىمى", "bayrimi"),
    ("مائارىپ", "maarip"),
    ("مۇئەللىم", "muellim"),
    ("دائىرە", "daire"),
    ("مۇئەييەن", "mueyyen"),
    ("تەبىئىي", "tebiiy"),
    ("پائالىيەت", "paaliyet"),
    ("ئىسھاق", "ishaq"),
    ("ئۆزبېكىستانغا", "özbékistanğa"),
    ("ھىنگان", "hingan"),
    ("چەكلەنگەن", "çeklengen"),
    ("گاڭگىراپ", "gañgirap"),
    ("باشلانغۇچ", "başlanğuç"),
    ("جەمئىيەت", "cem'iyet"),
    # ("جۇڭخۇا", "cuñxua"),
]


@pytest.mark.parametrize("input,expected", test_data)
def test_UAS2CTS(input, expected):
    converter = UgMultiScriptConverter("UAS", "CTS")
    assert converter(input) == expected
