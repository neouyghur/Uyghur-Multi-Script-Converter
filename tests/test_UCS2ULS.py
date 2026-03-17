from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('қол', 'qol'),
    ('баш', 'bash'),
    ('пут', 'put'),
    ('көз', 'köz'),
    ('җәңчи', 'jengchi'),
    ('сан', 'san'),
    ('сәй', 'sey'),
    ('шир', 'shir'),
    ('китаб', 'kitab'),
    ('вәтән', 'weten'),
    ('томур', 'tomur'),
    ('көмүр', 'kömür'),
    ('еликтир', 'éliktir'),
    ('шинҗаң', 'shinjang'),
    ('анар', 'anar'),
    ('әнҗүр', 'enjür'),
    ('орда', 'orda'),
    ('уруш', 'urush'),
    ('өрдәк', 'ördek'),
    ('үзүм', 'üzüm'),
    ('елан', 'élan'),
    ('инкас', 'inkas'),
    ('нәмәнган', "nemen'gan"),
    ('өзхан', 'özxan'),
    ('пасха', 'pasxa'),
    ('байрими', 'bayrimi'),
    ('һинган', "hin'gan"),
    ('чәкләнгән', "cheklen'gen"),
    ('башланғуч', "bashlan'ghuch"),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UCS2ULS(input, expected):
    converter = UgMultiScriptConverter("UCS", "ULS")
    assert converter(input) == expected
