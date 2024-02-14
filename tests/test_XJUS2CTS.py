from umsc.umsc import UgMultiScriptConverter
import pytest

# Pair each input with its expected output
test_data = [
    ("qol", "qol"),
    ("baş", "bax"),
    ("put", "put"),
    ("köz", "kOz"),
    ("ceñçi", "jANci"),
    ("cudé", "jude"),
    ("san", "san"),
    ("sey", "sAy"),
    ("é", "ve"),
    ("şir", "xir"),
    ("şañxey", "xaNHAy"),
    ("kitab", "kitab"),
    ("veten", "wAtAn"),
    ("tomur", "tomur"),
    ("kömür", "kOmUr"),
    ("éliktir", "veliktir"),
    ("vyétnam", "wyetnam"),
    ("şincañ", "xinjaN"),
    ("anar", "vanar"),
    ("encür", "vAnjUr"),
    ("orda", "vorda"),
    ("uruş", "vurux"),
    ("ördek", "vOrdAk"),
    ("üzüm", "vUzUm"),
    ("élan", "velan"),
    ("inkas", "vinkas"),
    ("inik'ana", "vinikvana"),
    ("es'et", "vAsvAt"),
    ("radio", "radivo"),
    ("mes'ul", "mAsvul"),
    ("qariörük", "qarivOrUk"),
    ("naümid", "navUmid"),
    ("it'éyiq", "vitveyiq"),
    ("cem'iy", "jAmviy"),
    ("nemengan", "nAmAngan"),
    ("özxan", "vOzHan"),
    ("pasxa", "pasHa"),
    ("bayrimi", "bayrimi"),
    ("maarip", "mavarip"),
    ("muellim", "muvAllim"),
    ("daire", "davirA"),
    ("mueyyen", "muvAyyAn"),
    ("tebiiy", "tAbiviy"),
    ("paaliyet", "pavaliyAt"),
    ("ishaq", "vishaq"),
    ("özbékistanğa", "vOzbekistanGa"),
    ("hingan", "hingan"),
    ("çeklengen", "cAklAngAn"),
    ("gañgirap", "gaNgirap"),
    ("başlanğuç", "baxlanGuc"),
    ("cem'iyet", "jAmviyAt"),
    # ('cuñxua', 'جۇڭخۇا'),
    # ('cuñxua', 'جۇڭخۇئا'),
]


test_data = [(value, key) for key, value in test_data]
@pytest.mark.parametrize("input,expected", test_data)
def test_CTS2UAS(input, expected):
    converter = UgMultiScriptConverter("XJUS", "CTS")
    assert converter(input) == expected
