from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('ⱪol', 'qol'),
    ('bax', 'baş'),
    ('put', 'put'),
    ('køz', 'köz'),
    ('jəngqi', 'ceñçi'),
    ('san', 'san'),
    ('səy', 'sey'),
    ('xir', 'şir'),
    ('kitab', 'kitab'),
    ('wətən', 'veten'),
    ('tomur', 'tomur'),
    ('kømür', 'kömür'),
    ('eliktir', 'éliktir'),
    ('xinjang', 'şincañ'),
    ('anar', 'anar'),
    ('ənjür', 'encür'),
    ('orda', 'orda'),
    ('urux', 'uruş'),
    ('ørdək', 'ördek'),
    ('üzüm', 'üzüm'),
    ('elan', 'élan'),
    ('inkas', 'inkas'),
    ("nəmən'gan", "nemen'gan"),
    ('øzhan', 'özxan'),
    ('pasha', 'pasxa'),
    ('bayrimi', 'bayrimi'),
    ("ⱨin'gan", "hin'gan"),
    ("qəklən'gən", "çeklen'gen"),
    ('baxlanƣuq', 'başlanğuç'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UYS2CTS(input, expected):
    converter = UgMultiScriptConverter("UYS", "CTS")
    assert converter(input) == expected
