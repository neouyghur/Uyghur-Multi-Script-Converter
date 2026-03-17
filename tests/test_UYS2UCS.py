from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('ⱪol', 'қол'),
    ('bax', 'баш'),
    ('put', 'пут'),
    ('køz', 'көз'),
    ('jəngqi', 'җәңчи'),
    ('san', 'сан'),
    ('səy', 'сәй'),
    ('xir', 'шир'),
    ('kitab', 'китаб'),
    ('wətən', 'вәтән'),
    ('tomur', 'томур'),
    ('kømür', 'көмүр'),
    ('eliktir', 'еликтир'),
    ('xinjang', 'шинҗаң'),
    ('anar', 'анар'),
    ('ənjür', 'әнҗүр'),
    ('orda', 'орда'),
    ('urux', 'уруш'),
    ('ørdək', 'өрдәк'),
    ('üzüm', 'үзүм'),
    ('elan', 'елан'),
    ('inkas', 'инкас'),
    ("nəmən'gan", "нәмән'ган"),
    ('øzhan', 'өзхан'),
    ('pasha', 'пасха'),
    ('bayrimi', 'байрими'),
    ("ⱨin'gan", "һин'ган"),
    ("qəklən'gən", "чәклән'гән"),
    ('baxlanƣuq', 'башланғуч'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UYS2UCS(input, expected):
    converter = UgMultiScriptConverter("UYS", "UCS")
    assert converter(input) == expected
