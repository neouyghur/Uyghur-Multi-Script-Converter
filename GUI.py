import sys
import ctypes  # 新增导入Windows API模块 | Added Windows API module import
import os  # 添加os模块导入 | Added os module import
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,QLabel, QComboBox, QTextEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QFontDatabase
from umsc import UgMultiScriptConverter

# 多语言文本常量 - 新增代码 | Multilingual text constants - new code
LANGUAGES = {
    'en': {
        'window_title': 'Uyghur Script Converter',
        'source_label': 'Source Script:',
        'target_label': 'Target Script:',
        'input_label': 'Input Text:',
        'placeholder_text': 'Please enter text to convert...',
        'convert_btn': 'Convert Text',
        'result_label': 'Conversion Result:',
        'input_error_title': 'Input Error',
        'input_error_msg': 'Please enter text to convert!',
        'conversion_error_title': 'Conversion Error',
        'conversion_error_msg': 'An error occurred during conversion: %s'
    },
    'zh': {
        'window_title': '维吾尔文字母转换器',
        'source_label': '源脚本:',
        'target_label': '目标脚本:',
        'input_label': '输入文本:',
        'placeholder_text': '请输入要转换的文本...',
        'convert_btn': '转换文本',
        'result_label': '转换结果:',
        'input_error_title': '输入错误',
        'input_error_msg': '请输入要转换的文本!',
        'conversion_error_title': '转换错误',
        'conversion_error_msg': '转换过程中发生错误: %s',
        'scripts': [
            'ULS | 维吾尔拉丁字母',
            'UYS | 维吾尔新文字',
            'CPS | 中文拼音',
            'UAS | 维吾尔阿拉伯字母',
            'CTS | 通用突厥字母',
            'UCS | 维吾尔西里尔字母',
        ]
    },
    'ru': {
        'window_title': 'Конвертер уйгурских скриптов', 
        'source_label': 'Исходный скрипт:',  
        'target_label': 'Целевой скрипт:', 
        'input_label': 'Входной текст:',  
        'placeholder_text': 'Введите текст для преобразования...', 
        'convert_btn': 'Преобразовать текст', 
        'result_label': 'Результат преобразования:', 
        'input_error_title': 'Ошибка ввода',  
        'input_error_msg': 'Пожалуйста, введите текст для преобразования!', 
        'conversion_error_title': 'Ошибка преобразования', 
        'conversion_error_msg': 'Произошла ошибка во время преобразования: %s'
    }
}

# 添加静态脚本选项常量 | Add static script options constant
SCRIPTS = [
    'ULS | Uyghur Latin Script',
    'UYS | Uyghur New Script',
    'CPS | Chinese Pinyin Script',
    'UAS | Uyghur Arabic Script',
    'CTS | Common Turkic Script',
    'UCS | Uyghur Cyrillic Script',
]

# 当前语言选择 - 修改此处切换语言 ('en'/'zh'/'ru') | Current language selection - modify here to switch languages ('en'/'zh'/'ru')
CURRENT_LANGUAGE = 'en'
# 获取当前语言文本 | Get current language text
lang = LANGUAGES[CURRENT_LANGUAGE]

