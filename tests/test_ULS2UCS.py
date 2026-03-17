from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('qol', 'қол'),
    ('bash', 'баш'),
    ('put', 'пут'),
    ('köz', 'көз'),
    ('jengchi', 'җәңчи'),
    ('san', 'сан'),
    ('sey', 'сәй'),
    ('shir', 'шир'),
    ('kitab', 'китаб'),
    ('weten', 'вәтән'),
    ('tomur', 'томур'),
    ('kömür', 'көмүр'),
    ('éliktir', 'еликтир'),
    ('shinjang', 'шинҗаң'),
    ('anar', 'анар'),
    ('enjür', 'әнҗүр'),
    ('orda', 'орда'),
    ('urush', 'уруш'),
    ('ördek', 'өрдәк'),
    ('üzüm', 'үзүм'),
    ('élan', 'елан'),
    ('inkas', 'инкас'),
    ("nemen'gan", 'нәмәнган'),
    ('özxan', 'өзхан'),
    ('pasxa', 'пасха'),
    ('bayrimi', 'байрими'),
    ("hin'gan", 'һинган'),
    ("cheklen'gen", 'чәкләнгән'),
    ("bashlan'ghuch", 'башланғуч'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_ULS2UCS(input, expected):
    converter = UgMultiScriptConverter("ULS", "UCS")
    assert converter(input) == expected
