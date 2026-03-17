from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'ⱪol'),
    ('bash', 'bax'),
    ('put', 'put'),
    ('köz', 'køz'),
    ('jengchi', 'jəngqi'),
    ('san', 'san'),
    ('sey', 'səy'),
    ('shir', 'xir'),
    ('kitab', 'kitab'),
    ('weten', 'wətən'),
    ('tomur', 'tomur'),
    ('kömür', 'kømür'),
    ('éliktir', 'eliktir'),
    ('shinjang', 'xinjang'),
    ('anar', 'anar'),
    ('enjür', 'ənjür'),
    ('orda', 'orda'),
    ('urush', 'urux'),
    ('ördek', 'ørdək'),
    ('üzüm', 'üzüm'),
    ('élan', 'elan'),
    ('inkas', 'inkas'),
    ("nemen'gan", "nəmən'gan"),
    ('özxan', 'øzhan'),
    ('pasxa', 'pasha'),
    ('bayrimi', 'bayrimi'),
    ("hin'gan", "ⱨin'gan"),
    ("cheklen'gen", "qəklən'gən"),
    ("bashlan'ghuch", 'baxlanƣuq'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_ULS2UYS(input, expected):
    converter = UgMultiScriptConverter("ULS", "UYS")
    assert converter(input) == expected
