# Multiple-Uyghur-Script-Converter
This converter converts multiple Uyghur scripts scuh as ULS(Uyghur Latin Script), UAS(Uyghur Arabic Script), CTS(Common Turkish Scritp).   

# Functions:
	UAS to ULS (uyghur arab yeziqidin uyghur latin yeziqigha)
	UAS to UCT (uyghur arab yeziqidin ortaq turk yeziqigha)

# Sample Input Output Examples (Örnek misallar)

Input	| 	Output
-------- | -------- 
قول باش پۇت كۆز | qol baş put köz
جەڭچى جۇدې		|	ceñçi cudé
سان سەي ئې | san sey é
شىر شاڭخەي | şir şañxey
كىتاب ۋەتەن تومۇر  كۆمۈر ئېلىكتىر | kitab veten tomur  kömür éliktir
ۋەتەن ۋيېتنام | veten vyétnam
شىنجاڭ | şincañ
ئانار ئەنجۈر ئوردا ئۇرۇش  ئۆردەك ئۈزۈم ئېلان ئىنكاس | anar encür orda uruş  ördek üzüm élan inkas
ئىنىكئانا ئەسئەت رادىئو مەسئۇل قارىئۆرۈك نائۈمىد  ئىتئېيىق جەمئىي | inik'ana es'et radi'o mes'ul qari'örük na'ümid  it'éyiq cem'iy
نەمەنگان ئۆزخان پاسخا بايرىمى |  nemengan özxan pasxa bayrimi
qol baş put köz ceñçi cudé san sey é şir şañxey kitab veten tomur  kömür éliktir veten vyétnam şincañ anar encür orda uruş  ördek üzüm élan inkas inik'ana es'et radi'o mes'ul qari'örük na'ümid  it'éyiq cem'iy nemengan özxan pasxa bayrimi | قول باش پۇت كۆز جەڭچى جۇدې سان سەي ئې شىر شاڭخەي كىتاب ۋەتەن تومۇر  كۆمۈر ئېلىكتىر ۋەتەن ۋيېتنام شىنجاڭ ئانار ئەنجۈر ئوردا ئۇرۇش  ئۆردەك ئۈزۈم ئېلان ئىنكاس ئىنىكئانا ئەسئەت رادىئو مەسئۇل قارىئۆرۈك نائۈمىد  ئىتئېيىق جەمئىي نەمەنگان ئۆزخان پاسخا بايرىمى

# User interface:

Pyqt is used for user iterface. umsc.ui is graphic file which could be open by clicking on it.
	
	```pyuic4 -x umsc.ui -o umsc.py``` (converting the ui file to python file)
	```python umsc.py``` (run the gui program)
