from umsc.umsc import UgMultiScriptConverter
import pytest

test_data = [
    ('қол', 'qol'),
    ('баш', 'baş'),
    ('пут', 'put'),
    ('көз', 'köz'),
    ('җәңчи', 'ceñçi'),
    ('сан', 'san'),
    ('сәй', 'sey'),
    ('шир', 'şir'),
    ('китаб', 'kitab'),
    ('вәтән', 'veten'),
    ('томур', 'tomur'),
    ('көмүр', 'kömür'),
    ('еликтир', 'éliktir'),
    ('шинҗаң', 'şincañ'),
    ('анар', 'anar'),
    ('әнҗүр', 'encür'),
    ('орда', 'orda'),
    ('уруш', 'uruş'),
    ('өрдәк', 'ördek'),
    ('үзүм', 'üzüm'),
    ('елан', 'élan'),
    ('инкас', 'inkas'),
    ('нәмәнган', 'nemengan'),
    ('өзхан', 'özxan'),
    ('пасха', 'pasxa'),
    ('байрими', 'bayrimi'),
    ('һинган', 'hingan'),
    ('чәкләнгән', 'çeklengen'),
    ('башланғуч', 'başlanğuç'),
]

@pytest.mark.parametrize("input,expected", test_data)
def test_UCS2CTS(input, expected):
    converter = UgMultiScriptConverter("UCS", "CTS")
    assert converter(input) == expected
