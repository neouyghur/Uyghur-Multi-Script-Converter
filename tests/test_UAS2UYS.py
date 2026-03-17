from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('قول', 'ⱪol'),
    ('باش', 'bax'),
    ('پۇت', 'put'),
    ('كۆز', 'køz'),
    ('جەڭچى', 'jəngqi'),
    ('سان', 'san'),
    ('سەي', 'səy'),
    ('شىر', 'xir'),
    ('كىتاب', 'kitab'),
    ('ۋەتەن', 'wətən'),
    ('تومۇر', 'tomur'),
    ('كۆمۈر', 'kømür'),
    ('ئېلىكتىر', 'eliktir'),
    ('شىنجاڭ', 'xinjang'),
    ('ئانار', 'anar'),
    ('ئەنجۈر', 'ənjür'),
    ('ئوردا', 'orda'),
    ('ئۇرۇش', 'urux'),
    ('ئۆردەك', 'ørdək'),
    ('ئۈزۈم', 'üzüm'),
    ('ئېلان', 'elan'),
    ('ئىنكاس', 'inkas'),
    ('نەمەنگان', "nəmən'gan"),
    ('ئۆزخان', 'øzhan'),
    ('پاسخا', 'pasha'),
    ('بايرىمى', 'bayrimi'),
    ('ھىنگان', "ⱨin'gan"),
    ('چەكلەنگەن', "qəklən'gən"),
    ('باشلانغۇچ', 'baxlanƣuq'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UAS2UYS(input, expected):
    converter = UgMultiScriptConverter("UAS", "UYS")
    assert converter(input) == expected
