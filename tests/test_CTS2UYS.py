from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'ⱪol'),
    ('baş', 'bax'),
    ('put', 'put'),
    ('köz', 'køz'),
    ('ceñçi', 'jəngqi'),
    ('san', 'san'),
    ('sey', 'səy'),
    ('şir', 'xir'),
    ('kitab', 'kitab'),
    ('veten', 'wətən'),
    ('tomur', 'tomur'),
    ('kömür', 'kømür'),
    ('éliktir', 'eliktir'),
    ('şincañ', 'xinjang'),
    ('anar', 'anar'),
    ('encür', 'ənjür'),
    ('orda', 'orda'),
    ('uruş', 'urux'),
    ('ördek', 'ørdək'),
    ('üzüm', 'üzüm'),
    ('élan', 'elan'),
    ('inkas', 'inkas'),
    ('nemengan', "nəmən'gan"),
    ('özxan', 'øzhan'),
    ('pasxa', 'pasha'),
    ('bayrimi', 'bayrimi'),
    ('hingan', "ⱨin'gan"),
    ('çeklengen', "qəklən'gən"),
    ('başlanğuç', 'baxlanƣuq'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_CTS2UYS(input, expected):
    converter = UgMultiScriptConverter("CTS", "UYS")
    assert converter(input) == expected
