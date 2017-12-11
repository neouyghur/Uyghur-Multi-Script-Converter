# Multiple-Uyghur-Script-Converter
This converter converts multiple Uyghur scripts such as ULS(Uyghur Latin Script), UAS(Uyghur Arabic Script), CTS(Common Turkish Script).   

# Functions
	UAS to ULS (uyghur arab yeziqidin uyghur latin yeziqigha)
	UAS to UCT (uyghur arab yeziqidin ortaq turk yeziqigha)

# Sample input output examples (örnek misallar CMT)

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
مائارىپ مۇئەللىم دائىرە مۇئەييەن تەبىئىي پائالىيەت ئىسھاق ئۆزبېكىستانغا ھىنگان چەكلەنگەن گاڭگىراپ باشلانغۇچ جەمئىيەت| ma'arip mu'ellim da'ire mu'eyyen tebi'iy pa'aliyet ishaq özbékistanğa hingan çeklengen gañgirap başlanğuç cem'iyet
قول باش پۇت كۆز جەڭچى جۇدې سان سەي ئې شىر شاڭخەي كىتاب ۋەتەن تومۇر  كۆمۈر ئېلىكتىر ۋەتەن ۋيېتنام شىنجاڭ ئانار ئەنجۈر ئوردا ئۇرۇش  ئۆردەك ئۈزۈم ئېلان ئىنكاس ئىنىكئانا ئەسئەت رادىئو مەسئۇل قارىئۆرۈك نائۈمىد  ئىتئېيىق جەمئىي نەمەنگان ئۆزخان پاسخا بايرىمى مائارىپ مۇئەللىم دائىرە مۇئەييەن تەبىئىي پائالىيەت ئىسھاق ئۆزبېكىستانغا ھىنگان چەكلەنگەن گاڭگىراپ باشلانغۇچ جەمئىيەت جۇڭخۇا| qol baş put köz ceñçi cudé san sey é şir şañxey kitab veten tomur  kömür éliktir veten vyétnam şincañ anar encür orda uruş  ördek üzüm élan inkas inik'ana es'et radio mes'ul qariörük naümid  it'éyiq cem'iy nemengan özxan pasxa bayrimi maarip muellim daire mueyyen tebiiy paaliyet ishaq özbékistanğa hingan çeklengen gañgirap başlanğuç cem'iyet jungxua

# User interface

Pyqt is used for user interface. mainWindow.ui is graphic file which could be open by clicking on it.

        pyuic4 -x mainWindow.ui -o mainWindow.py (converting the ui file to python file)
        python umsc.py (run the gui program)

# Files
name | info
-----|----
mainWindow.ui | pyqt user interface
converter.py | functions for converting
umsc.py | main function for running the program which includes mainWindow.py and converter.py
materials | official materials for uyghur script converter
php_code  | this python code is improved version of the php code which is written by Mr. Gheyret Kenji.

