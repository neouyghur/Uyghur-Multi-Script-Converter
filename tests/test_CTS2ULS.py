from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'qol'),
    ('baş', 'bash'),
    ('put', 'put'),
    ('köz', 'köz'),
    ('ceñçi', 'jengchi'),
    ('san', 'san'),
    ('sey', 'sey'),
    ('şir', 'shir'),
    ('kitab', 'kitab'),
    ('veten', 'weten'),
    ('tomur', 'tomur'),
    ('kömür', 'kömür'),
    ('éliktir', 'éliktir'),
    ('şincañ', 'shinjang'),
    ('anar', 'anar'),
    ('encür', 'enjür'),
    ('orda', 'orda'),
    ('uruş', 'urush'),
    ('ördek', 'ördek'),
    ('üzüm', 'üzüm'),
    ('élan', 'élan'),
    ('inkas', 'inkas'),
    ('nemengan', "nemen'gan"),
    ('özxan', 'özxan'),
    ('pasxa', 'pasxa'),
    ('bayrimi', 'bayrimi'),
    ('hingan', "hin'gan"),
    ('çeklengen', "cheklen'gen"),
    ('başlanğuç', "bashlan'ghuch"),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_CTS2ULS(input, expected):
    converter = UgMultiScriptConverter("CTS", "ULS")
    assert converter(input) == expected
