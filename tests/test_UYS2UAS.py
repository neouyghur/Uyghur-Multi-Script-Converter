from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('ⱪol', 'قول'),
    ('bax', 'باش'),
    ('put', 'پۇت'),
    ('køz', 'كۆز'),
    ('jəngqi', 'جەڭچى'),
    ('san', 'سان'),
    ('səy', 'سەي'),
    ('xir', 'شىر'),
    ('kitab', 'كىتاب'),
    ('wətən', 'ۋەتەن'),
    ('tomur', 'تومۇر'),
    ('kømür', 'كۆمۈر'),
    ('eliktir', 'ئېلىكتىر'),
    ('xinjang', 'شىنجاڭ'),
    ('anar', 'ئانار'),
    ('ənjür', 'ئەنجۈر'),
    ('orda', 'ئوردا'),
    ('urux', 'ئۇرۇش'),
    ('ørdək', 'ئۆردەك'),
    ('üzüm', 'ئۈزۈم'),
    ('elan', 'ئېلان'),
    ('inkas', 'ئىنكاس'),
    ("nəmən'gan", 'نەمەنگان'),
    ('øzhan', 'ئۆزخان'),
    ('pasha', 'پاسخا'),
    ('bayrimi', 'بايرىمى'),
    ("ⱨin'gan", 'ھىنگان'),
    ("qəklən'gən", 'چەكلەنگەن'),
    ('baxlanƣuq', 'باشلانغۇچ'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UYS2UAS(input, expected):
    converter = UgMultiScriptConverter("UYS", "UAS")
    assert converter(input) == expected
