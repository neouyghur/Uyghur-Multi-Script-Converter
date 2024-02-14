# Script Converter for Uyghur Language
This converter converts multiple Uyghur scripts such as **ULS** (Uyghur Latin Script), **UAS** (Uyghur Arabic Script), 
**CTS** (Common Turkish Script), **UCS** (Uyghur Cyrillic Script), **UYS** (Uyghur Yengi (new) Script), 
International Phonetic Alphabet (IPA), Uzbek and Xinjiang University Script (XJUS).

## Installation
```
pip install umsc
```


## Mapping table
| UAS | CTS | ULS| UCS|UYS| IPA   | Uzbek | XJUS |
|-----|----| ---- | --- | -- |-------|---|------|
| ا   | a  | a    | а   |a | /ɑ/   | o | a    |
| ە   | e  | e    | ә   |ə | /æ/   | a | A    |
| ب   | b  | b    | б   |b | /b/   | b | b    |
| پ   | p  | p    | п   |p | /p/   | p | p    |
| ت   | t  | t    | т   |t | /t/   | t | t    |
| ج   | c  | j    | җ   |j | /d͡ʒ/ |  j | j   |
| چ   | ç  | ch   | ч   |q | /t͡ʃ/ | ch | c   |
| خ   | x  | x    | х   |h | /χ/   | x | H    |
| د   | d  | d    | д   |d | /d/   | d | d    |
| ر   | r  | r    | р   |r | /r/   | r | r    |
| ز   | z  | z    | з   |z | /z/   | z | z    |
| ژ   | j  | zh   | ж   |ⱬ | /ʒ/   |  j | J   |
| س   | s  | s    | с   |s | /s/   | s | s    |
| ش   | ş  | sh   | ш   |x | /ʃ/   | sh | x   |
| ف   | f  | f    | ф   |f | /f/   | f | f    |
| ڭ   | ñ  | ng   | ң   |ng | /ŋ/   | ng | N  |
| ل   | l  | l    | л   |l | /l/   | l | l    |
| م   | m  | m    | м   |m | /m/   | m | m    |
| ھ   | h  | h    | һ   |ⱨ | /h/   | h | h    |
| و   | o  | o    | о   |o | /o/   | oʻ | o    |
| ۇ   | u  | u    | у   |u | /u/   | u | u    |
| ۆ   | ö  | ö    | ө   |ɵ | /ø/   | oʻ | O   |
| ۈ   | ü  | ü    | ү   |ü | /y/   | uʻ | U   |
| ۋ   | v  | w    | в   |w | /w/   | v | w    |
| ې   | é  | é    | е   |e | /ɛ/   | e | e    |
| ى   | i  | i    | и   |i | /i/   | i | i    |
| ي   | y  | y    | й   |y | /j/   | y | y    |
| ق   | q  | q    | қ   |ⱪ | /q/   | q | q    |
| ك   | k  | k    | к   |k | /k/   | k | k    |
| گ   | g  | g    | г   |g | /ɡ/   | g | g    |
| ن   | n  | n    | н   |n | /n/   | n | n    |
| غ   | ğ  | gh   | ғ   |ƣ | /ʁ/   | gʻ | G   |
| ئ   |    |      |     | |       |   | v    |
| يا  | ya | ya   | я   |ya |       | ya | ya   |
| يۇ  | yu | yu   | ю   |yu |       | yu | yu   |

## Sample input and output examples

Review the files in the tests directory for examples of converting between different scripts.

## Usage

```
from umsc import UgMultiScriptConverter
source_script = 'UAS'
target_script = 'ULS'
converter = UgMultiScriptConverter(source_script, target_script)
text = 'ياخشىمۇسىز!'
text = converter(text)
print(text)
```

## Notes
- API and Uzbek are currently developing. The mapping might not be very accurate. Especially for Uzbek, it is not very clear how to map "ئا" and "ئە" to Uzbek.


## Citation

If you wish to cite this project, please use `cite this repository`. 

## Contributing
Feel free to raise issue and pull request.

## License
Distributed under the Apache 2.0 License. See [`LICENSE`](LICENSE) for more information.
