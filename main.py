import configparser
import os
import sys
import pyperclip
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QDesktopWidget
from PyQt5.QtMultimedia import QSoundEffect

from src.AK_encrypt import AK_decrypt, AK_encrypt

from design.main_ui import Ui_MainWindow as main_ui

ini_path = 'CONFIG.ini'
default_config = {
    'DESIGN': {
        'MAIN': 'design/main.ui',
    },
    'SOUND': {
        'PATH': 'sound/1.wav'
    },
}

def read_or_create_ini(file_path, default_values):
    """
    Read an existing INI file or create a new one with default values.

    Parameters:
        file_path (str): Path to the INI file.
        default_values (dict): Default values for sections and options.

    Returns:
        configparser.ConfigParser: ConfigParser object with read or default values.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file doesn't exist, create it with default values
        config = configparser.ConfigParser()

        # Write the default values to the INI file
        for section, options in default_values.items():
            config[section] = options

        # Write the configuration to the INI file
        with open(file_path, 'w') as configfile:
            config.write(configfile)

    # Read the INI file
    config = configparser.ConfigParser()
    config.read(file_path)

    # Check if each section exists, create it if not
    for section, options in default_values.items():
        if section not in config:
            config[section] = options
    return config

CONFIG = read_or_create_ini(ini_path,default_config)

MAIN_UI = CONFIG['DESIGN']['MAIN']
SOUND_PATH = CONFIG['SOUND']['PATH']

# from PyQt5.uic import loadUiType
# MainUI,_ = loadUiType(MAIN_UI)

class Main(QMainWindow, main_ui):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.sound_effect = QSoundEffect(self)
        self.sound_effect.setSource(QUrl.fromLocalFile(SOUND_PATH))
        self.handel_buttons()
        self.handel_ui()
        

    def handel_buttons(self):
        self.pushButton_2.clicked.connect(self.open_encrypt_tab)
        self.pushButton_3.clicked.connect(self.open_decrypt_tab)
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_4.clicked.connect(self.copy_encrypt)
        self.pushButton_5.clicked.connect(self.decrypt)
        self.pushButton_6.clicked.connect(self.copy_decrypt)
        
        self.lineEdit.returnPressed.connect(self.encrypt)
        self.lineEdit_6.returnPressed.connect(self.decrypt)
    
    def encrypt(self):
        try:
            self.lineEdit_2.setText('')
            secret_key = self.lineEdit_3.text()
            text = self.lineEdit.text()
            if (secret_key != '' or text != ''):
                if len(secret_key) not in [16,24,32]:
                    QMessageBox.warning(self,"اعلام","يجب ان يتكون مفتاح التشفير من 16 او 24 او 32 خانة")
                    return
                encrypt = AK_encrypt(secret_key,text)
                self.lineEdit_2.setText(encrypt)
                self.change_status_bar('تم التشفير بنجاح')
            else:
                QMessageBox.warning(self,"اعلام","من فضلك اكمل البيانات اولا")
                return
        except Exception as e:
            self.lineEdit_2.setText('')
            QMessageBox.critical(self,"error",f"حدث هذا الخطأ  : \n {e}")
            
    def copy_encrypt(self):
        text = self.lineEdit_2.text()
        if (text!=''):
            pyperclip.copy(text)
            self.change_status_bar('تم نسخ التشفير بنجاح')
    
    def decrypt(self):
        try:
            self.lineEdit_5.setText('')
            secret_key = self.lineEdit_4.text()
            text = self.lineEdit_6.text()
            if (secret_key != '' or text != ''):
                if len(secret_key)!=16:
                    QMessageBox.warning(self,"اعلام","يجب ان يكون مفتاح التشفير 16 خانة")
                    return
                decrypt = AK_decrypt(secret_key,text)
                self.lineEdit_5.setText(decrypt)
                self.change_status_bar('تم فك التشفير بنجاح')
            else:
                QMessageBox.warning(self,"اعلام","من فضلك اكمل البيانات اولا")
                return
        except Exception as e:
            self.lineEdit_5.setText('')
            QMessageBox.critical(self,"error",f"حدث هذا الخطأ  : \n {e}")
            
    def copy_decrypt(self):
        text = self.lineEdit_5.text()
        if (text!=''):
            pyperclip.copy(text)
            self.change_status_bar('تم نسخ فك التشفير بنجاح')
    
    def handel_ui(self):
        self.open_main_tab()
        self.showMaximized()
        self.setGeometry(*self.center_on_screen(510, 488))

    def center_on_screen(self, width, height):
        screen_geo = QDesktopWidget().screenGeometry()
        x = (screen_geo.width() - width) // 2
        y = (screen_geo.height() - height) // 2

        return x, y, width, height

        
    
    def open_main_tab(self):
        self.tabWidget.setCurrentIndex(0)
    
    def open_encrypt_tab(self):
        self.tabWidget.setCurrentIndex(1)
        
    def open_decrypt_tab(self):
        self.tabWidget.setCurrentIndex(2)
    
    def change_status_bar(self,message='',time_out=3000):
        self.play_sound()
        self.statusBar().showMessage(message,time_out)
        
    def play_sound(self):
        self.sound_effect.play()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    