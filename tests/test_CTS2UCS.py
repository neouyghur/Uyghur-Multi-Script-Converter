from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'қол'),
    ('baş', 'баш'),
    ('put', 'пут'),
    ('köz', 'көз'),
    ('ceñçi', 'җәңчи'),
    ('san', 'сан'),
    ('sey', 'сәй'),
    ('şir', 'шир'),
    ('kitab', 'китаб'),
    ('veten', 'вәтән'),
    ('tomur', 'томур'),
    ('kömür', 'көмүр'),
    ('éliktir', 'еликтир'),
    ('şincañ', 'шинҗаң'),
    ('anar', 'анар'),
    ('encür', 'әнҗүр'),
    ('orda', 'орда'),
    ('uruş', 'уруш'),
    ('ördek', 'өрдәк'),
    ('üzüm', 'үзүм'),
    ('élan', 'елан'),
    ('inkas', 'инкас'),
    ('nemengan', 'нәмәнган'),
    ('özxan', 'өзхан'),
    ('pasxa', 'пасха'),
    ('bayrimi', 'байрими'),
    ('hingan', 'һинган'),
    ('çeklengen', 'чәкләнгән'),
    ('başlanğuç', 'башланғуч'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_CTS2UCS(input, expected):
    converter = UgMultiScriptConverter("CTS", "UCS")
    assert converter(input) == expected
