# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formFWtBuR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1023, 627)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"\n"
"QScrollBar:vertical {\n"
"	border:none;\n"
"	\n"
"	background-color: rgb(102, 102, 102);\n"
"	width:14px;\n"
"	margin: 15px 0 15px 0;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	width:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(79, 79, 79);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(255, 1, 69);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background-color: rgb(140, 0, 42);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u0432\u0435\u0440\u0445-\u0432\u043d\u0438\u0437 */\n"
"\n"
"\n"
"/* \u0412\u0435\u0440\u0445\u043d\u044f\u044f */\n"
"QScrollBar::sub-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height:15px;\n"
"	border-top-left-raduis:7px;\n"
"	border-top-right-radius:7px;\n"
"	subcontrol-"
                        "position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	background-color: rgb(255, 1, 69);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	\n"
"	background-color: rgb(140, 0, 42);\n"
"}\n"
"\n"
"/* \u041d\u0438\u0436\u043d\u044f\u044f */\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height:15px;\n"
"	border-bottom-left-raduis:7px;\n"
"	border-bottom-right-radius:7px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"	background-color: rgb(255, 1, 69);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"	\n"
"	background-color: rgb(140, 0, 42);\n"
"}\n"
"\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043f\u043e\u043b\u043e\u0441\u043e\u043a */\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"	background:none;\n"
"\n"
"}\n"
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e"
                        "\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"\n"
