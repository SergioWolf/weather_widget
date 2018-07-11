# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_city.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(214, 129)
        self.labelCountry = QtWidgets.QLabel(Dialog)
        self.labelCountry.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCountry.setFont(font)
        self.labelCountry.setObjectName("labelCountry")
        self.comboBoxCountry = QtWidgets.QComboBox(Dialog)
        self.comboBoxCountry.setGeometry(QtCore.QRect(70, 10, 131, 22))
        self.comboBoxCountry.setObjectName("comboBoxCountry")
        self.labelCity = QtWidgets.QLabel(Dialog)
        self.labelCity.setGeometry(QtCore.QRect(10, 40, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCity.setFont(font)
        self.labelCity.setObjectName("labelCity")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.labelCityID = QtWidgets.QLabel(Dialog)
        self.labelCityID.setGeometry(QtCore.QRect(10, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCityID.setFont(font)
        self.labelCityID.setObjectName("labelCityID")
        self.lineEditCityID = QtWidgets.QLineEdit(Dialog)
        self.lineEditCityID.setGeometry(QtCore.QRect(70, 70, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCityID.setFont(font)
        self.lineEditCityID.setObjectName("lineEditCityID")
        self.pushButtonOk = QtWidgets.QPushButton(Dialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(124, 100, 81, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SearchCity"))
        self.labelCountry.setText(_translate("Dialog", "Country"))
        self.labelCity.setText(_translate("Dialog", "City"))
        self.labelCityID.setText(_translate("Dialog", "CityID"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

