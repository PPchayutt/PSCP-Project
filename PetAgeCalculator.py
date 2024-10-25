# -*- coding: utf-8 -*-
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

def dog_to_human_age(dog_age):
    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4

def cat_to_human_age(cat_age):
    age_table = {
        1: 15, 2: 24, 3: 28, 4: 32, 5: 36, 6: 40, 7: 44, 8: 48, 9: 52, 10: 56,
        11: 60, 12: 64, 13: 68, 14: 72, 15: 76, 16: 80, 17: 84, 18: 88,
        19: 92, 20: 96, 21: 100, 22: 104, 23: 108, 24: 112, 25: 116
    }
    return age_table.get(cat_age, 116)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 919)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 226, 156);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(204, 142, 55);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:white;\n"
"    height:30px;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(250, 255, 235);\n"
"    color: rgb(204, 142, 55);\n"
"    font-weight:bold;\n"
"}")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/gui/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gui/dog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/gui/cat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 516, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gui/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.gridLayout_4.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/gui/cat.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox_2.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_7.addWidget(self.spinBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(250, 250))
        self.textBrowser_4.setMaximumSize(QtCore.QSize(250, 250))
        self.textBrowser_4.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_9.addWidget(self.textBrowser_4)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_9.addWidget(self.textBrowser_6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_3.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_8.addWidget(self.textBrowser_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 162, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.gridLayout_3.addWidget(self.widget_2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/gui/bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoRepeat(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        spacerItem4 = QtWidgets.QSpacerItem(638, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget.setObjectName("widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 50))
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/gui/dog.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_5.addWidget(self.spinBox_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(250, 250))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(250, 250))
        self.textBrowser_2.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_8.addWidget(self.textBrowser_2)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_5.setTabChangesFocus(False)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_8.addWidget(self.textBrowser_5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_9.addWidget(self.textBrowser_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 162, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 1, 1)
        self.icon_namewidget = QtWidgets.QWidget(self.centralwidget)
        self.icon_namewidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(204, 142, 55);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:white;\n"
"    text-align:left;\n"
"    height:30px;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(250, 255, 235);\n"
"    color: rgb(204, 142, 55);\n"
"    font-weight:bold;\n"
"}")
        self.icon_namewidget.setObjectName("icon_namewidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_namewidget)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.icon_namewidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 60))
        self.label_2.setMaximumSize(QtCore.QSize(60, 60))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/gui/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.icon_namewidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 504, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.pushButton_6 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.gridLayout_4.addWidget(self.icon_namewidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # กำหนด font สำหรับ TextBrowser
        thai_font = QtGui.QFont()
        thai_font.setFamily("TH Sarabun New")
        thai_font.setPointSize(16)
        thai_font.setBold(True)

        # สไตล์สำหรับ TextBrowser ทั้งหมด
        text_browser_style = """
            QTextBrowser {
                background-color: rgb(250, 255, 235);
                border: 2px solid rgb(204, 142, 55);
                border-radius: 10px;
                padding: 15px;
                color: rgb(70, 70, 70);
            }
            QTextBrowser:hover {
                border: 2px solid rgb(180, 120, 40);
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(240, 240, 240);
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: rgb(204, 142, 55);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """

        # กำหนดสไตล์และ font ให้กับแต่ละ TextBrowser แยกทีละตัว
        self.textBrowser_2.setFont(thai_font)
        self.textBrowser_2.setStyleSheet(text_browser_style)
        self.textBrowser_2.document().setDocumentMargin(10)
        self.textBrowser_4.setFont(thai_font)
        self.textBrowser_4.setStyleSheet(text_browser_style)
        self.textBrowser_4.document().setDocumentMargin(10)
        self.textBrowser_5.setFont(thai_font)
        self.textBrowser_5.setStyleSheet(text_browser_style)
        self.textBrowser_5.document().setDocumentMargin(10)
        self.textBrowser_6.setFont(thai_font)
        self.textBrowser_6.setStyleSheet(text_browser_style)
        self.textBrowser_6.document().setDocumentMargin(10)
        self.textBrowser_2.setStyleSheet(text_browser_style)
        self.textBrowser_4.setStyleSheet(text_browser_style)
        self.textBrowser_5.setStyleSheet(text_browser_style)
        self.textBrowser_6.setStyleSheet(text_browser_style)
        self.retranslateUi(MainWindow)
        self.pushButton_9.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.pushButton_9.toggled['bool'].connect(self.icon_namewidget.setHidden) # type: ignore
        self.pushButton_4.toggled['bool'].connect(self.pushButton_2.setChecked) # type: ignore
        self.pushButton_4.toggled['bool'].connect(self.widget.setHidden) # type: ignore
        self.pushButton_4.toggled['bool'].connect(self.widget_2.setVisible) # type: ignore
        self.pushButton_2.toggled['bool'].connect(self.pushButton_4.setChecked) # type: ignore
        self.pushButton.toggled['bool'].connect(self.pushButton_3.setChecked) # type: ignore
        self.pushButton_3.toggled['bool'].connect(self.pushButton.setChecked) # type: ignore
        self.pushButton_3.toggled['bool'].connect(self.widget.setVisible) # type: ignore
        self.pushButton_3.toggled['bool'].connect(self.widget_2.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(25)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(25)
        self.spinBox_3.setSingleStep(1)
        self.pushButton_7.clicked.connect(self.calculate_dog_age)
        self.pushButton_8.clicked.connect(self.calculate_cat_age)
        self.pushButton_5.clicked.connect(self.exit_application)
        self.pushButton_6.clicked.connect(self.exit_application)
        main_color = "#B87333"
        secondary_color = "#FFF8DC"
        accent_color = "#8B4513"
        self.centralwidget.setStyleSheet(f"background-color: {secondary_color};")
        
        # สไตล์สำหรับปุ่ม
        button_style = """
            QPushButton {
                background-color: #B87333;
                color: white;
                border: 2px solid #8B4513;
                border-radius: 15px;
                padding: 8px 15px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #8B4513;
                border: 2px solid #B87333;
                transition: background-color 0.3s;
            }
            QPushButton:pressed {
                background-color: #6B4423;
                border: 3px solid #B87333;
                padding: 10px 15px;
            }
        """
        
        # สไตล์สำหรับ SpinBox
        spinbox_style = """
            QSpinBox {
                background-color: white;
                border: 2px solid #B87333;
                border-radius: 10px;
                padding: 5px;
                min-height: 30px;
                font-size: 14px;
            }
            QSpinBox::up-button {
                width: 20px;
                border: 1px solid #B87333;
                border-top-right-radius: 8px;
                background-color: #FFF8DC;
                margin-top: 1px;
                margin-right: 1px;
                subcontrol-position: top right;
            }
            QSpinBox::down-button {
                width: 20px;
                border: 1px solid #B87333;
                border-bottom-right-radius: 8px;
                background-color: #FFF8DC;
                margin-bottom: 1px;
                margin-right: 1px;
                subcontrol-position: bottom right;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: #FFE4B5;
            }
            QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {
                background-color: #DEB887;
            }
            QSpinBox::up-arrow {
                image: url(:/gui/up_arrow.png);
                width: 10px;
                height: 10px;
            }
            QSpinBox::down-arrow {
                image: url(:/gui/down_arrow.png);
                width: 10px;
                height: 10px;
            }
        """

        # สไตล์สำหรับ widget หลัก
        widget_style = f"""
            QWidget#widget, QWidget#widget_2 {{
                background-color: {main_color};
                border-radius: 20px;
                margin: 10px;
            }}
        """

        # สไตล์สำหรับ label
        label_style = """
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
            }
        """

        # สไตล์สำหรับ TextBrowser
        text_browser_style = f"""
            QTextBrowser {{
                background-color: white;
                border: 2px solid {main_color};
                border-radius: 15px;
                padding: 15px;
                color: #333333;
                font-size: 14px;
            }}
            QTextBrowser:hover {{
                border: 2px solid {accent_color};
            }}
            QScrollBar:vertical {{
                border: none;
                background: #F0F0F0;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical {{
                background: {main_color};
                min-height: 20px;
                border-radius: 5px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """

        # กำหนดสไตล์ให้กับ widgets
        self.pushButton_7.setStyleSheet(button_style)
        self.pushButton_8.setStyleSheet(button_style)
        self.spinBox_2.setStyleSheet(spinbox_style)
        self.spinBox_3.setStyleSheet(spinbox_style)
        self.widget.setStyleSheet(widget_style)
        self.widget_2.setStyleSheet(widget_style)
        
        # กำหนด font สำหรับ TextBrowser
        thai_font = QtGui.QFont()
        thai_font.setFamily("TH Sarabun New")
        thai_font.setPointSize(16)
        thai_font.setBold(True)

        # กำหนดสไตล์และ font ให้กับ TextBrowser
        for browser in [self.textBrowser_2, self.textBrowser_4, 
                       self.textBrowser_5, self.textBrowser_6]:
            browser.setFont(thai_font)
            browser.setStyleSheet(text_browser_style)
            browser.document().setDocumentMargin(15)

        # เพิ่ม Effect เงา
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 50))
        self.widget.setGraphicsEffect(shadow)
        shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(20)
        shadow2.setXOffset(5)
        shadow2.setYOffset(5)
        shadow2.setColor(QtGui.QColor(0, 0, 0, 50))
        self.widget_2.setGraphicsEffect(shadow2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pet Age Calculator"))
        self.label_7.setText(_translate("MainWindow", "Cat's Age (1-25 Year)"))
        self.pushButton_8.setText(_translate("MainWindow", "Calculate"))
        self.label_6.setText(_translate("MainWindow", "Dog's Age (1-25 Year)"))
        self.pushButton_7.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "PAC"))
        self.pushButton_3.setText(_translate("MainWindow", "DOG"))
        self.pushButton_4.setText(_translate("MainWindow", "CAT"))
        self.pushButton_6.setText(_translate("MainWindow", "Exit"))

    def calculate_dog_age(self):
        dog_age = self.spinBox_3.value()
        human_age = dog_to_human_age(dog_age)
    
        # จัดรูปแบบข้อความให้สวยงาม
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐶 ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุสุนัข:</b> {dog_age} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """
        calculation = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📝 วิธีการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>สูตรที่ใช้:</b><br>
                • 1-2 ปีแรก: อายุคน = อายุสุนัข × 10.5<br>
                • หลังจากนั้น: อายุคน = 21 + (อายุสุนัข - 2) × 4
            </p>
        </div>
        """
        self.textBrowser_2.setHtml(result)
        self.textBrowser_5.setHtml(calculation)

    def calculate_cat_age(self):
        cat_age = self.spinBox_2.value()
        human_age = cat_to_human_age(cat_age)
        life_stage = self.get_cat_life_stage(cat_age)

        # จัดรูปแบบข้อความให้สวยงาม
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐱 ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุแมว:</b> {cat_age} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>ช่วงชีวิต:</b><br>
                {life_stage}
            </p>
        </div>
        """
        self.textBrowser_4.setHtml(result)
        self.textBrowser_6.setHtml(info)

    def get_cat_life_stage(self, age):
        stages = {
            (0, 1): "🐱 Kitten (แรกเกิดถึง 1 ปี)\nช่วงวัยเด็ก การเจริญเติบโตและพัฒนาการสูง",
            (1, 2): "🐱 Junior (1-2 ปี)\nช่วงวัยรุ่น เต็มไปด้วยพลังและความกระตือรือร้น",
            (2, 6): "🐱 Prime (3-6 ปี)\nช่วงวัยผู้ใหญ่ สมบูรณ์แข็งแรงที่สุด",
            (6, 10): "🐱 Mature (7-10 ปี)\nช่วงวัยกลางคน เริ่มมีการเปลี่ยนแปลงทางร่างกาย",
            (10, 15): "🐱 Senior (11-14 ปี)\nช่วงวัยสูงอายุ ต้องการการดูแลเป็นพิเศษ",
            (15, 100): "🐱 Geriatric (15 ปีขึ้นไป)\nช่วงวัยชรา ต้องการการดูแลอย่างใกล้ชิด"
        }
        for (min_age, max_age), description in stages.items():
            if min_age <= age < max_age:
                return description
        return stages[(15, 100)]
    def exit_application(self):
        QtWidgets.QApplication.quit()

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
