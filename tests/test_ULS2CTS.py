from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'qol'),
    ('bash', 'baş'),
    ('put', 'put'),
    ('köz', 'köz'),
    ('jengchi', 'ceñçi'),
    ('san', 'san'),
    ('sey', 'sey'),
    ('shir', 'şir'),
    ('kitab', 'kitab'),
    ('weten', 'veten'),
    ('tomur', 'tomur'),
    ('kömür', 'kömür'),
    ('éliktir', 'éliktir'),
    ('shinjang', 'şincañ'),
    ('anar', 'anar'),
    ('enjür', 'encür'),
    ('orda', 'orda'),
    ('urush', 'uruş'),
    ('ördek', 'ördek'),
    ('üzüm', 'üzüm'),
    ('élan', 'élan'),
    ('inkas', 'inkas'),
    ("nemen'gan", 'nemengan'),
    ('özxan', 'özxan'),
    ('pasxa', 'pasxa'),
    ('bayrimi', 'bayrimi'),
    ("hin'gan", 'hingan'),
    ("cheklen'gen", 'çeklengen'),
    ("bashlan'ghuch", 'başlanğuç'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_ULS2CTS(input, expected):
    converter = UgMultiScriptConverter("ULS", "CTS")
    assert converter(input) == expected
