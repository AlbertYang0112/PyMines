# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created: Tue Jan 24 20:56:18 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitDialog(object):
    def comboBoxselect(self,s):
        print('Combo Box Select:',s)
        if s==3:
            self.widget.show()
        else:
            self.widget.hide()
    def accept(self):
        mode=self.comboBox.currentIndex()
        print('Mode ',mode)
        if mode==0:
            self.setfield(3,5,5)
        elif mode==1:
            self.setfield(10,7,7)
        elif mode==2:
            self.setfield(15,10,10)
        elif mode==3:
            sizex=self.lineEdit.text()
            sizey=self.lineEdit_2.text()
            minenum=self.lineEdit_3.text()
            if sizex.isdigit() and sizey.isdigit() and minenum.isdigit():
                sizex,sizey,minenum=map(int,(sizex,sizey,minenum))
                self.setfield(minenum,sizex,sizey)
            else:
                print('Illegal Input')
                return
            print(sizex,sizey,minenum)
        self.diag.accept()
    def setupUi(self, Dialog,setfield):
        Dialog.setObjectName("InitDialog")
        Dialog.resize(291, 98)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Dialog.setModal(False)
        self.setfield=setfield
        self.diag=Dialog
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 263, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("SizeX")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("SizeX_Edit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("SizeY")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("SizeY_Edit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("MineNum")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("MineNum_Edit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget.hide()
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.comboBox.currentIndexChanged['int'].connect(self.comboBoxselect)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyMine v0.2.1"))
        self.comboBox.setItemText(0, _translate("Dialog", "Beginner"))
        self.comboBox.setItemText(1, _translate("Dialog", "Normal"))
        self.comboBox.setItemText(2, _translate("Dialog", "Master"))
        self.comboBox.setItemText(3, _translate("Dialog", "Custom"))
        self.label_2.setText(_translate("Dialog", "SizeX:"))
        self.label_3.setText(_translate("Dialog", "SizeY:"))
        self.label_4.setText(_translate("Dialog", "Mine:"))