"QScrollBar:vertical {\n"
"	border:none;\n"
"	background-color: rgb(102, 102, 102);\n"
"	width:14px;\n"
"	margin: 15px 0 15px 0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_Bar = QFrame(self.centralwidget)
        self.top_Bar.setObjectName(u"top_Bar")
        self.top_Bar.setMaximumSize(QSize(16777215, 40))
        self.top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_Bar.setFrameShape(QFrame.NoFrame)
        self.top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(150, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(61, 145, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_toggle = QPushButton(self.frame_toggle)
        self.Btn_toggle.setObjectName(u"Btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_toggle.sizePolicy().hasHeightForWidth())
        self.Btn_toggle.setSizePolicy(sizePolicy)
        self.Btn_toggle.setMinimumSize(QSize(150, 0))
        self.Btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.Btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(150, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.Btn_Menu_2 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setObjectName(u"Btn_Menu_2")
        self.Btn_Menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"pictures/acoustic_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Menu_2.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.Btn_Menu_2)

        self.Btn_Menu_1 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setObjectName(u"Btn_Menu_1")
        self.Btn_Menu_1.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"pictures/electric_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Menu_1.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.Btn_Menu_1)

        self.Btn_Menu_3 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setObjectName(u"Btn_Menu_3")
        sizePolicy.setHeightForWidth(self.Btn_Menu_3.sizePolicy().hasHeightForWidth())
        self.Btn_Menu_3.setSizePolicy(sizePolicy)
        self.Btn_Menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"pictures/bass_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Menu_3.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.Btn_Menu_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.frame_contact_section = QFrame(self.frame_left_menu)
        self.frame_contact_section.setObjectName(u"frame_contact_section")
        sizePolicy.setHeightForWidth(self.frame_contact_section.sizePolicy().hasHeightForWidth())
        self.frame_contact_section.setSizePolicy(sizePolicy)
        self.frame_contact_section.setMinimumSize(QSize(0, 0))
        self.frame_contact_section.setStyleSheet(u"")
        self.frame_contact_section.setFrameShape(QFrame.NoFrame)
        self.frame_contact_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_contact_section)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.checkBox_muz = QCheckBox(self.frame_contact_section)
        self.checkBox_muz.setObjectName(u"checkBox_muz")
        self.checkBox_muz.setStyleSheet(u"color:white;\n"
"font-size:13px;\n"
"margin-left:40px;")

        self.verticalLayout_6.addWidget(self.checkBox_muz, 0, Qt.AlignLeft)

        self.checkBox_skif = QCheckBox(self.frame_contact_section)
        self.checkBox_skif.setObjectName(u"checkBox_skif")
        self.checkBox_skif.setStyleSheet(u"color:white;\n"
"font-size:13px;\n"
"margin-left:40px;")

        self.verticalLayout_6.addWidget(self.checkBox_skif, 0, Qt.AlignLeft)

        self.checkBox_pop = QCheckBox(self.frame_contact_section)
        self.checkBox_pop.setObjectName(u"checkBox_pop")
        self.checkBox_pop.setStyleSheet(u"color:white;\n"
"font-size:13px;\n"
"margin-left:40px;\n"
"margin-bottom:10px;")

        self.verticalLayout_6.addWidget(self.checkBox_pop, 0, Qt.AlignLeft)

        self.but_instr = QPushButton(self.frame_contact_section)
        self.but_instr.setObjectName(u"but_instr")
        sizePolicy.setHeightForWidth(self.but_instr.sizePolicy().hasHeightForWidth())
        self.but_instr.setSizePolicy(sizePolicy)
        self.but_instr.setMinimumSize(QSize(0, 40))
        self.but_instr.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 145, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_instr.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.but_instr)

        self.button_author = QPushButton(self.frame_contact_section)
        self.button_author.setObjectName(u"button_author")
        self.button_author.setMinimumSize(QSize(0, 40))
        self.button_author.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 145, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_author.setIcon(icon5)

        self.verticalLayout_6.addWidget(self.button_author)

        self.version = QLabel(self.frame_contact_section)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color:white;\n"
"font-size: 15px;")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.version)


        self.verticalLayout_3.addWidget(self.frame_contact_section, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.Pages_Widget.setFrameShape(QFrame.NoFrame)
        self.page_loading = QWidget()
        self.page_loading.setObjectName(u"page_loading")
        self.horizontalLayout_6 = QHBoxLayout(self.page_loading)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_loading)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.loading_bar = QLabel(self.frame_2)
        self.loading_bar.setObjectName(u"loading_bar")
        self.loading_bar.setStyleSheet(u"color:white;\n"
"font-size:50px;")

        self.horizontalLayout_7.addWidget(self.loading_bar, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.Pages_Widget.addWidget(self.page_loading)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.verticalLayout_20 = QVBoxLayout(self.page_add)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_add)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.back_but_2 = QPushButton(self.frame_6)
        self.back_but_2.setObjectName(u"back_but_2")
        self.back_but_2.setMaximumSize(QSize(100, 16777215))
        self.back_but_2.setCursor(QCursor(Qt.CrossCursor))
        self.back_but_2.setStyleSheet(u"color:white;\n"
"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back_but_2.setIcon(icon6)
        self.back_but_2.setIconSize(QSize(35, 35))

        self.verticalLayout_21.addWidget(self.back_but_2)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:white;\n"
"font-size:20px;")

        self.verticalLayout_21.addWidget(self.label_2)

        self.comboBox_name = QComboBox(self.frame_6)
        self.comboBox_name.setObjectName(u"comboBox_name")
        self.comboBox_name.setMaximumSize(QSize(700, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.comboBox_name.setFont(font)
        self.comboBox_name.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_21.addWidget(self.comboBox_name)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:white;\n"
"font-size:20px;")

        self.verticalLayout_21.addWidget(self.label_8)

        self.muztorg_add = QLineEdit(self.frame_6)
        self.muztorg_add.setObjectName(u"muztorg_add")
        self.muztorg_add.setMaximumSize(QSize(700, 16777215))
        self.muztorg_add.setFont(font)
        self.muztorg_add.setStyleSheet(u"background-color:white;")
        self.muztorg_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.muztorg_add)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:white;\n"
"font-size:20px;")

        self.verticalLayout_21.addWidget(self.label_9)

        self.skif_add = QLineEdit(self.frame_6)
        self.skif_add.setObjectName(u"skif_add")
        self.skif_add.setMaximumSize(QSize(700, 16777215))
        self.skif_add.setFont(font)
        self.skif_add.setStyleSheet(u"background-color:white;")
        self.skif_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.skif_add)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:white;\n"
"font-size:20px;")

        self.verticalLayout_21.addWidget(self.label_10)

        self.pop_add = QLineEdit(self.frame_6)
        self.pop_add.setObjectName(u"pop_add")
        self.pop_add.setMaximumSize(QSize(700, 16777215))
        self.pop_add.setFont(font)
        self.pop_add.setStyleSheet(u"background-color:white;")
        self.pop_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.pop_add)

        self.but_img = QPushButton(self.frame_6)
        self.but_img.setObjectName(u"but_img")
        self.but_img.setMaximumSize(QSize(200, 16777215))
        self.but_img.setFont(font)
        self.but_img.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	margin-top:12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(105, 75, 255);\n"
