from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('қол', 'ⱪol'),
    ('баш', 'bax'),
    ('пут', 'put'),
    ('көз', 'køz'),
    ('җәңчи', 'jəngqi'),
    ('сан', 'san'),
    ('сәй', 'səy'),
    ('шир', 'xir'),
    ('китаб', 'kitab'),
    ('вәтән', 'wətən'),
    ('томур', 'tomur'),
    ('көмүр', 'kømür'),
    ('еликтир', 'eliktir'),
    ('шинҗаң', 'xinjang'),
    ('анар', 'anar'),
    ('әнҗүр', 'ənjür'),
    ('орда', 'orda'),
    ('уруш', 'urux'),
    ('өрдәк', 'ørdək'),
    ('үзүм', 'üzüm'),
    ('елан', 'elan'),
    ('инкас', 'inkas'),
    ('нәмәнган', "nəmən'gan"),
    ('өзхан', 'øzhan'),
    ('пасха', 'pasha'),
    ('байрими', 'bayrimi'),
    ('һинган', "ⱨin'gan"),
    ('чәкләнгән', "qəklən'gən"),
    ('башланғуч', 'baxlanƣuq'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UCS2UYS(input, expected):
    converter = UgMultiScriptConverter("UCS", "UYS")
    assert converter(input) == expected
