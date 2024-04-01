# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctos-welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_title = QtWidgets.QHBoxLayout()
        self.main_title.setObjectName("main_title")
        self.main_title_logo = QtWidgets.QLabel(self.centralwidget)
        self.main_title_logo.setText("")
        self.main_title_logo.setPixmap(QtGui.QPixmap("../../Pictures/Coopertronics/Cutting_Room/Dragon.greenWhite.2024.square.png"))
        self.main_title_logo.setObjectName("main_title_logo")
        self.main_title.addWidget(self.main_title_logo)
        self.main_title_head = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sunflower Light")
        font.setPointSize(36)
        self.main_title_head.setFont(font)
        self.main_title_head.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title_head.setObjectName("main_title_head")
        self.main_title.addWidget(self.main_title_head)
        self.verticalLayout.addLayout(self.main_title)
        self.thBtns = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(16)
        self.thBtns.setFont(font)
        self.thBtns.setObjectName("thBtns")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.thBtns)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_grid = QtWidgets.QGridLayout()
        self.btn_grid.setObjectName("btn_grid")
        self.btn_help = QtWidgets.QPushButton(self.thBtns)
        self.btn_help.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_help.setFont(font)
        self.btn_help.setObjectName("btn_help")
        self.btn_grid.addWidget(self.btn_help, 0, 1, 1, 1)
##  Home Page Button
        self.btn_home = QtWidgets.QPushButton(self.thBtns)
        self.btn_home.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_home.setFont(font)
        self.btn_home.setObjectName("btn_home")
        self.btn_home.clicked.connect(self.btn_home_action)
        self.btn_grid.addWidget(self.btn_home, 1, 1, 1, 1)

        self.btn_surgest = QtWidgets.QPushButton(self.thBtns)
        self.btn_surgest.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_surgest.setFont(font)
        self.btn_surgest.setObjectName("btn_surgest")
        self.btn_grid.addWidget(self.btn_surgest, 2, 0, 1, 1)
        self.btn_settings = QtWidgets.QPushButton(self.thBtns)
        self.btn_settings.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_settings.setFont(font)
        self.btn_settings.setObjectName("btn_settings")
        self.btn_grid.addWidget(self.btn_settings, 2, 2, 1, 1)
        self.btn_how = QtWidgets.QPushButton(self.thBtns)
        self.btn_how.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_how.setFont(font)
        self.btn_how.setObjectName("btn_how")
        self.btn_grid.addWidget(self.btn_how, 2, 1, 1, 1)
        self.btn_install = QtWidgets.QPushButton(self.thBtns)
        self.btn_install.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_install.setFont(font)
        self.btn_install.setObjectName("btn_install")
        self.btn_grid.addWidget(self.btn_install, 0, 2, 1, 1)
        self.btn_about = QtWidgets.QPushButton(self.thBtns)
        self.btn_about.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_about.setFont(font)
        self.btn_about.setObjectName("btn_about")
        self.btn_grid.addWidget(self.btn_about, 0, 0, 1, 1)
        self.btn_setup = QtWidgets.QPushButton(self.thBtns)
        self.btn_setup.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_setup.setFont(font)
        self.btn_setup.setObjectName("btn_setup")
        self.btn_grid.addWidget(self.btn_setup, 1, 2, 1, 1)
        self.btn_tour = QtWidgets.QPushButton(self.thBtns)
        self.btn_tour.setMaximumSize(QtCore.QSize(250, 42))
        font = QtGui.QFont()
        font.setFamily("Sunflower Medium")
        font.setPointSize(14)
        self.btn_tour.setFont(font)
        self.btn_tour.setObjectName("btn_tour")
        self.btn_grid.addWidget(self.btn_tour, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.btn_grid)
        self.verticalLayout.addWidget(self.thBtns)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btn_home_action(self):
        print("HOME PAGE button pressed")
        subprocess.run(["xdg-open","https://coopertronic.co.uk/"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_title_head.setText(_translate("MainWindow", "Welcome to Coopertronic OS"))
        self.thBtns.setTitle(_translate("MainWindow", "Explore Coopertronic OS"))
        self.btn_help.setText(_translate("MainWindow", "Help"))
        self.btn_home.setText(_translate("MainWindow", "Home Page"))
        self.btn_surgest.setText(_translate("MainWindow", "Surgestions"))
        self.btn_settings.setText(_translate("MainWindow", "Settings"))
        self.btn_how.setText(_translate("MainWindow", "How To"))
        self.btn_install.setText(_translate("MainWindow", "Install Apps"))
        self.btn_about.setText(_translate("MainWindow", "About"))
        self.btn_setup.setText(_translate("MainWindow", "Setup"))
        self.btn_tour.setText(_translate("MainWindow", "Guided Tour"))
