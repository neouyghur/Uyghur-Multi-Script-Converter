from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('ⱪol', 'qol'),
    ('bax', 'bash'),
    ('put', 'put'),
    ('køz', 'köz'),
    ('jəngqi', 'jengchi'),
    ('san', 'san'),
    ('səy', 'sey'),
    ('xir', 'shir'),
    ('kitab', 'kitab'),
    ('wətən', 'weten'),
    ('tomur', 'tomur'),
    ('kømür', 'kömür'),
    ('eliktir', 'éliktir'),
    ('xinjang', 'shinjang'),
    ('anar', 'anar'),
    ('ənjür', 'enjür'),
    ('orda', 'orda'),
    ('urux', 'urush'),
    ('ørdək', 'ördek'),
    ('üzüm', 'üzüm'),
    ('elan', 'élan'),
    ('inkas', 'inkas'),
    ("nəmən'gan", "nemen'gan"),
    ('øzhan', 'özxan'),
    ('pasha', 'pasxa'),
    ('bayrimi', 'bayrimi'),
    ("ⱨin'gan", "hin'gan"),
    ("qəklən'gən", "cheklen'gen"),
    ('baxlanƣuq', "bashlan'ghuch"),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UYS2ULS(input, expected):
    converter = UgMultiScriptConverter("UYS", "ULS")
    assert converter(input) == expected
