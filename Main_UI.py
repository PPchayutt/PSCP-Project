"""โค้ดส่วนหน้า UI ของโปรแกรม"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from calculation import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """ส่วน Main UI"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gui/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 226, 156);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.pushButton_14 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_14.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gui/hamster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_17 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_17.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/gui/hedgehog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon3)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_18.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/gui/bunny.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon4)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_19.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/gui/squirrel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout.addWidget(self.pushButton_19)
        spacerItem = QtWidgets.QSpacerItem(20, 546, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_5.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/gui/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout_3.addWidget(self.icon_only_widget, 0, 0, 1, 1)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icon_namewidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
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
        self.pushButton_15 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_20 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_20.setIcon(icon4)
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_2.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_2.addWidget(self.pushButton_21)
        spacerItem1 = QtWidgets.QSpacerItem(20, 546, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtWidgets.QPushButton(self.icon_namewidget)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.gridLayout_3.addWidget(self.icon_namewidget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/gui/bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoRepeat(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(898, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
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
        spacerItem3 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setMinimumHeight(400)
        self.textBrowser_2.setMaximumHeight(400)
        self.textBrowser_2.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_8.addWidget(self.textBrowser_2)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setMinimumHeight(400)
        self.textBrowser_5.setMaximumHeight(400)
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_5.setTabChangesFocus(False)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_8.addWidget(self.textBrowser_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_8.setStretch(0, 30)
        self.horizontalLayout_8.setStretch(1, 70)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setMinimumHeight(220)
        self.textBrowser_7.setMaximumHeight(220)
        self.textBrowser_7.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_9.addWidget(self.textBrowser_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_22.addWidget(self.widget)
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
        spacerItem6 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_4.setMinimumHeight(400)
        self.textBrowser_4.setMaximumHeight(400)
        self.textBrowser_4.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_9.addWidget(self.textBrowser_4)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_9.addWidget(self.textBrowser_6)
        self.horizontalLayout_9.setStretch(0, 30)
        self.horizontalLayout_9.setStretch(1, 70)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_3.setMinimumHeight(220)
        self.textBrowser_3.setMaximumHeight(220)
        self.textBrowser_3.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_8.addWidget(self.textBrowser_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.horizontalLayout_22.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setMinimumSize(QtCore.QSize(50, 50))
        self.label_8.setMaximumSize(QtCore.QSize(50, 50))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/gui/hamster.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox_4.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_4.setObjectName("spinBox_4")
        self.verticalLayout_14.addWidget(self.spinBox_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_14)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem9 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_10.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_11.addWidget(self.pushButton_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_8.setMinimumHeight(400)
        self.textBrowser_8.setMaximumHeight(400)
        self.textBrowser_8.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.horizontalLayout_12.addWidget(self.textBrowser_8)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_9.setTabChangesFocus(False)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout_12.addWidget(self.textBrowser_9)
        self.horizontalLayout_12.setStretch(0, 30)
        self.horizontalLayout_12.setStretch(1, 70)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem10 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem10)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_10.setMinimumHeight(220)
        self.textBrowser_10.setMaximumHeight(220)
        self.textBrowser_10.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.verticalLayout_15.addWidget(self.textBrowser_10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem11)
        self.verticalLayout_12.addLayout(self.verticalLayout_15)
        self.horizontalLayout_22.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.widget_5)
        self.label_10.setMinimumSize(QtCore.QSize(50, 50))
        self.label_10.setMaximumSize(QtCore.QSize(50, 50))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/gui/hedgehog.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_18.addWidget(self.label_11)
        self.spinBox_5 = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_5.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_5.setObjectName("spinBox_5")
        self.verticalLayout_18.addWidget(self.spinBox_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_18)
        self.verticalLayout_17.addLayout(self.horizontalLayout_13)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem12 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_11.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_14.addWidget(self.pushButton_11)
        self.verticalLayout_16.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_11.setMinimumHeight(400)
        self.textBrowser_11.setMaximumHeight(400)
        self.textBrowser_11.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.horizontalLayout_15.addWidget(self.textBrowser_11)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_12.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_12.setTabChangesFocus(False)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.horizontalLayout_15.addWidget(self.textBrowser_12)
        self.horizontalLayout_15.setStretch(0, 30)
        self.horizontalLayout_15.setStretch(1, 70)
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        spacerItem13 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem13)
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_13.setMinimumHeight(220)
        self.textBrowser_13.setMaximumHeight(220)
        self.textBrowser_13.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.verticalLayout_19.addWidget(self.textBrowser_13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem14)
        self.verticalLayout_16.addLayout(self.verticalLayout_19)
        self.horizontalLayout_22.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setMinimumSize(QtCore.QSize(50, 50))
        self.label_12.setMaximumSize(QtCore.QSize(50, 50))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/gui/bunny.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_22.addWidget(self.label_13)
        self.spinBox_6 = QtWidgets.QSpinBox(self.widget_6)
        self.spinBox_6.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_6.setObjectName("spinBox_6")
        self.verticalLayout_22.addWidget(self.spinBox_6)
        self.horizontalLayout_16.addLayout(self.verticalLayout_22)
        self.verticalLayout_21.addLayout(self.horizontalLayout_16)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem15 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem15)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_12.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_17.addWidget(self.pushButton_12)
        self.verticalLayout_20.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_14.setMinimumHeight(400)
        self.textBrowser_14.setMaximumHeight(400)
        self.textBrowser_14.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.horizontalLayout_18.addWidget(self.textBrowser_14)
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_15.setTabChangesFocus(False)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.horizontalLayout_18.addWidget(self.textBrowser_15)
        self.horizontalLayout_18.setStretch(0, 30)
        self.horizontalLayout_18.setStretch(1, 70)
        self.verticalLayout_20.addLayout(self.horizontalLayout_18)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        spacerItem16 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(spacerItem16)
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_16.setMinimumHeight(220)
        self.textBrowser_16.setMaximumHeight(220)
        self.textBrowser_16.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.verticalLayout_23.addWidget(self.textBrowser_16)
        spacerItem17 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(spacerItem17)
        self.verticalLayout_20.addLayout(self.verticalLayout_23)
        self.horizontalLayout_22.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setStyleSheet("background-color: rgb(204, 142, 55);")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.widget_7)
        self.label_14.setMinimumSize(QtCore.QSize(50, 50))
        self.label_14.setMaximumSize(QtCore.QSize(50, 50))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/gui/squirrel.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_15 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_26.addWidget(self.label_15)
        self.spinBox_7 = QtWidgets.QSpinBox(self.widget_7)
        self.spinBox_7.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.spinBox_7.setObjectName("spinBox_7")
        self.verticalLayout_26.addWidget(self.spinBox_7)
        self.horizontalLayout_19.addLayout(self.verticalLayout_26)
        self.verticalLayout_25.addLayout(self.horizontalLayout_19)
        self.verticalLayout_24.addLayout(self.verticalLayout_25)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem18 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem18)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_13.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_20.addWidget(self.pushButton_13)
        self.verticalLayout_24.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser_17.setMinimumHeight(400)
        self.textBrowser_17.setMaximumHeight(400)
        self.textBrowser_17.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.horizontalLayout_21.addWidget(self.textBrowser_17)
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser_18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_18.setTabChangesFocus(False)
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.horizontalLayout_21.addWidget(self.textBrowser_18)
        self.horizontalLayout_21.setStretch(0, 30)
        self.horizontalLayout_21.setStretch(1, 70)
        self.verticalLayout_24.addLayout(self.horizontalLayout_21)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        spacerItem19 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem19)
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser_19.setMinimumHeight(220)
        self.textBrowser_19.setMaximumHeight(220)
        self.textBrowser_19.setStyleSheet("background-color: rgb(250, 255, 235);")
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.verticalLayout_27.addWidget(self.textBrowser_19)
        spacerItem20 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem20)
        self.verticalLayout_24.addLayout(self.verticalLayout_27)
        self.horizontalLayout_22.addWidget(self.widget_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2483, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        main_color = "#B87333"
        secondary_color = "#FFF8DC"
        accent_color = "#8B4513"

        # สไตล์สำหรับทุก widget ของสัตว์เลี้ยง
        for widget in [self.widget, self.widget_2, self.widget_4, 
                      self.widget_5, self.widget_6, self.widget_7]:
            widget.setStyleSheet(f"""
                background-color: {main_color};
                border-radius: 20px;
                margin: 10px;
                padding: 15px;
            """)
            
            # สร้าง shadow effect สำหรับแต่ละ widget
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setBlurRadius(20)
            shadow.setXOffset(5)
            shadow.setYOffset(5)
            shadow.setColor(QtGui.QColor(0, 0, 0, 50))
            widget.setGraphicsEffect(shadow)

        # สไตล์สำหรับทุก TextBrowser
        all_browsers = [
            self.textBrowser_2, self.textBrowser_3, self.textBrowser_4, 
            self.textBrowser_5, self.textBrowser_6, self.textBrowser_8, 
            self.textBrowser_9, self.textBrowser_11, self.textBrowser_12, 
            self.textBrowser_14, self.textBrowser_15, self.textBrowser_17, 
            self.textBrowser_18, self.textBrowser_7, self.textBrowser_10, 
            self.textBrowser_13, self.textBrowser_16, self.textBrowser_19
        ]

        text_style = """
            QTextBrowser {
                background-color: rgb(250, 255, 235);
                border: 2px solid rgb(204, 142, 55);
                border-radius: 15px;
                padding: 15px;
                color: rgb(70, 70, 70);
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(240, 240, 240);
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: rgb(204, 142, 55);
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """

        for browser in all_browsers:
            browser.setStyleSheet(text_style)

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

        # กำหนด font และสไตล์สำหรับทุก TextBrowser
        thai_font = QtGui.QFont()
        thai_font.setFamily("TH Sarabun New")
        thai_font.setPointSize(16)
        thai_font.setBold(True)

        for browser in all_browsers:
            browser.setFont(thai_font)
            browser.setStyleSheet(text_browser_style)
            browser.document().setDocumentMargin(15)

        # สไตล์สำหรับทุกปุ่ม "คำนวณ"
        all_buttons = [
            self.pushButton_7, self.pushButton_8, self.pushButton_10,
            self.pushButton_11, self.pushButton_12, self.pushButton_13
        ]

        button_style = f"""
            QPushButton {{
                background-color: {main_color};
                color: white;
                border: 2px solid {accent_color};
                border-radius: 15px;
                padding: 8px 15px;
                font-weight: bold;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: {accent_color};
                border: 2px solid {main_color};
            }}
            QPushButton:pressed {{
                background-color: #6B4423;
                border: 3px solid {main_color};
                padding: 10px 15px;
            }}
        """

        for button in all_buttons:
            button.setStyleSheet(button_style)

        # สไตล์สำหรับทุก SpinBox
        all_spinboxes = [
            self.spinBox_2, self.spinBox_3, self.spinBox_4,
            self.spinBox_5, self.spinBox_6, self.spinBox_7
        ]

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

        for spinbox in all_spinboxes:
            spinbox.setStyleSheet(spinbox_style)

        # กำหนดสไตล์สำหรับ label
        all_labels = [
            self.label_6, self.label_7, self.label_9,
            self.label_11, self.label_13, self.label_15
        ]
        label_style = """
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
            }
        """

        for label in all_labels:
            label.setStyleSheet(label_style)  
  
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
        self.pushButton_9.toggled['bool'].connect(self.icon_namewidget.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget_2.setVisible)
        self.pushButton_3.toggled['bool'].connect(self.widget.setVisible)
        self.pushButton_3.toggled['bool'].connect(self.widget_2.setHidden)
        self.pushButton_9.toggled['bool'].connect(self.icon_only_widget.setVisible)
        self.pushButton_4.toggled['bool'].connect(self.pushButton_2.setChecked)
        self.pushButton.toggled['bool'].connect(self.pushButton_3.setChecked)
        self.pushButton_3.toggled['bool'].connect(self.pushButton.setChecked)
        self.pushButton_2.toggled['bool'].connect(self.pushButton_4.setChecked)
        self.pushButton_3.toggled['bool'].connect(self.widget_4.setHidden)
        self.pushButton_3.toggled['bool'].connect(self.widget_5.setHidden)
        self.pushButton_3.toggled['bool'].connect(self.widget_6.setHidden)
        self.pushButton_3.toggled['bool'].connect(self.widget_7.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget_4.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget_5.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget_6.setHidden)
        self.pushButton_4.toggled['bool'].connect(self.widget_7.setHidden)
        self.pushButton_15.toggled['bool'].connect(self.pushButton_14.setChecked)
        self.pushButton_15.toggled['bool'].connect(self.pushButton_14.setChecked)
        self.pushButton_15.toggled['bool'].connect(self.widget.setHidden)
        self.pushButton_15.toggled['bool'].connect(self.widget_2.setHidden)
        self.pushButton_15.toggled['bool'].connect(self.widget_4.setVisible)
        self.pushButton_15.toggled['bool'].connect(self.widget_5.setHidden)
        self.pushButton_15.toggled['bool'].connect(self.widget_6.setHidden)
        self.pushButton_15.toggled['bool'].connect(self.widget_7.setHidden)
        self.pushButton_16.toggled['bool'].connect(self.pushButton_17.setChecked)
        self.pushButton_17.toggled['bool'].connect(self.pushButton_16.setChecked)
        self.pushButton_16.toggled['bool'].connect(self.widget.setHidden)
        self.pushButton_16.toggled['bool'].connect(self.widget_2.setHidden)
        self.pushButton_16.toggled['bool'].connect(self.widget_4.setHidden)
        self.pushButton_16.toggled['bool'].connect(self.widget_5.setVisible)
        self.pushButton_16.toggled['bool'].connect(self.widget_6.setHidden)
        self.pushButton_16.toggled['bool'].connect(self.widget_7.setHidden)
        self.pushButton_18.toggled['bool'].connect(self.pushButton_20.setChecked)
        self.pushButton_20.toggled['bool'].connect(self.pushButton_18.setChecked)
        self.pushButton_21.toggled['bool'].connect(self.pushButton_19.setChecked)
        self.pushButton_19.toggled['bool'].connect(self.pushButton_21.setChecked)
        self.pushButton_20.toggled['bool'].connect(self.widget.setHidden)
        self.pushButton_20.toggled['bool'].connect(self.widget_2.setHidden)
        self.pushButton_20.toggled['bool'].connect(self.widget_4.setHidden)
        self.pushButton_20.toggled['bool'].connect(self.widget_5.setHidden)
        self.pushButton_20.toggled['bool'].connect(self.widget_6.setVisible)
        self.pushButton_20.toggled['bool'].connect(self.widget_7.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget_2.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget_4.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget_5.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget_6.setHidden)
        self.pushButton_21.toggled['bool'].connect(self.widget_7.setVisible)
        self.pushButton_14.toggled['bool'].connect(self.pushButton_15.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.spinBox_2.setMinimum(0) # dog
        self.spinBox_2.setMaximum(25)
        self.spinBox_2.setSingleStep(1)

        self.spinBox_3.setMinimum(0) # cat
        self.spinBox_3.setMaximum(25)
        self.spinBox_3.setSingleStep(1)

        self.pushButton_7.clicked.connect(self.calculate_dog_age)
        self.pushButton_8.clicked.connect(self.calculate_cat_age)
        self.pushButton_5.clicked.connect(self.exit_application)
        self.pushButton_6.clicked.connect(self.exit_application)

        self.spinBox_4.setMinimum(0)  # hamster
        self.spinBox_4.setMaximum(3)
        self.spinBox_4.setSingleStep(1)

        self.spinBox_5.setMinimum(0)  # hedgehog
        self.spinBox_5.setMaximum(7)
        self.spinBox_5.setSingleStep(1)

        self.spinBox_6.setMinimum(0)  # bunny
        self.spinBox_6.setMaximum(16)
        self.spinBox_6.setSingleStep(1)

        self.spinBox_7.setMinimum(0) # squirrel
        self.spinBox_7.setMaximum(23)
        self.spinBox_7.setSingleStep(1)

        self.pushButton_10.clicked.connect(self.calculate_hamster_age)
        self.pushButton_11.clicked.connect(self.calculate_hedgehog_age)
        self.pushButton_12.clicked.connect(self.calculate_bunny_age)
        self.pushButton_13.clicked.connect(self.calculate_squirrel_age)
        self.centralwidget.setStyleSheet(f"background-color: {secondary_color};")

    def retranslateUi(self, MainWindow):
        """ข้อความของ UI"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pet Age Calculator"))
        self.label_3.setText(_translate("MainWindow", "PAC"))
        self.pushButton_3.setText(_translate("MainWindow", "สุนัข"))
        self.pushButton_4.setText(_translate("MainWindow", "แมว"))
        self.pushButton_15.setText(_translate("MainWindow", "แฮมสเตอร์"))
        self.pushButton_16.setText(_translate("MainWindow", "เม่น"))
        self.pushButton_20.setText(_translate("MainWindow", "กระต่าย"))
        self.pushButton_21.setText(_translate("MainWindow", "กระรอก"))
        self.pushButton_6.setText(_translate("MainWindow", "ออก"))
        self.label_6.setText(_translate("MainWindow", "อายุสุนัข (0-25 ปี)"))
        self.pushButton_7.setText(_translate("MainWindow", "คำนวณ"))
        self.label_7.setText(_translate("MainWindow", "อายุแมว (0-25 ปี)"))
        self.pushButton_8.setText(_translate("MainWindow", "คำนวณ"))
        self.label_9.setText(_translate("MainWindow", "อายุแฮมสเตอร์ (0-3 ปี)"))
        self.pushButton_10.setText(_translate("MainWindow", "คำนวณ"))
        self.label_11.setText(_translate("MainWindow", "อายุเม่น (0-7 ปี)"))
        self.pushButton_11.setText(_translate("MainWindow", "คำนวณ"))
        self.label_13.setText(_translate("MainWindow", "อายุกระต่าย (0-16 ปี)"))
        self.pushButton_12.setText(_translate("MainWindow", "คำนวณ"))
        self.label_15.setText(_translate("MainWindow", "อายุกระรอก (0-23 ปี)"))
        self.pushButton_13.setText(_translate("MainWindow", "คำนวณ"))

    def calculate_dog_age(self):
        """แสดงการคำนวณอายุสุนัข"""
        dog_age = self.spinBox_3.value()
        human_age = dog_to_human_age(dog_age)
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🐶 ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุสุนัข</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{dog_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """
        
        calculation = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>สูตรที่ใช้:</b><br>
                🐶 1-2 ปีแรก: อายุคน = อายุสุนัข × 10.5<br>
                🐶 หลังจากนั้น: อายุคน = 21 + (อายุสุนัข - 2) × 4
            </p>
            <hr style='border: 1px solid #B87333; margin: 15px 0;'>
            <h3 style='color: #B87333;'>⚠️ หมายเหตุ:</h3>
            <p style='font-size: 16px; margin: 10px 0;'>
                การคำนวณนี้เป็นเพียงการประเมินคร่าวๆ<br>
                อายุที่แท้จริงอาจแตกต่างกันตามขนาดและน้ำหนักของสุนัข<br><br>
                <b>โดยทั่วไป:</b><br>
                • สุนัขพันธุ์เล็ก อายุยืนกว่าพันธุ์ใหญ่<br>
                • สุนัขพันธุ์ใหญ่ เข้าสู่วัยชราเร็วกว่าพันธุ์เล็ก
            </p>
        </div>
        """

        # กำหนดข้อมูลตามช่วงอายุ
        if dog_age < 1:
            stage_title = "🐕 Puppy"
            stage_age = "แรกเกิดถึง 1 ปี"
            stage_desc = "ช่วงวัยเด็ก การเจริญเติบโตและพัฒนาการสูง"
            stage_detail = """
            • ต้องการวัคซีนและการถ่ายพยาธิ
            • การฝึกพื้นฐานและการเข้าสังคม
            • อาหารสำหรับลูกสุนัขโดยเฉพาะ
            """
        elif 1 <= dog_age <= 8:
            stage_title = "🐕 Adult"
            stage_age = "1-8 ปี"
            stage_desc = "ช่วงวัยผู้ใหญ่ แข็งแรงสมบูรณ์"
            stage_detail = """
            • ควรได้รับการออกกำลังกายสม่ำเสมอ
            • ตรวจสุขภาพประจำปี
            • ดูแลสุขภาพฟันและเหงือก
            """
        else:
            stage_title = "🐕 Senior"
            stage_age = "มากกว่า 8 ปี"
            stage_desc = "ช่วงวัยชรา ต้องการการดูแลเป็นพิเศษ"
            stage_detail = """
            • ตรวจสุขภาพทุก 6 เดือน
            • อาหารสำหรับสุนัขสูงอายุ
            • ระวังโรคข้อและกระดูก
            """

        stage_info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                <h2 style='color: #B87333; margin-bottom: 5px;'>{stage_title}</h2>
                <h3 style='color: #8B4513; margin-top: 5px;'>อายุ: {stage_age}</h3>
            </div>
            
            <div style='margin: 15px 0; padding: 10px; background-color: rgba(184, 115, 51, 0.1); border-radius: 5px;'>
                <p style='color: #666; margin: 0;'>{stage_desc}</p>
            </div>
            
            <div style='margin-top: 15px;'>
                <p style='color: #B87333; font-weight: bold; margin-bottom: 10px;'>การดูแลที่เหมาะสม:</p>
                <div style='color: #666; padding-left: 10px;'>
                    {stage_detail.strip().replace('•', '&#8226;')}
                </div>
            </div>
        </div>
        """
        
        self.textBrowser_2.setHtml(result)
        self.textBrowser_5.setHtml(calculation)
        self.textBrowser_7.setHtml(stage_info)

    def calculate_cat_age(self):
        """แสดงการคำนวณอายุแมว"""
        cat_age = self.spinBox_2.value()
        human_age = cat_to_human_age(cat_age)
        stage_info = self.get_cat_stage_info(cat_age)
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🐱 ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุแมว</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{cat_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """
        calculation = f"""
            <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
                <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
                <p style='font-size: 16px; margin: 10px 0;'>
                    <b>การคำนวณอายุแมว:</b><br>
                    • 1 ปีแรก = 15 ปีคน<br>
                    • 2 ปี = 24 ปีคน<br>
                    • แต่ละปีหลังจากนั้น = ประมาณ 4 ปีคน<br>
                </p>
                <hr style='border: 1px solid #B87333; margin: 15px 0;'>
                <h3 style='color: #B87333;'>⚠️ คำเตือน:</h3>
                <p style='font-size: 16px; margin: 10px 0;'>
                    การคำนวณนี้เป็นเพียงการประมาณค่า<br>
                    อายุที่แท้จริงอาจแตกต่างกันตาม:<br>
                    • สายพันธุ์แมว<br>
                    • พันธุกรรม<br>
                    • การเลี้ยงดูและสภาพแวดล้อม<br>
                    • สุขภาพโดยรวม
                </p>
            </div>
            """

        self.textBrowser_4.setHtml(result)
        self.textBrowser_6.setHtml(calculation)
        self.textBrowser_3.setHtml(stage_info)

    def get_cat_stage_info(self, age):
        """ข้อมูลรายละเอียดช่วงวัยแมว"""
        if age < 0.5:  # น้อยกว่า 6 เดือน
            stage_title = "🐱 Kitten"
            stage_age = "แรกเกิด - 6 เดือน"
            stage_desc = "ช่วงวัยลูกแมว การเจริญเติบโตอย่างรวดเร็ว"
            stage_detail = """
            • ต้องการสารอาหารและพลังงานมากเป็นพิเศษ 
            • ช่วงการพัฒนาที่สำคัญ
            • ต้องการวัคซีนและการถ่ายพยาธิ
            """
        elif 0.5 <= age <= 2:  # 6 เดือน - 2 ปี
            stage_title = "🐱 Junior"
            stage_age = "6 เดือน - 2 ปี"
            stage_desc = "ช่วงวัยเด็ก เริ่มเข้าสู่วัยเจริญพันธุ์"
            stage_detail = """
            • แสดงลักษณะนิสัยเฉพาะตัว
            • เมื่ออายุ 1 ปี สามารถเปลี่ยนเป็นอาหารแมวโตได้
            • ควรทำหมันในช่วงนี้
            """
        elif 3 <= age <= 6:  # 3-6 ปี
            stage_title = "🐱 Prime"
            stage_age = "3 - 6 ปี"
            stage_desc = "ช่วงวัยรุ่น ร่างกายสมบูรณ์แข็งแรงที่สุด"
            stage_detail = """
            • ร่างกายอยู่ในสภาพที่สมบูรณ์ที่สุด
            • ควรตรวจสุขภาพกับสัตวแพทย์เป็นประจำ
            • ต้องการการออกกำลังกายสม่ำเสมอ
            """
        elif 7 <= age <= 10:  # 7-10 ปี
            stage_title = "🐱 Mature"
            stage_age = "7 - 10 ปี" 
            stage_desc = "ช่วงโตเต็มวัย อาจทำกิจกรรมน้อยลง"
            stage_detail = """
            • น้ำหนักอาจเพิ่มง่ายขึ้น
            • ควรเปลี่ยนสูตรอาหาร
            • ต้องการวิตามินเสริมภูมิคุ้มกัน
            """
        elif 11 <= age <= 14:  # 11-14 ปี
            stage_title = "🐱 Senior"
            stage_age = "11 - 14 ปี"
            stage_desc = "ช่วงสูงวัย มีความเสี่ยงสูงที่จะเจ็บป่วย"
            stage_detail = """
            • ควรพบสัตวแพทย์เป็นประจำ
            • ต้องการสารอาหารครบถ้วน
            • เฝ้าระวังโรคเรื้อรัง
            """
        else:  # 15 ปีขึ้นไป
            stage_title = "🐱 Geriatric"
            stage_age = "15 ปีขึ้นไป"
            stage_desc = "ช่วงวัยชรา ไม่ค่อยแอ็กทีฟ"
            stage_detail = """
            • ต้องการการดูแลเป็นพิเศษ
            • อาหารเฉพาะสำหรับแมวสูงวัย
            • ดูแลใกล้ชิดและเอาใจใส่
            """

        return f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                <h2 style='color: #B87333; margin-bottom: 5px;'>{stage_title}</h2>
                <h3 style='color: #8B4513; margin-top: 5px;'>อายุ: {stage_age}</h3>
            </div>
            
            <div style='margin: 15px 0; padding: 10px; background-color: rgba(184, 115, 51, 0.1); border-radius: 5px;'>
                <p style='color: #666; margin: 0;'>{stage_desc}</p>
            </div>
            
            <div style='margin-top: 15px;'>
                <p style='color: #B87333; font-weight: bold; margin-bottom: 10px;'>การดูแลที่เหมาะสม:</p>
                <div style='color: #666; padding-left: 10px;'>
                    {stage_detail.strip().replace('•', '&#8226;')}
                </div>
            </div>
        </div>
        """

    def calculate_bunny_age(self):
        """แสดงการคำนวณอายุกระต่าย"""
        bunny_age = self.spinBox_6.value()
        human_age = bunny_to_human_age(bunny_age)

        # กำหนดช่วงวัยตามอายุ 
        if bunny_age < 0.5:
            stage_title = "🐰 Baby Bunny"
            stage_age = "(0-6 เดือน)"
            stage_desc = "ช่วงวัยเด็ก ต้องการการดูแลเป็นพิเศษ"
            stage_detail = """
            • ต้องการนมแม่หรืออาหารทดแทนนมแม่
            • พัฒนาการเติบโตและการเรียนรู้
            • ต้องการความอบอุ่นและการดูแลใกล้ชิด
            • เริ่มฝึกการขับถ่ายและการกินอาหาร
            """
        elif 0.5 <= bunny_age <= 1:
            stage_title = "🐰 Young Bunny"
            stage_age = "(6 เดือน - 1 ปี)"
            stage_desc = "ช่วงวัยรุ่น พัฒนาบุคลิกภาพ"
            stage_detail = """
            • ควรทำหมันในช่วงนี้
            • มีพลังงานสูง ต้องการพื้นที่วิ่งเล่น
            • เริ่มแสดงพฤติกรรมทางสังคม
            • ต้องการการฝึกและการเข้าสังคม
            """
        elif 1 < bunny_age <= 6:
            stage_title = "🐰 Adult Bunny"
            stage_age = "(1-6 ปี)"
            stage_desc = "ช่วงวัยผู้ใหญ่ สมบูรณ์แข็งแรง"
            stage_detail = """
            • ควบคุมอาหารให้เหมาะสม
            • ต้องการการออกกำลังกายสม่ำเสมอ
            • ตรวจสุขภาพฟันและเล็บเป็นประจำ
            • สร้างกิจวัตรประจำวันที่แน่นอน
            """
        else:
            stage_title = "🐰 Senior Bunny"
            stage_age = "(6 ปีขึ้นไป)"
            stage_desc = "ช่วงวัยชรา ต้องการการดูแลใกล้ชิด"
            stage_detail = """
            • ตรวจสุขภาพบ่อยขึ้น
            • ปรับอาหารให้เหมาะกับวัย
            • ลดการออกกำลังกายหนักๆ
            • เฝ้าระวังโรคที่พบในวัยชรา
            """

        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🐰 ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุกระต่าย</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{bunny_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>การคำนวณอายุกระต่าย:</b><br>
                • 1 ปี เท่ากับ 21 ปีคน<br>
                • 2 ปี เท่ากับ 27 ปีคน<br>
                • อายุที่เพิ่มขึ้นแต่ละปี เท่ากับ 6 ปีคน<br>
                • สูงสุดประมาณ 16 ปี เท่ากับ 110 ปีคน
            </p>
            <hr style='border: 1px solid #B87333; margin: 15px 0;'>
            <h3 style='color: #B87333;'>⚠️ หมายเหตุ:</h3>
            <p style='font-size: 16px; margin: 10px 0;'>
                • อายุที่แท้จริงขึ้นอยู่กับสายพันธุ์<br>
                • กระต่ายพันธุ์เล็กมักอายุยืนกว่า<br>
                • การดูแลและสภาพแวดล้อมมีผลต่ออายุขัย
            </p>
        </div>
        """

        stage_info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                <h2 style='color: #B87333; margin-bottom: 5px;'>{stage_title}</h2>
                <h3 style='color: #8B4513; margin-top: 5px;'>{stage_age}</h3>
            </div>
            
            <div style='margin: 15px 0; padding: 10px; background-color: rgba(184, 115, 51, 0.1); border-radius: 5px;'>
                <p style='color: #666; margin: 0;'>{stage_desc}</p>
            </div>
            
            <div style='margin-top: 15px;'>
                <p style='color: #B87333; font-weight: bold; margin-bottom: 10px;'>การดูแลที่เหมาะสม:</p>
                <div style='color: #666; padding-left: 10px;'>
                    {stage_detail.strip().replace('•', '&#8226;')}
                </div>
            </div>
        </div>
        """

        self.textBrowser_14.setHtml(result)
        self.textBrowser_15.setHtml(info)
        self.textBrowser_16.setHtml(stage_info)

    def calculate_hamster_age(self):
        """แสดงการคำนวณอายุแฮมสเตอร์"""
        hamster_age = self.spinBox_4.value()
        human_age = hamster_to_human_age(hamster_age)
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🐹 ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุแฮมสเตอร์</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{hamster_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>การคำนวณอายุแฮมสเตอร์:</b><br>
                • 1 ปี เท่ากับ 41 ปีคน<br>
                • 1.5 ปี เท่ากับ 52.5 ปีคน<br>
                • 2 ปี เท่ากับ 63.5 ปีคน<br>
                • 2.5 ปี เท่ากับ 74.5 ปีคน<br>
                • 3 ปี เท่ากับ 80 ปีคน<br>
            </p>
            <hr style='border: 1px solid #B87333; margin: 15px 0;'>
            <h3 style='color: #B87333;'>⚠️ หมายเหตุ:</h3>
            <p style='font-size: 16px; margin: 10px 0;'>
                • แฮมสเตอร์มีอายุเฉลี่ย 2-3 ปี<br>
                • อายุที่แท้จริงอาจแตกต่างกันตามสายพันธุ์<br>
                • การดูแลและสภาพแวดล้อมมีผลต่ออายุขัย
            </p>
        </div>
        """

        stage_info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐹 ช่วงวัยของแฮมสเตอร์</h2>
            
            <div style='margin-top: 15px;'>
                <div style='border-left: 4px solid #B87333; padding-left: 15px; margin-bottom: 20px;'>
                    <h3 style='color: #B87333; margin-bottom: 5px;'>วัยเด็ก (0-3 เดือน)</h3>
                    <p style='color: #666;'>• ต้องการอาหารสำหรับลูกแฮมสเตอร์<br>
                    • เป็นช่วงที่เรียนรู้และปรับตัวกับสภาพแวดล้อม<br>
                    • ต้องการการดูแลเป็นพิเศษ</p>
                </div>
                
                <div style='border-left: 4px solid #B87333; padding-left: 15px; margin-bottom: 20px;'>
                    <h3 style='color: #B87333; margin-bottom: 5px;'>วัยรุ่น (3-6 เดือน)</h3>
                    <p style='color: #666;'>• เริ่มแสดงพฤติกรรมทางสังคม<br>
                    • มีพลังงานสูง ชอบสำรวจ<br>
                    • ควรเริ่มฝึกและเล่นกับเจ้าของ</p>
                </div>
                
                <div style='border-left: 4px solid #B87333; padding-left: 15px; margin-bottom: 20px;'>
                    <h3 style='color: #B87333; margin-bottom: 5px;'>โตเต็มวัย (6 เดือน - 1 ปี)</h3>
                    <p style='color: #666;'>• พัฒนาบุคลิกเฉพาะตัว<br>
                    • ควรได้รับอาหารที่สมดุล<br>
                    • ต้องการการออกกำลังกายสม่ำเสมอ</p>
                </div>
                
                <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                    <h3 style='color: #B87333; margin-bottom: 5px;'>วัยชรา (1 ปีขึ้นไป)</h3>
                    <p style='color: #666;'>• เคลื่อนไหวช้าลง<br>
                    • ต้องการอาหารสำหรับแฮมสเตอร์สูงอายุ<br>
                    • ควรได้รับการดูแลใกล้ชิด</p>
                </div>
            </div>
        </div>
        """

        self.textBrowser_8.setHtml(result)
        self.textBrowser_9.setHtml(info)
        self.textBrowser_10.setHtml(stage_info)

    def calculate_hedgehog_age(self):
        """แสดงการคำนวณอายุเม่น"""
        hedgehog_age = self.spinBox_5.value()
        human_age = hedgehog_to_human_age(hedgehog_age)
        
        # กำหนดช่วงวัยตามอายุ
        if hedgehog_age < 0.5:
            stage_title = "🦔 Baby Hedgehog"
            stage_age = "(0-6 เดือน)" 
            stage_desc = "ช่วงวัยเด็ก ต้องการการดูแลเป็นพิเศษ"
            stage_detail = """
            • ต้องการอาหารสำหรับลูกเม่น
            • เริ่มเรียนรู้สภาพแวดล้อม
            • ต้องการการดูแลอย่างใกล้ชิด
            • เริ่มแสดงพฤติกรรมการป้องกันตัว
            """
        elif 0.5 <= hedgehog_age <= 1:
            stage_title = "🦔 Young Hedgehog" 
            stage_age = "(6 เดือน - 1 ปี)"
            stage_desc = "ช่วงวัยรุ่น สำรวจและเรียนรู้"
            stage_detail = """
            • พัฒนาพฤติกรรมทางสังคม
            • มีพลังงานมาก ชอบสำรวจ
            • เริ่มแสดงบุคลิกชัดเจน
            • ควรเริ่มฝึกและสร้างความคุ้นเคย
            """
        elif 1 < hedgehog_age <= 4:
            stage_title = "🦔 Adult Hedgehog"
            stage_age = "(1-4 ปี)"
            stage_desc = "ช่วงวัยผู้ใหญ่ สมบูรณ์แข็งแรง"
            stage_detail = """
            • มีบุคลิกเฉพาะตัวชัดเจน
            • ควรได้รับอาหารที่เหมาะสม
            • ต้องการการออกกำลังกายสม่ำเสมอ
            • ควรมีกิจกรรมกระตุ้นความสนใจ
            """
        else:
            stage_title = "🦔 Senior Hedgehog"
            stage_age = "(4 ปีขึ้นไป)"
            stage_desc = "ช่วงวัยชรา ต้องการการดูแลใกล้ชิด"
            stage_detail = """
            • การเคลื่อนไหวช้าลง
            • ต้องการอาหารพิเศษสำหรับเม่นสูงอายุ
            • ควรตรวจสุขภาพสม่ำเสมอ
            • ต้องการการดูแลเอาใจใส่เป็นพิเศษ
            """

        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🦔 ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุเม่น</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{hedgehog_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>การคำนวณอายุเม่น:</b><br>
                • 1.17 ปี เท่ากับ 30 ปีคน<br>
                • 3 ปี เท่ากับ 40 ปีคน<br>
                • 3.5 ปี เท่ากับ 50 ปีคน<br>
                • 3.67 ปี เท่ากับ 60 ปีคน<br>
                • 4.17 ปี เท่ากับ 70 ปีคน<br>
                • 5.33 ปี เท่ากับ 80 ปีคน<br>
                • 6.17 ปี เท่ากับ 90 ปีคน<br>
                • 7.67 ปี เท่ากับ 100 ปีคน<br>
            </p>
            <hr style='border: 1px solid #B87333; margin: 15px 0;'>
            <h3 style='color: #B87333;'>⚠️ หมายเหตุ:</h3>
            <p style='font-size: 16px; margin: 10px 0;'>
                • เม่นมีอายุเฉลี่ย 4-6 ปี<br>
                • อายุขึ้นอยู่กับสายพันธุ์และการดูแล<br>
                • สภาพแวดล้อมมีผลต่ออายุขัย
            </p>
        </div>
        """

        stage_info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                <h2 style='color: #B87333; margin-bottom: 5px;'>{stage_title}</h2>
                <h3 style='color: #8B4513; margin-top: 5px;'>{stage_age}</h3>
            </div>
            
            <div style='margin: 15px 0; padding: 10px; background-color: rgba(184, 115, 51, 0.1); border-radius: 5px;'>
                <p style='color: #666; margin: 0;'>{stage_desc}</p>
            </div>
            
            <div style='margin-top: 15px;'>
                <p style='color: #B87333; font-weight: bold; margin-bottom: 10px;'>การดูแลที่เหมาะสม:</p>
                <div style='color: #666; padding-left: 10px;'>
                    {stage_detail.strip().replace('•', '&#8226;')}
                </div>
            </div>
        </div>
        """

        self.textBrowser_11.setHtml(result)
        self.textBrowser_12.setHtml(info)
        self.textBrowser_13.setHtml(stage_info)

    def calculate_squirrel_age(self):
        """แสดงการคำนวณอายุกระรอก"""
        squirrel_age = self.spinBox_7.value()
        human_age = squirrel_to_human_age(squirrel_age)

        # กำหนดช่วงวัยตามอายุ 
        if squirrel_age < 0.5:
            stage_title = "🐿️ Baby Squirrel"
            stage_age = "(0-6 เดือน)"
            stage_desc = "ช่วงวัยเด็ก ต้องการการดูแลใกล้ชิด"
            stage_detail = """
            • ต้องการนมหรืออาหารทดแทนนม
            • การดูแลความอบอุ่นเป็นพิเศษ
            • พัฒนาการด้านการเคลื่อนไหว
            • เริ่มฝึกการกินอาหารแข็ง
            """
        elif 0.5 <= squirrel_age <= 1:
            stage_title = "🐿️ Young Squirrel"
            stage_age = "(6 เดือน - 1 ปี)"
            stage_desc = "ช่วงวัยรุ่น เริ่มเป็นตัวของตัวเอง"
            stage_detail = """
            • ซุกซนและมีพลังงานสูง
            • ต้องการพื้นที่ออกกำลังกาย
            • เริ่มแสดงนิสัยเฉพาะตัว
            • ฝึกทักษะการปีนป่ายและกระโดด
            """
        elif 1 < squirrel_age <= 10:
            stage_title = "🐿️ Adult Squirrel"
            stage_age = "(1-10 ปี)"
            stage_desc = "ช่วงวัยผู้ใหญ่ แข็งแรงสมบูรณ์"
            stage_detail = """
            • ควบคุมอาหารให้เหมาะสม
            • ต้องการการออกกำลังกายประจำ
            • สร้างกิจวัตรที่แน่นอน
            • ตรวจสุขภาพเป็นระยะ
            """
        else:
            stage_title = "🐿️ Senior Squirrel"
            stage_age = "(10 ปีขึ้นไป)"
            stage_desc = "ช่วงวัยชรา ต้องการการดูแลพิเศษ"
            stage_detail = """
            • ตรวจสุขภาพบ่อยขึ้น
            • ปรับอาหารให้เหมาะกับวัย
            • เฝ้าระวังโรคในวัยชรา
            • ลดกิจกรรมที่หนักเกินไป
            """

        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333; text-align: center;'>🐿️ ผลการคำนวณ</h2>
            <div style='display: flex; justify-content: space-between; margin-top: 55px;'>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0;'>
                        <b>อายุกระรอก</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{squirrel_age}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
                <div style='flex: 1; text-align: center; padding: 10px; border-radius: 8px;'>
                    <p style='font-size: 16px; margin: 5px 0; margin-top: 35px;'>
                        <b>เทียบเท่าอายุคน</b><br>
                        <span style='font-size: 44px; color: #B87333;'>{human_age:.1f}</span>
                        <span style='font-size: 34px;'> ปี</span>
                    </p>
                </div>
            </div>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>การคำนวณอายุกระรอก:</b><br>
                • 1 ปี เท่ากับ 8.89 ปีคน<br>
                • 5 ปี เท่ากับ 44.45 ปีคน<br>
                • 10 ปี เท่ากับ 88.9 ปีคน<br>
                • 20 ปี เท่ากับ 177.8 ปีคน<br>
                • สูงสุดประมาณ 23 ปี เท่ากับ 204 ปีคน
            </p>
            <hr style='border: 1px solid #B87333; margin: 15px 0;'>
            <h3 style='color: #B87333;'>⚠️ หมายเหตุ:</h3>
            <p style='font-size: 16px; margin: 10px 0;'>
                • กระรอกในธรรมชาติมีอายุ 6-12 ปี<br>
                • การเลี้ยงดูที่ดีทำให้อายุยืนขึ้น<br>
                • สภาพแวดล้อมมีผลต่ออายุขัย
            </p>
        </div>
        """

        stage_info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <div style='border-left: 4px solid #B87333; padding-left: 15px;'>
                <h2 style='color: #B87333; margin-bottom: 5px;'>{stage_title}</h2>
                <h3 style='color: #8B4513; margin-top: 5px;'>{stage_age}</h3>
            </div>
            
            <div style='margin: 15px 0; padding: 10px; background-color: rgba(184, 115, 51, 0.1); border-radius: 5px;'>
                <p style='color: #666; margin: 0;'>{stage_desc}</p>
            </div>
            
            <div style='margin-top: 15px;'>
                <p style='color: #B87333; font-weight: bold; margin-bottom: 10px;'>การดูแลที่เหมาะสม:</p>
                <div style='color: #666; padding-left: 10px;'>
                    {stage_detail.strip().replace('•', '&#8226;')}
                </div>
            </div>
        </div>
        """

        self.textBrowser_17.setHtml(result)
        self.textBrowser_18.setHtml(info)
        self.textBrowser_19.setHtml(stage_info)
        
    def exit_application(self):
        """ปุ่มออกโปรแกรม"""
        QtWidgets.QApplication.quit()

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.widget_2.hide()
    ui.pushButton_3.setChecked(True)
    ui.widget.show()
    ui.pushButton_9.setChecked(True)
    MainWindow.show()
    sys.exit(app.exec_())