# 添加资源路径处理函数 | Add resource path handling function
def resource_path(relative_path):
    """获取资源的绝对路径，支持开发环境和打包后环境 | Get the absolute path of resources, supporting development and packaged environments"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# 隐藏终端窗口（仅Windows系统） | Hide terminal window (Windows only)
if sys.platform.startswith('win'):
    # 获取控制台窗口句柄 | Get console window handle
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        # 隐藏窗口（0=SW_HIDE） | Hide window (0=SW_HIDE)
        ctypes.windll.user32.ShowWindow(whnd, 0)
        # 释放句柄 | Release handle
        ctypes.windll.kernel32.CloseHandle(whnd)

class ScriptConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(lang['window_title'])  # 使用语言常量 | Use language constant
        self.setGeometry(100, 100, 800, 600)
        
        # 加载自定义字体文件 - 修改路径处理 | Load custom font file - modify path handling
        font_path = resource_path("font.ttf")  # 使用resource_path函数 | Use resource_path function
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            QMessageBox.warning(self, "Font Load Failed", f"Failed to load font file: {font_path}\nDefault font will be used")
            self.custom_font_family = None
        else:
            self.custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        # 创建中心部件和布局 | Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 脚本选择区域 | Script selection area
        script_layout = QHBoxLayout()
        
        # 源脚本选择 | Source script selection
        self.source_label = QLabel(lang['source_label'])  # 使用语言常量 | Use language constant
        self.source_combo = QComboBox()
        self._populate_script_combo(self.source_combo)
        
        # 目标脚本选择 | Target script selection
        self.target_label = QLabel(lang['target_label'])  # 使用语言常量 | Use language constant
        self.target_combo = QComboBox()
        self._populate_script_combo(self.target_combo)
        
        # 添加到脚本布局 | Add to script layout
        script_layout.addWidget(self.source_label)
        script_layout.addWidget(self.source_combo)
        script_layout.addSpacing(20)
        script_layout.addWidget(self.target_label)
        script_layout.addWidget(self.target_combo)
        
        # 文本输入区域 | Text input area
        self.input_label = QLabel(lang['input_label'])  # 使用语言常量 | Use language constant
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText(lang['placeholder_text'])  # 使用语言常量 | Use language constant
        # 设置输入框字体 | Set input box font
        input_font = self.input_text.font()
        input_font.setPointSize(20)
        if self.custom_font_family:
            input_font.setFamily(self.custom_font_family)
        self.input_text.setFont(input_font)
        
        # 转换按钮 | Conversion button
        self.convert_btn = QPushButton(lang['convert_btn'])  # 使用语言常量 | Use language constant
        self.convert_btn.clicked.connect(self.convert_text)
        
        # 结果显示区域 | Result display area
        self.result_label = QLabel(lang['result_label'])  # 使用语言常量 | Use language constant
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        # 设置输出框字体 | Set output box font
        result_font = self.result_text.font()
        result_font.setPointSize(20)
        if self.custom_font_family:
            result_font.setFamily(self.custom_font_family)
        self.result_text.setFont(result_font)
        
        # 添加所有部件到主布局 | Add all widgets to main layout
        main_layout.addLayout(script_layout)
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_text)
        main_layout.addWidget(self.convert_btn)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_text)
        
    def _populate_script_combo(self, combo):
        # 使用静态脚本列表替换多语言脚本列表 | Use static script list instead of multilingual script list
        for script in SCRIPTS:
            combo.addItem(script)
    def convert_text(self):
        """处理文本转换逻辑 | Handle text conversion logic"""
        try:
            # 获取选择的脚本（提取缩写部分） | Get selected script (extract abbreviation part)
            source_script = self.source_combo.currentText().split('|')[0].strip()
            target_script = self.target_combo.currentText().split('|')[0].strip()
            input_text = self.input_text.toPlainText()
            
            if not input_text.strip():
                QMessageBox.warning(self, lang['input_error_title'], lang['input_error_msg'])  # 使用语言常量 | Use language constant
                return
            
            # 执行转换 | Perform conversion
            converter = UgMultiScriptConverter(source_script, target_script)
            result = converter(input_text)
            
            # 显示结果 | Display result
            self.result_text.setText(result)
        except Exception as e:
            QMessageBox.critical(self, lang['conversion_error_title'], lang['conversion_error_msg'] % str(e))  # 使用语言常量 | Use language constant

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置英文字体支持 | Set English font support
    font = app.font()
    font.setFamily("Arial")  # 使用Arial字体确保英文显示正常 | Use Arial font to ensure proper English display
    app.setFont(font)
    
    window = ScriptConverterWindow()
    window.show()
    sys.exit(app.exec_())