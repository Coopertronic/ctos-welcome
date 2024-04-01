# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import subprocess
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 389)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_title = QHBoxLayout()
        self.main_title.setObjectName(u"main_title")
        self.main_title_logo = QLabel(self.centralwidget)
        self.main_title_logo.setObjectName(u"main_title_logo")
        self.main_title_logo.setPixmap(QPixmap(u"../../Pictures/Coopertronics/Cutting_Room/Dragon.greenWhite.2024.square.png"))

        self.main_title.addWidget(self.main_title_logo)

        self.main_title_head = QLabel(self.centralwidget)
        self.main_title_head.setObjectName(u"main_title_head")
        font = QFont()
        font.setFamilies([u"Sunflower Light"])
        font.setPointSize(36)
        self.main_title_head.setFont(font)
        self.main_title_head.setAlignment(Qt.AlignCenter)

        self.main_title.addWidget(self.main_title_head)


        self.verticalLayout.addLayout(self.main_title)

        self.thBtns = QGroupBox(self.centralwidget)
        self.thBtns.setObjectName(u"thBtns")
        font1 = QFont()
        font1.setFamilies([u"Sunflower Medium"])
        font1.setPointSize(16)
        self.thBtns.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.thBtns)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_grid = QGridLayout()
        self.btn_grid.setObjectName(u"btn_grid")
        self.btn_help = QPushButton(self.thBtns)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMaximumSize(QSize(250, 42))
        font2 = QFont()
        font2.setFamilies([u"Sunflower Medium"])
        font2.setPointSize(14)
        self.btn_help.setFont(font2)

        self.btn_grid.addWidget(self.btn_help, 0, 1, 1, 1)

        self.btn_home = QPushButton(self.thBtns)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.clicked.connect(self.btn_home_action)
        self.btn_home.setMaximumSize(QSize(250, 42))
        self.btn_home.setFont(font2)

        self.btn_grid.addWidget(self.btn_home, 1, 1, 1, 1)

        self.btn_surgest = QPushButton(self.thBtns)
        self.btn_surgest.setObjectName(u"btn_surgest")
        self.btn_surgest.setMaximumSize(QSize(250, 42))
        self.btn_surgest.setFont(font2)

        self.btn_grid.addWidget(self.btn_surgest, 2, 0, 1, 1)

        self.btn_settings = QPushButton(self.thBtns)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMaximumSize(QSize(250, 42))
        self.btn_settings.setFont(font2)

        self.btn_grid.addWidget(self.btn_settings, 2, 2, 1, 1)

        self.btn_how = QPushButton(self.thBtns)
        self.btn_how.setObjectName(u"btn_how")
        self.btn_how.setMaximumSize(QSize(250, 42))
        self.btn_how.setFont(font2)

        self.btn_grid.addWidget(self.btn_how, 2, 1, 1, 1)

        self.btn_install = QPushButton(self.thBtns)
        self.btn_install.setObjectName(u"btn_install")
        self.btn_install.setMaximumSize(QSize(250, 42))
        self.btn_install.setFont(font2)

        self.btn_grid.addWidget(self.btn_install, 0, 2, 1, 1)

        self.btn_about = QPushButton(self.thBtns)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMaximumSize(QSize(250, 42))
        self.btn_about.setFont(font2)

        self.btn_grid.addWidget(self.btn_about, 0, 0, 1, 1)

        self.btn_setup = QPushButton(self.thBtns)
        self.btn_setup.setObjectName(u"btn_setup")
        self.btn_setup.setMaximumSize(QSize(250, 42))
        self.btn_setup.setFont(font2)

        self.btn_grid.addWidget(self.btn_setup, 1, 2, 1, 1)

        self.btn_tour = QPushButton(self.thBtns)
        self.btn_tour.setObjectName(u"btn_tour")
        self.btn_tour.setMaximumSize(QSize(250, 42))
        self.btn_tour.setFont(font2)

        self.btn_grid.addWidget(self.btn_tour, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.btn_grid)


        self.verticalLayout.addWidget(self.thBtns)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    def btn_home_action(self):
        print("HOME PAGE button pressed")
        subprocess.run(["xdg-open","https://coopertronic.co.uk/"])

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_title_logo.setText("")
        self.main_title_head.setText(QCoreApplication.translate("MainWindow", u"Welcome to Coopertronic OS", None))
        self.thBtns.setTitle(QCoreApplication.translate("MainWindow", u"Explore Coopertronic OS", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.btn_surgest.setText(QCoreApplication.translate("MainWindow", u"Surgestions", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_how.setText(QCoreApplication.translate("MainWindow", u"How To", None))
        self.btn_install.setText(QCoreApplication.translate("MainWindow", u"Install Apps", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_setup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.btn_tour.setText(QCoreApplication.translate("MainWindow", u"Guided Tour", None))
    # retranslateUi

