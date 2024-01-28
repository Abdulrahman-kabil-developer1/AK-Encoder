# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\abdulrahman_ragab\Dropbox\Projects _\AK_Encoder\AK-Encoder\design\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(510, 515))
        MainWindow.setMaximumSize(QtCore.QSize(510, 515))
        MainWindow.setBaseSize(QtCore.QSize(510, 510))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #fff;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::focus\n"
"{\n"
"    background-color: rgb(39, 53, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #454544;\n"
"    font-weight: bold;\n"
"    \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #58D5D3;\n"
"    color: #ffffff;\n"
"    border: 5px;\n"
"    border-color: #000;\n"
"    border-radius: 25px;\n"
"\n"
"}\n"
"\n"
"QPushButton::focus\n"
"{\n"
"    background-color: #4d56a1;\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #4d56a1;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #58D5D3;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #58D5D3;\n"
"    \n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #58D5D3;\n"
"    border: 1px solid #58D5D3;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #58D5D3;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    color: #000;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"    background-color: #58D5D3;\n"
"    color: #fff;\n"
"    \n"
"    font-weight: bold;\n"
"    show-decoration-selected: 0;\n"
"    border-radius: 4px;\n"
"    padding-left: -15px;\n"
"    padding-right: -15px;\n"
"    padding-top: 5px;\n"
"\n"
"} \n"
"\n"
"\n"
"QListView:disabled \n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 0px;\n"
"    padding-left : 10px;\n"
"    height: 32px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    color: #000;\n"
"    background-color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"    color: #fff;\n"
"    background-color: #58D5D3;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"    background-color: #fff;\n"
"    show-decoration-selected: 0;\n"
"    color: #454544;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView:disabled\n"
"{\n"
"    background-color: #242526;\n"
"    show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"    background-color: #58D5D3;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"    background-color: #58D5D3;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #fff;\n"
"    border: 1px solid gray;\n"
"    color: #454544;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"QTapWidget item:selected {\n"
"    background-color: #A4B9BA;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #A4B9BA;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #ced5e3;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #2a547f;\n"
"    border: 0px;\n"
"    background-color: #ced5e3;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #58D5D3;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"/* QPushButton\n"
"{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
" */\n"
"QTabBar::tab:selected {\n"
"            background-color: lightblue;\n"
"              color: black;        }\n"
"\n"
"")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(510, 450))
        self.centralwidget.setBaseSize(QtCore.QSize(510, 450))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 291, 141))
        self.label.setStyleSheet("border-image: url(:/imgs/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 160, 501, 281))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 30, 321, 101))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 140, 321, 101))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setMaxLength(999999999)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(350, 70, 141, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 281, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName("pushButton")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(350, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setMouseTracking(True)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setMaxLength(999999999)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(400, 190, 81, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 190, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setMaxLength(999999999)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(3, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 10, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setMouseTracking(True)
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setMaxLength(999999999)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 190, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setMouseTracking(True)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setMaxLength(999999999)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(400, 190, 81, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 130, 281, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(350, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 70, 341, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setMouseTracking(True)
        self.lineEdit_6.setTabletTracking(False)
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setMaxLength(999999999)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(350, 70, 141, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(3, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setEnabled(False)
        self.label_30.setGeometry(QtCore.QRect(0, 440, 511, 31))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setEnabled(True)
        self.label_31.setGeometry(QtCore.QRect(0, 460, 511, 31))
        font = QtGui.QFont()
        font.setFamily("El Messiri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setOpenExternalLinks(True)
        self.label_31.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_31.setObjectName("label_31")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet("QStatusBar {\n"
"                background-color: #333;\n"
"                color: white;\n"
"                font-size: 16px;\n"
"                font-family: \"El Messiri\";\n"
"                font-weight: bold;\n"
"                text-align: center;\n"
"            }")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.pushButton_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AK Encoder"))
        self.pushButton_2.setText(_translate("MainWindow", "تشفير"))
        self.pushButton_3.setText(_translate("MainWindow", "فك تشفير"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "الرئيسية"))
        self.label_24.setText(_translate("MainWindow", "المراد تشفيرة"))
        self.pushButton.setText(_translate("MainWindow", "تشفير"))
        self.label_26.setText(_translate("MainWindow", "مفتاح التشفير"))
        self.label_25.setText(_translate("MainWindow", "النتيجة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "التشفير"))
        self.label_27.setText(_translate("MainWindow", "النتيجة"))
        self.pushButton_5.setText(_translate("MainWindow", "فك التشفير"))
        self.label_28.setText(_translate("MainWindow", "مفتاح التشفير"))
        self.label_29.setText(_translate("MainWindow", "المراد فك تشفيرة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "فك التشفير"))
        self.label_30.setText(_translate("MainWindow", "AK-Soft Technologies 2024 جميع حقوق النشر محفوظة لـ ©"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>(+20) 1149312512 <a href=\"mailto:abdulrahman.ragab.kabil@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">E-mail</span></a> - <a href=\"https://www.linkedin.com/in/abdulrahman-kabil-5729621a2/\"><span style=\" text-decoration: underline; color:#0000ff;\">LinkedIn</span></a></p></body></html>"))
import imgs_rc
