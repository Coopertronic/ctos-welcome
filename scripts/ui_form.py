# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        MainWindow.resize(805, 389)
        icon = QIcon()
        icon.addFile(u"assets/org.dragonWG.dragonWG.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_title = QHBoxLayout()
        self.main_title.setObjectName(u"main_title")
        self.main_title_logo = QLabel(self.centralwidget)
        self.main_title_logo.setObjectName(u"main_title_logo")
        self.main_title_logo.setMaximumSize(QSize(300, 300))
        self.main_title_logo.setPixmap(QPixmap(u"assets/Dragon.greenWhite.2024.square.png"))
        self.main_title_logo.setAlignment(Qt.AlignCenter)

        self.main_title.addWidget(self.main_title_logo)

        self.main_title_head = QLabel(self.centralwidget)
        self.main_title_head.setObjectName(u"main_title_head")
        self.main_title_head.setMaximumSize(QSize(1200, 400))
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
        self.thBtns.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.thBtns)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_grid = QGridLayout()
        self.btn_grid.setObjectName(u"btn_grid")
        self.btn_tour = QPushButton(self.thBtns)
        self.btn_tour.setObjectName(u"btn_tour")
        self.btn_tour.setMaximumSize(QSize(250, 42))
        font2 = QFont()
        font2.setFamilies([u"Sunflower Medium"])
        font2.setPointSize(14)
        self.btn_tour.setFont(font2)
        self.btn_tour.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_tour, 2, 0, 1, 1)

        self.btn_about = QPushButton(self.thBtns)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMaximumSize(QSize(250, 42))
        self.btn_about.setFont(font2)
        self.btn_about.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_about, 1, 0, 1, 1)

        self.btn_home = QPushButton(self.thBtns)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(250, 42))
        self.btn_home.setFont(font2)
        self.btn_home.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_home, 2, 1, 1, 1)

        self.btn_setup = QPushButton(self.thBtns)
        self.btn_setup.setObjectName(u"btn_setup")
        self.btn_setup.setMaximumSize(QSize(250, 42))
        self.btn_setup.setFont(font2)
        self.btn_setup.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_setup, 2, 2, 1, 1)

        self.btn_help = QPushButton(self.thBtns)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMaximumSize(QSize(250, 42))
        self.btn_help.setFont(font2)
        self.btn_help.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_help, 1, 1, 1, 1)

        self.btn_how = QPushButton(self.thBtns)
        self.btn_how.setObjectName(u"btn_how")
        self.btn_how.setMaximumSize(QSize(250, 42))
        self.btn_how.setFont(font2)
        self.btn_how.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_how, 3, 1, 1, 1)

        self.btn_install = QPushButton(self.thBtns)
        self.btn_install.setObjectName(u"btn_install")
        self.btn_install.setMaximumSize(QSize(250, 42))
        self.btn_install.setFont(font2)
        self.btn_install.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_install, 1, 2, 1, 1)

        self.btn_surgest = QPushButton(self.thBtns)
        self.btn_surgest.setObjectName(u"btn_surgest")
        self.btn_surgest.setMaximumSize(QSize(250, 42))
        self.btn_surgest.setFont(font2)
        self.btn_surgest.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_surgest, 3, 0, 1, 1)

        self.btn_settings = QPushButton(self.thBtns)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMaximumSize(QSize(250, 42))
        self.btn_settings.setFont(font2)
        self.btn_settings.setToolTipDuration(0)

        self.btn_grid.addWidget(self.btn_settings, 3, 2, 1, 1)

        self.col_examine = QLabel(self.thBtns)
        self.col_examine.setObjectName(u"col_examine")
        font3 = QFont()
        font3.setFamilies([u"Sunflower"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setUnderline(True)
        self.col_examine.setFont(font3)
        self.col_examine.setAlignment(Qt.AlignCenter)

        self.btn_grid.addWidget(self.col_examine, 0, 0, 1, 1)

        self.col_learn = QLabel(self.thBtns)
        self.col_learn.setObjectName(u"col_learn")
        self.col_learn.setFont(font3)
        self.col_learn.setAlignment(Qt.AlignCenter)

        self.btn_grid.addWidget(self.col_learn, 0, 1, 1, 1)

        self.col_custom = QLabel(self.thBtns)
        self.col_custom.setObjectName(u"col_custom")
        self.col_custom.setFont(font3)
        self.col_custom.setAlignment(Qt.AlignCenter)

        self.btn_grid.addWidget(self.col_custom, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.btn_grid)


        self.verticalLayout.addWidget(self.thBtns)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.main_title_logo.setText("")
        self.main_title_head.setText(QCoreApplication.translate("MainWindow", u"Welcome to Coopertronic OS", None))
        self.thBtns.setTitle(QCoreApplication.translate("MainWindow", u"Explore Coopertronic OS", None))
#if QT_CONFIG(tooltip)
        self.btn_tour.setToolTip(QCoreApplication.translate("MainWindow", u"Watch a video that will\n"
"take you through the\n"
"operation of Coopertronic OS.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tour.setText(QCoreApplication.translate("MainWindow", u"Guided Tour", None))
#if QT_CONFIG(tooltip)
        self.btn_about.setToolTip(QCoreApplication.translate("MainWindow", u"A dialog that gives you\n"
"a brief overview of what\n"
"Coopertronic OS is all about.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.btn_setup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_how.setText(QCoreApplication.translate("MainWindow", u"How To", None))
        self.btn_install.setText(QCoreApplication.translate("MainWindow", u"Install Apps", None))
#if QT_CONFIG(tooltip)
        self.btn_surgest.setToolTip(QCoreApplication.translate("MainWindow", u"Leave sugestions and\n"
"critisisums for Coopertronic\n"
"so that he can better\n"
"improve Coopertronic OS.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_surgest.setText(QCoreApplication.translate("MainWindow", u"Surgestions", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.col_examine.setText(QCoreApplication.translate("MainWindow", u" Examine ", None))
        self.col_learn.setText(QCoreApplication.translate("MainWindow", u" Learn More ", None))
        self.col_custom.setText(QCoreApplication.translate("MainWindow", u" Customise ", None))
    # retranslateUi

