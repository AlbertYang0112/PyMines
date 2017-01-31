from PyQt5 import QtCore, QtGui, QtWidgets
from init import *

class QP(QtWidgets.QPushButton):
    _click=QtCore.pyqtSignal(str)
    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.RightButton:
            self._click.emit('R')
            self.parent().mousePressEvent(event)
        else:
            self._click.emit('L')
            self.parent().mousePressEvent(event)

class Ui_MainWindow(object):
    def clickfield(self,s):
        sender=self.mw.sender()
        (x,y)=map(int,sender.objectName().split(' '))
        print(sender.objectName() + ' was clicked!'+s)
        if s=='L':
            openlist=self.minefield.open(x,y)
            for pos in openlist:
                self.pushButtons[pos[1]-1][pos[0]-1].hide()
                self.pushButtons[pos[1]-1][pos[0]-1].destroy()
                if self.minefield.field[pos[1]][pos[0]][0]!=0:
                    self.words.append(QtWidgets.QLabel(self.centralwidget))
                    self.words[-1].setGeometry(QtCore.QRect(self.blocksize*(pos[0]-1),self.blocksize*(pos[1]-1),self.blocksize,self.blocksize))
                    self.words[-1].setObjectName(str(pos[0]-1)+' '+str(pos[1]-1))
                    self.words[-1].setFont(self.font)
                    self.words[-1].setText(str(self.minefield.field[pos[1]][pos[0]][0]))
                    self.words[-1].show()
                print(self.pushButtons[pos[1]-1][pos[0]-1].objectName()+' was opened')
        elif s=='R':
            sender.setText(self.minefield.mark(x,y))

    def setupUi(self,MainWindow,MineField):
        self.blocksize=50
        self.mw=MainWindow
        self.minefield=MineField
        self.words=[]
        self.font=QtGui.QFont()
        self.font.setFamily("System")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.blocksize*self.minefield.sizex, self.blocksize*self.minefield.sizey+21)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Show Keys
        self.pushButtons=[[QP(self.centralwidget) for i in range(self.minefield.sizex)] for j in range(self.minefield.sizey)]
        for i in range(0,self.minefield.sizex):
            for j in range(0,self.minefield.sizey):
                self.pushButtons[j][i].setGeometry(QtCore.QRect(self.blocksize*i,self.blocksize*j,self.blocksize,self.blocksize))
                self.pushButtons[j][i].setObjectName(str(i)+' '+str(j))
                
        MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        #self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        for Buttons in self.pushButtons:
            for butt in Buttons:
                butt._click.connect(self.clickfield)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('PyMine')

