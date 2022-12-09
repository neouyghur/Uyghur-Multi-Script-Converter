# Multiple-Uyghur-Script-Converter

Refactored for Python 3 and Qt 5, enjoy it!

`python umsc_qt5.py`

This converter converts multiple Uyghur scripts such as ULS(Uyghur Latin Script), UAS(Uyghur Arabic Script), CTS(Common Turkish Script).

## Scripts

- Uyghur Ereb Yëziqi (UEY) - arabic script
- Uyghur Latin Yëziqi (ULY) - latin script since 2001
- Common Turkic (Ortaq Türkche Alfabet)
- Uyghur Siril Yëziqi (USY) - cyrillic script
- Uyghur Yëngi Yëziqi (UYY) - latin script used between 1965 and 1982
- Toponymy Transcription [SASM/GNC/SRC transcriptions](https://en.wikipedia.org/wiki/SASM/GNC_romanization) - a modification of UYY, currently used in place names

| Arabic(UEY) | Common Turkic | Latin(ULY) | Cyrillic(USY) | UYY | Toponymy Transcription  |
| ----------- | ------------- | ---------- | ------------- | --- | ----------------------- |
| ا           | a             | a          | а             | a   | a                       |
| ە           | e             | e          | ә             | ə   | a                       |
| ب           | b             | b          | б             | b   | b                       |
| پ           | p             | p          | п             | p   | p                       |
| ت           | t             | t          | т             | t   | t                       |
| ج           | c             | j          | җ             | j   | j                       |
| چ           | ç             | ch         | ч             | q   | q                       |
| خ           | x             | x          | х             | h   | h                       |
| د           | d             | d          | д             | d   | d                       |
| ر           | r             | r          | р             | r   | r                       |
| ز           | z             | z          | з             | z   | z                       |
| ژ           | j             | zh         | ж             | ⱬ   | y, j(final of syllable) |
| س           | s             | s          | с             | s   | s                       |
| ش           | ş             | sh         | ш             | x   | x                       |
| ف           | f             | f          | ф             | f   | f                       |
| ڭ           | ñ             | ng         | ң             | ng  | ng                      |
| ل           | l             | l          | л             | l   | l                       |
| م           | m             | m          | м             | m   | m                       |
| ھ           | h             | h          | һ             | h   | h                       |
| و           | o             | o          | о             | o   | o                       |
| ۇ           | u             | u          | у             | u   | u                       |
| ۆ           | ö             | ö          | ө             | ɵ   | ö                       |
| ۈ           | ü             | ü          | ү             | ü   | ü                       |
| ۋ           | v             | w          | в             | w   | w                       |
| ې           | é             | ë, é       | е             | e   | e                       |
| ى           | i             | i          | и             | i   | i                       |
| ي           | y             | y          | й             | y   | y                       |
| ق           | q             | q          | қ             | ⱪ   | k                       |
| ك           | k             | k          | к             | k   | k                       |
| گ           | g             | g          | г             | g   | g                       |
| ن           | n             | n          | н             | n   | n                       |
| غ           | ğ             | gh         | ғ             | ƣ   | g                       |
| ئ           |               |            |               |     |                         |
| يا          | ya            | ya         | я             | ya  | ya                      |
| يۇ          | yu            | yu         | ю             | yu  | yu                      |

## Examples

| Source                                                                                                                                                                                                                      | Converted                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| سايباغ رايونى ئۈرۈمچى شەھىرى گە قاراشلىق شەھەر رايونى بولۇپ                                                                                                                                                                 | (Toponymy Transcription) saybag rayoni ürümqi xahiri ga karaxlik xahar rayoni bolup                                                                                                                         |
| (ULY) Uyghur tili uzaq tarixqa ige güzel tili.                                                                                                                                                                              | ئۇيغۇر تىلى ئۇزاق تارىخقا ئىگە گۈزەل تىلى.                                                                                                                                                                  |
| (Common Turkic) eqilliq kélişim bir xil qanunluq küçke ige bolğan, aldin'ala qoşulğan kélişm yaki toxtamniñ maddiliriğan asasen aptomatik halda icira qilindiğan kompyotér pirogrammisi yaki éliktronluq élim-bérim nizami. | әқиллиқ келишим бир хил қанунлуқ күчкә игә болған, алдин'ала қошулған келишм йаки тохтамниң маддилириған асасән аптоматик һалда иҗира қилиндиған компйотер пирограммиси йаки еликтронлуқ елим-берим низами. |
| ھەممە ئادەم تۇغۇلۇشىدىنلا ئەركىن، ئىززەت۔ھۆرمەت ۋە ھوقۇقتا باب۔باراۋەر بولۇپ تۇغۇلغان.                                                                                                                                      | (UYY) ⱨəmmə adəm tuƣuluxidinla ərkin, izzət-ⱨɵrmət və ⱨoⱪuⱪta bab-baravər bolup tuƣulƣan.                                                                                                                   |

## Files

| name             | info                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------- |
| umsc_qt5.py      | Refactored main program in py3 and qt5 , uses `mainWindow_qt5.py`                           |
| converter_py3.py | Refactored converter in py3                                                                 |
| mainWindow.ui    | pyqt user interface                                                                         |
| converter.py     | functions for converting                                                                    |
| umsc.py          | main function for running the program which includes mainWindow.py and converter.py         |
| materials        | official materials for uyghur script converter                                              |
| php_code         | this python code is improved version of the php code which is written by Mr. Gheyret Kenji. |
