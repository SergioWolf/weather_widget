# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(193, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPicture = QtWidgets.QLabel(self.centralwidget)
        self.labelPicture.setGeometry(QtCore.QRect(0, 0, 81, 81))
        self.labelPicture.setObjectName("labelPicture")
        self.lineEditDegree = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDegree.setGeometry(QtCore.QRect(100, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditDegree.setFont(font)
        self.lineEditDegree.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEditDegree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditDegree.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDegree.setObjectName("lineEditDegree")
        self.lineEditSky = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSky.setGeometry(QtCore.QRect(100, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditSky.setFont(font)
        self.lineEditSky.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditSky.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditSky.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSky.setObjectName("lineEditSky")
        self.lineEditCity = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCity.setGeometry(QtCore.QRect(0, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEditCity.setFont(font)
        self.lineEditCity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditCity.setObjectName("lineEditCity")
        self.lineEditDateTime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateTime.setGeometry(QtCore.QRect(20, 116, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEditDateTime.setFont(font)
        self.lineEditDateTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDateTime.setObjectName("lineEditDateTime")
        self.labelWind = QtWidgets.QLabel(self.centralwidget)
        self.labelWind.setGeometry(QtCore.QRect(10, 140, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWind.sizePolicy().hasHeightForWidth())
        self.labelWind.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelWind.setFont(font)
        self.labelWind.setObjectName("labelWind")
        self.lineEditWind = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWind.setGeometry(QtCore.QRect(60, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditWind.setFont(font)
        self.lineEditWind.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditWind.setObjectName("lineEditWind")
        self.labelHumidity = QtWidgets.QLabel(self.centralwidget)
        self.labelHumidity.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelHumidity.setFont(font)
        self.labelHumidity.setObjectName("labelHumidity")
        self.lineEditHumidity = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHumidity.setGeometry(QtCore.QRect(100, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditHumidity.setFont(font)
        self.lineEditHumidity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditHumidity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHumidity.setObjectName("lineEditHumidity")
        self.labelPressure = QtWidgets.QLabel(self.centralwidget)
        self.labelPressure.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelPressure.setFont(font)
        self.labelPressure.setObjectName("labelPressure")
        self.lineEditPressure = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPressure.setGeometry(QtCore.QRect(90, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEditPressure.setFont(font)
        self.lineEditPressure.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPressure.setObjectName("lineEditPressure")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 193, 21))
        self.menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.menubar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeatherWidget"))
        self.labelPicture.setText(_translate("MainWindow", "NoPicture"))
        self.labelWind.setText(_translate("MainWindow", "Ветер:"))
        self.labelHumidity.setText(_translate("MainWindow", "Влажность:"))
        self.labelPressure.setText(_translate("MainWindow", "Давление:"))