"}")

        self.verticalLayout_21.addWidget(self.but_img)

        self.check_img = QCheckBox(self.frame_6)
        self.check_img.setObjectName(u"check_img")
        self.check_img.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.check_img.setFont(font1)
        self.check_img.setStyleSheet(u"margin-left: 40px;\n"
"margin-top: 10px;\n"
"color:white;")

        self.verticalLayout_21.addWidget(self.check_img)

        self.but_find = QPushButton(self.frame_6)
        self.but_find.setObjectName(u"but_find")
        self.but_find.setFont(font)
        self.but_find.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	margin-top:12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 145, 255);\n"
"}")

        self.verticalLayout_21.addWidget(self.but_find)

        self.but_add_g = QPushButton(self.frame_6)
        self.but_add_g.setObjectName(u"but_add_g")
        self.but_add_g.setFont(font)
        self.but_add_g.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	margin-top:12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 145, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"pictures/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_add_g.setIcon(icon7)

        self.verticalLayout_21.addWidget(self.but_add_g)


        self.verticalLayout_20.addWidget(self.frame_6)

        self.Pages_Widget.addWidget(self.page_add)
        self.page_table_parce = QWidget()
        self.page_table_parce.setObjectName(u"page_table_parce")
        self.verticalLayout_15 = QVBoxLayout(self.page_table_parce)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_table_parce)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 100))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.back_but = QPushButton(self.header)
        self.back_but.setObjectName(u"back_but")
        self.back_but.setMaximumSize(QSize(100, 16777215))
        self.back_but.setCursor(QCursor(Qt.CrossCursor))
        self.back_but.setStyleSheet(u"color:white;\n"
"border:none;")
        self.back_but.setIcon(icon6)
        self.back_but.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.back_but)

        self.label_7 = QLabel(self.header)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(18)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color:white")
        self.label_7.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_16.addWidget(self.header)

        self.table_and_buttons = QFrame(self.frame)
        self.table_and_buttons.setObjectName(u"table_and_buttons")
        self.table_and_buttons.setMaximumSize(QSize(850, 16777215))
        self.table_and_buttons.setFrameShape(QFrame.StyledPanel)
        self.table_and_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.table_and_buttons)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.table_and_buttons)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(1000, 16777215))
        self.tableWidget.setStyleSheet(u"background-color:white;")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.label_guitar = QLabel(self.table_and_buttons)
        self.label_guitar.setObjectName(u"label_guitar")
        self.label_guitar.setMinimumSize(QSize(300, 0))
        self.label_guitar.setPixmap(QPixmap(u"guitars/FENDER SQUIER BULLET TREM BSB.png"))
        self.label_guitar.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_guitar)


        self.verticalLayout_16.addWidget(self.table_and_buttons)

        self.but_export = QPushButton(self.frame)
        self.but_export.setObjectName(u"but_export")
        self.but_export.setMinimumSize(QSize(0, 40))
        self.but_export.setStyleSheet(u"QPushButton {\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 145, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../Downloads/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_export.setIcon(icon8)

        self.verticalLayout_16.addWidget(self.but_export)


        self.verticalLayout_15.addWidget(self.frame)

        self.Pages_Widget.addWidget(self.page_table_parce)
        self.page_instruction = QWidget()
        self.page_instruction.setObjectName(u"page_instruction")
        self.verticalLayout_13 = QVBoxLayout(self.page_instruction)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_instruction)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border:none;")

        self.verticalLayout_18.addWidget(self.textEdit)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.Pages_Widget.addWidget(self.page_instruction)
        self.page_start = QWidget()
        self.page_start.setObjectName(u"page_start")
        self.verticalLayout_12 = QVBoxLayout(self.page_start)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_start = QFrame(self.page_start)
        self.frame_start.setObjectName(u"frame_start")
        self.frame_start.setFrameShape(QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_start)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 10, 261, 141))
        self.label_5.setStyleSheet(u"color:white;\n"
"font-size: 20px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_start)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 100, 711, 141))
        self.label_6.setStyleSheet(u"color:white;\n"
"font-size: 20px;")

        self.verticalLayout_12.addWidget(self.frame_start)

        self.Pages_Widget.addWidget(self.page_start)
        self.page_author = QWidget()
        self.page_author.setObjectName(u"page_author")
        self.verticalLayout_10 = QVBoxLayout(self.page_author)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_author = QFrame(self.page_author)
        self.frame_author.setObjectName(u"frame_author")
        self.frame_author.setFrameShape(QFrame.StyledPanel)
        self.frame_author.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_author)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 0, 0, 0)
        self.frame_au_top = QFrame(self.frame_author)
        self.frame_au_top.setObjectName(u"frame_au_top")
        self.frame_au_top.setFrameShape(QFrame.StyledPanel)
        self.frame_au_top.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_au_top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, -100, 731, 331))
        self.label_3.setStyleSheet(u"color:white;\n"
"font-size:20px;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.frame_au_top)

        self.label_4 = QLabel(self.frame_author)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
"font-size:20px")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.frame_au_bottom = QFrame(self.frame_author)
        self.frame_au_bottom.setObjectName(u"frame_au_bottom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_au_bottom.sizePolicy().hasHeightForWidth())
        self.frame_au_bottom.setSizePolicy(sizePolicy1)
        self.frame_au_bottom.setMinimumSize(QSize(700, 0))
        self.frame_au_bottom.setMaximumSize(QSize(1067, 16777215))
        self.frame_au_bottom.setStyleSheet(u"")
        self.frame_au_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_au_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_au_bottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vk_but = QPushButton(self.frame_au_bottom)
        self.vk_but.setObjectName(u"vk_but")
        self.vk_but.setMaximumSize(QSize(200, 16777215))
        self.vk_but.setCursor(QCursor(Qt.OpenHandCursor))
        self.vk_but.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"pictures/vk-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vk_but.setIcon(icon9)
        self.vk_but.setIconSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.vk_but)

        self.telega_but = QPushButton(self.frame_au_bottom)
        self.telega_but.setObjectName(u"telega_but")
        self.telega_but.setMaximumSize(QSize(200, 16777215))
        self.telega_but.setCursor(QCursor(Qt.OpenHandCursor))
        self.telega_but.setStyleSheet(u"border:none;")
        icon10 = QIcon()
        icon10.addFile(u"pictures/telega.png", QSize(), QIcon.Normal, QIcon.Off)
        self.telega_but.setIcon(icon10)
        self.telega_but.setIconSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.telega_but)

        self.but_mail = QPushButton(self.frame_au_bottom)
        self.but_mail.setObjectName(u"but_mail")
        font3 = QFont()
        font3.setPointSize(15)
        self.but_mail.setFont(font3)
        self.but_mail.setCursor(QCursor(Qt.OpenHandCursor))
        self.but_mail.setStyleSheet(u"QPushButton{ \n"
"	color:white;\n"
"border:none;\n"
"}")

        self.horizontalLayout_3.addWidget(self.but_mail)


        self.verticalLayout_11.addWidget(self.frame_au_bottom, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.frame_author)

        self.Pages_Widget.addWidget(self.page_author)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Pages_Widget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 2000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 2000))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.grid_acoustic = QFrame(self.scrollAreaWidgetContents)
        self.grid_acoustic.setObjectName(u"grid_acoustic")
        self.grid_acoustic.setEnabled(True)
        self.grid_acoustic.setMinimumSize(QSize(1000, 1200))
        self.grid_acoustic.setMaximumSize(QSize(9999999, 16777215))
        self.grid_acoustic.setStyleSheet(u"")
        self.grid_acoustic.setFrameShape(QFrame.NoFrame)
        self.grid_acoustic.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.grid_acoustic)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 30, 741, 1411))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.grid_acoustic)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_bass = QWidget()
        self.page_bass.setObjectName(u"page_bass")
        self.verticalLayout_9 = QVBoxLayout(self.page_bass)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.page_bass)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.scrollArea_2 = QScrollArea(self.frame_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 853, 567))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -408, 1000, 1200))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.grid_bass = QFrame(self.scrollAreaWidgetContents_2)
        self.grid_bass.setObjectName(u"grid_bass")
        self.grid_bass.setEnabled(True)
        self.grid_bass.setMinimumSize(QSize(1000, 1200))
        self.grid_bass.setMaximumSize(QSize(9999999, 16777215))
        self.grid_bass.setStyleSheet(u"")
        self.grid_bass.setFrameShape(QFrame.NoFrame)
        self.grid_bass.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.grid_bass)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(50, 30, 741, 802))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.grid_bass)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.frame_5)

        self.Pages_Widget.addWidget(self.page_bass)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_17 = QVBoxLayout(self.page_4)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_3)

        self.Pages_Widget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 90, 341, 191))
        self.label.setStyleSheet(u"color:white;\n"
"font-size:40px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.scrollArea_3 = QScrollArea(self.page_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 853, 567))
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -419, 1000, 1200))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.grid_electro = QFrame(self.scrollAreaWidgetContents_3)
        self.grid_electro.setObjectName(u"grid_electro")
        self.grid_electro.setEnabled(True)
        self.grid_electro.setMinimumSize(QSize(1000, 1200))
        self.grid_electro.setMaximumSize(QSize(9999999, 16777215))
        self.grid_electro.setStyleSheet(u"")
        self.grid_electro.setFrameShape(QFrame.NoFrame)
        self.grid_electro.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.grid_electro)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 30, 741, 802))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.grid_electro)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.Pages_Widget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_toggle.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u041d\u042e", None))
