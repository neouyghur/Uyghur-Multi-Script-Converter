from umsc.umsc import UgMultiScriptConverter
import pytest

# Pair each input with its expected output
test_data = [
    ("قول", "qol"),
    ("باش", "bash"),
    ("پۇت", "put"),
    ("كۆز", "köz"),
    ("جەڭچى", "jengchi"),
    ("جۇدې", "judé"),
    ("سان", "san"),
    ("سەي", "sey"),
    ("ئې", "é"),
    ("شىر", "shir"),
    ("شاڭخەي", "shangxey"),
    ("كىتاب", "kitab"),
    ("ۋەتەن", "weten"),
    ("تومۇر", "tomur"),
    ("كۆمۈر", "kömür"),
    ("ئېلىكتىر", "éliktir"),
    ("ۋيېتنام", "wyétnam"),
    ("شىنجاڭ", "shinjang"),
    ("ئانار", "anar"),
    ("ئەنجۈر", "enjür"),
    ("ئوردا", "orda"),
    ("ئۇرۇش", "urush"),
    ("ئۆردەك", "ördek"),
    ("ئۈزۈم", "üzüm"),
    ("ئېلان", "élan"),
    ("ئىنكاس", "inkas"),
    ("ئىنىكئانا", "inik'ana"),
    ("ئەسئەت", "es'et"),
    ("رادىئو", "radi'o"),
    ("مەسئۇل", "mes'ul"),
    ("قارىئۆرۈك", "qari'örük"),
    ("نائۈمىد", "na'ümid"),
    ("ئىتئېيىق", "it'éyiq"),
    ("جەمئىي", "jem'iy"),
    ("نەمەنگان", "nemen'gan"),
    ("ئۆزخان", "özxan"),
    ("پاسخا", "pasxa"),
    ("بايرىمى", "bayrimi"),
    ("مائارىپ", "ma'arip"),
    ("مۇئەللىم", "mu'ellim"),
    ("دائىرە", "da'ire"),
    ("مۇئەييەن", "mu'eyyen"),
    ("تەبىئىي", "tebi'iy"),
    ("پائالىيەت", "pa'aliyet"),
    ("ئىسھاق", "is'haq"),
    ("ئۆزبېكىستانغا", "özbékistan'gha"),
    ("ھىنگان", "hin'gan"),
    ("چەكلەنگەن", "cheklen'gen"),
    ("گاڭگىراپ", "ganggirap"),
    ("باشلانغۇچ", "bashlan'ghuch"),
    ("جەمئىيەت", "jem'iyet"),
    ("جۇڭخۇا", "jungxua"),
    ("ئەدەب-ئەخلاق", "edeb-exlaq"),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UAS2CTS(input, expected):
    converter = UgMultiScriptConverter("UAS", "ULS")
    assert converter(input) == expected
