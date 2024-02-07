# Script Converter for Uyghur Language
This converter converts multiple Uyghur scripts such as **ULS** (Uyghur Latin Script), **UAS** (Uyghur Arabic Script), 
**CTS** (Common Turkish Script), **UCS** (Uyghur Cyrillic Script) and **UYS** (Uyghur Yengi (new) Script).


API and Uzbek are currently developing. The mapping might not be very accurate. Especially for Uzbek,
it is not very clear how to map "ئا" and "ئە" to Uzbek.


## Mapping table
| UAS | CTS | ULS| UCS|UYS| API | Uzbek |
|-----|----| ---- | --- | -- |----|---|
| ا   | a  | a    | а   |a |  /ɑ/ | o |
| ە   | e  | e    | ә   |ə |  /æ/ | a |
| ب   | b  | b    | б   |b |  /b/ | b |
| پ   | p  | p    | п   |p |   /p/ | p | 
| ت   | t  | t    | т   |t | /t/ | t |
| ج   | c  | j    | җ   |j | /d͡ʒ/ |   |
| چ   | ç  | ch   | ч   |q |  /t͡ʃ/ | ch |
| خ   | x  | x    | х   |h | /χ/ | x |
| د   | d  | d    | д   |d |  /d/ | d |
| ر   | r  | r    | р   |r |  /r/ | r |
| ز   | z  | z    | з   |z |  /z/ | z |
| ژ   | j  | zh   | ж   |ⱬ | /ʒ/ |   |
| س   | s  | s    | с   |s |  /s/ | s |
| ش   | ş  | sh   | ш   |x |  /ʃ/ | sh |
| ف   | f  | f    | ф   |f |  /f/ | f |
| ڭ   | ñ  | ng   | ң   |ng | /ŋ/ | ng |
| ل   | l  | l    | л   |l |  /l/ | l |
| م   | m  | m    | м   |m |  /m/ | m |
| ھ   | h  | h    | һ   |ⱨ |  /h/ | h |
| و   | o  | o    | о   |o |  /o/ | o |
| ۇ   | u  | u    | у   |u |   /u/ | u |
| ۆ   | ö  | ö    | ө   |ɵ |  /ø/ | oʻ |
| ۈ   | ü  | ü    | ү   |ü |  /y/ | uʻ |
| ۋ   | v  | w    | в   |w |  /w/ | v |
| ې   | é  | é    | е   |e | /ɛ/ | e |
| ى   | i  | i    | и   |i | /i/ | i |
| ي   | y  | y    | й   |y | /j/ | y |
| ق   | q  | q    | қ   |ⱪ | /q/ | q |
| ك   | k  | k    | к   |k |  /k/ | k |
| گ   | g  | g    | г   |g | /ɡ/| g |
| ن   | n  | n    | н   |n |   /n/ | n |
| غ   | ğ  | gh   | ғ   |ƣ | /ʁ/ | gʻ |
| ئ   |    |      |     | |    |   |
| يا  | ya | ya   | я   |ya |    | ya |
| يۇ  | yu | yu   | ю   |yu |    | yu |

## Sample input and output examples

|UAS|CTS|ULS|UCS| UYS                                                                                                                                                                                                                                                                                                                                                                         |
|-------- | ------ | ---- | -----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
قول باش پۇت كۆز جەڭچى جۇدې سان سەي ئې شىر شاڭخەي كىتاب ۋەتەن تومۇر  كۆمۈر ئېلىكتىر ۋەتەن ۋيېتنام شىنجاڭ ئانار ئەنجۈر ئوردا ئۇرۇش  ئۆردەك ئۈزۈم ئېلان ئىنكاس ئىنىكئانا ئەسئەت رادىئو مەسئۇل قارىئۆرۈك نائۈمىد  ئىتئېيىق جەمئىي نەمەنگان ئۆزخان پاسخا بايرىمى مائارىپ مۇئەللىم دائىرە مۇئەييەن تەبىئىي پائالىيەت ئىسھاق ئۆزبېكىستانغا ھىنگان چەكلەنگەن گاڭگىراپ باشلانغۇچ جەمئىيەت جۇڭخۇا| qol baş put köz ceñçi cudé san sey é şir şañxey kitab veten tomur  kömür éliktir veten vyétnam şincañ anar encür orda uruş  ördek üzüm élan inkas inik'ana es'et radio mes'ul qariörük naümid  it'éyiq cem'iy nemengan özxan pasxa bayrimi maarip muellim daire mueyyen tebiiy paaliyet ishaq özbékistanğa hingan çeklengen gañgirap başlanğuç cem'iyet cuñxua|qol bash put köz jengchi judé san sey é shir shangxey kitab weten tomur kömür éliktir weten wyétnam shinjang anar enjür orda urush ördek üzüm élan inkas inik'ana es'et radi'o mes'ul qari'örük na'ümid it'éyiq jem'iy nemen'gan özxan pasxa bayrimi ma'arip mu'ellim da'ire mu'eyyen tebi'iy pa'aliyet is'haq özbékistan'gha hin'gan cheklen'gen ganggirap bashlan'ghuch jem'iyet jungxua |қол баш пут көз җәңчи җуде сан сәй е шир шаңхәй китаб вәтән томур көмүр еликтир вәтән вйетнам шинҗаң анар әнҗүр орда уруш өрдәк үзүм елан инкас иник'ана әс'әт ради'о мәс'ул қари'өрүк на'үмид ит'ейиқ җәм'ий нәмәнган өзхан пасха байрими ма'арип му'әллим да'ирә му'әййән тәби'ий па'алийәт исһақ өзбекистанға һинган чәкләнгән гаңгирап башланғуч җәм'ийәт җуңхуа|ⱪol bax put køz jəngqi jude san səy e xir xanghəy kitab wətən tomur kømür eliktir wətən wyetnam xinjang anar ənjür orda urux ørdək üzüm elan inkas inik'ana əs'ət radi'o məs'ul ⱪari'ørük na'ümid it'eyiⱪ jəm'iy nəmən'gan øzhan pasha bayrimi ma'arip mu'əllim da'irə mu'əyyən təbi'iy pa'aliyət isⱨaⱪ øzbekistanƣa ⱨin'gan qəklən'gən ganggirap baxlanƣuq jəm'iyət junghua |


### Example

```
from umsc import UgMultiScriptConverter
source_script = 'UAS'
target_script = 'ULS'
converter = UgMultiScriptConverter(source_script, target_script)
text = 'ياخشىمۇسىز!'
text = converter(text)
print(text)
```

## Citation

If you wish to cite this project, please use `cite this repository`. 

## Contributing
Feel free to raise issue and pull request.

## License
Distributed under the Apache 2.0 License. See [`LICENSE`](LICENSE) for more information.