#if QT_CONFIG(tooltip)
        self.Btn_Menu_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0443\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435", None))
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0433\u0438\u0442\u0430\u0440\u044b", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441-\u0433\u0438\u0442\u0430\u0440\u044b     ", None))
        self.checkBox_muz.setText(QCoreApplication.translate("MainWindow", u"Muztorg", None))
        self.checkBox_skif.setText(QCoreApplication.translate("MainWindow", u"SkfiMusic", None))
        self.checkBox_pop.setText(QCoreApplication.translate("MainWindow", u"PopMusic", None))
        self.but_instr.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.button_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"V 1.0", None))
        self.loading_bar.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u041a\u0410..............", None))
        self.back_but_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u043c\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 MuzTorg", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 SkifMusic", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 PopMusic", None))
        self.but_img.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.check_img.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e", None))
        self.but_find.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.but_add_g.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.back_but.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430", None));
        self.label_guitar.setText("")
        self.but_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 JSON", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">      \u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u0438</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">1. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0443\u044e \u0432\u0430\u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0438 \u0442\u043e\u0432\u0430\u0440.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">2. \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u0412\u044b\u0431\u043e\u0440&quot; \u0438 \u0434\u043e\u0436\u0434\u0438\u0442\u0435"
                        "\u0441\u044c \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 \u0441\u0431\u043e\u0440\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c \u0442\u043e\u0432\u0430\u0440\u0435.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">3. \u0412 \u0442\u0430\u0431\u043b\u0438\u0446\u0435, \u0433\u0434\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0446\u0435\u043d\u0430\u0445 \u0438 \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0435, \u0432\u044b\u0431\u0435\u0440\u0438\u0442"
                        "\u0435 \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0439 \u0432\u0430\u043c \u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u0438 \u043f\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u044e \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041f\u0435\u0440\u0435\u0439\u0442\u0438&quot; \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043a\u0440\u044b\u0442\u0430 WEB-\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437 . \u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u044f \u0441\u0441\u044b\u043b\u043a\u0438 \u043d\u0430 \u0442\u043e\u0432\u0430\u0440 \u0432 \u043e\u0434\u043d\u043e\u043c \u0438\u0437 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432, \u0432 \u0442\u0430\u0431"
                        "\u043b\u0438\u0446\u0443 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u0441\u044f &quot;empty&quot; \u0438 \u043a\u043d\u043e\u043f\u043a\u0430 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0442\u043e\u0432\u0430\u0440\u0430 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">4. \u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043c\u043e\u0436\u043d\u043e \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 JSON-\u0444\u0430\u0439\u043b,"
                        " \u043d\u0430\u0436\u0430\u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0438 \u0442\u043e\u0432\u0430\u0440, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u0430\u0441 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u0435\u0442.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u043a\u0443\u0440\u0441\u0430\u043d\u0442\u043e\u043c 431 \u0433\u0440\u0443\u043f\u043f\u044b \u0427\u0435\u0440\u043d\u0438\u043a\u043e\u0432\u044b\u043c \u0421.\u0421. \u0432 \u0446\u0435\u043b\u044f\u0445 \u0441\u0431\u043e\u0440\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u0430\u0445", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0441\u0432\u044f\u0437\u0438 \u0441 \u0430\u0432\u0442\u043e\u0440\u043e\u043c", None))
        self.vk_but.setText("")
        self.telega_but.setText("")
        self.but_mail.setText(QCoreApplication.translate("MainWindow", u"svyat_developer@mail.ru", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0433\u0438\u0442\u0430\u0440\u044b", None))
    # retranslateUi

