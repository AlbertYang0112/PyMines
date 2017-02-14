from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_InitDialog(object):

    def __init__(self, mainWindow):
        self.inited = False
        self.mainWindow = mainWindow
    def comboBoxselect(self,s):
        print('Combo Box Select:',s)
        if s==3:
            self.widget.show()
        else:
            self.widget.hide()
    def accept( self ):
        mode=self.comboBox.currentIndex()
        #print('Mode ',mode)
        if mode==0:
            self.setfield(3,5,5)
        elif mode==1:
            self.setfield(10,7,7)
        elif mode==2:
            self.setfield(30,20,20)
        elif mode==3:
            sizex=self.lineEdit.text()
            sizey=self.lineEdit_2.text()
            minenum=self.lineEdit_3.text()
            if sizex.isdigit() and sizey.isdigit() and minenum.isdigit():
                sizex, sizey, minenum = map(int, (sizex, sizey, minenum))
                illegal = False
                if sizex < 5:
                    self.lineEdit.setText('5')
                    illegal = True
                if sizey < 5:
                    self.lineEdit_2.setText('5')
                    illegal = True
                if sizex > 40:
                    self.lineEdit.setText('50')
                    illegal = True
                if sizey > 40:
                    self.lineEdit_2.setText('50')
                    illegal = True
                if minenum > 0.6 * sizex * sizey:
                    self.lineEdit_3.setText(str(int(sizex * sizey * 0.6)))
                    illegal = True
                if minenum < 0.1 * sizex * sizey:
                    self.lineEdit_3.setText(str(int(sizex * sizey * 0.1)))
                    illegal = True
                if illegal:
                    return
                sizex,sizey,minenum=map(int,(sizex,sizey,minenum))
                self.setfield(minenum,sizex,sizey)
            else:
                print('Illegal Input')
                return
            print(sizex,sizey,minenum)
        self.diag.accept()
        self.diag.destroy()
    def setupUi(self, setfield):
        self.diag = QtWidgets.QDialog(self.mainWindow)
        self.diag.setObjectName("Initdiag")
        self.diag.resize(291, 98)
        self.diag.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.diag.setModal(False)
        self.setfield=setfield
        if not self.inited:
            self.verticalLayoutWidget = QtWidgets.QWidget(self.diag)
            self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
            self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
            self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
            self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
            self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
            self.diag.setWindowIcon(QIcon('icons/title.ico'))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 263, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2.setObjectName("SizeX")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit.setObjectName("SizeX_Edit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3.setObjectName("SizeY")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2.setObjectName("SizeY_Edit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_4.setObjectName("MineNum")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3.setObjectName("MineNum_Edit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget.hide()
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(self.diag)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.diag.reject)
        self.comboBox.currentIndexChanged['int'].connect(self.comboBoxselect)
        QtCore.QMetaObject.connectSlotsByName(self.diag)
        self.diag.show()
    def restart(self):
        self.setupUi(self.setfield)
        self.diag.show()

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

    colorTable = ['0,0,255', '0,255,0', '255, 0, 0',
                  '0,0,128', '0,128,0', '128,0,0',
                  '255,255,0', '255,0,255', '0,255,255', '255,255,255']

    def __init__(self):
        self.inited = False

    def clickfield(self,s):
        sender=self.mw.sender()
        (x,y)=map(int,sender.objectName().split(' '))
        if s=='L':
            openlist=self.minefield.open(x,y)
            for pos in openlist:
                self.pushButtons[pos[1]-1][pos[0]-1].hide()
                self.pushButtons[pos[1]-1][pos[0]-1].destroy()
                if self.minefield.field[pos[1]][pos[0]][0] != 0 and self.minefield.field[pos[1]][pos[0]][0] != 'x':
                    self.words.append(QtWidgets.QLabel(self.centralwidget))
                    self.words[-1].setGeometry(QtCore.QRect(self.blocksize*(pos[0]-1) + self.blocksize/2,
                                                            self.blocksize*(pos[1]-1) + self.dy_up,
                                                            self.blocksize, self.blocksize))
                    self.words[-1].setObjectName(str(pos[0]-1)+' '+str(pos[1]-1))
                    self.words[-1].setStyleSheet('QLabel{color:rgb(' +
                                                 self.colorTable[ self.minefield.field[pos[1]][pos[0]][0] - 1 ] +
                                                 ',250);'
                                                 'font-size:19px;' +
                                                 'font-weight:bold;' +
                                                 'font-family:Microsoft YaHei UI;}'
                                                 )
                    self.words[-1].setText(str(self.minefield.field[pos[1]][pos[0]][0]))
                    self.words[-1].show()
                #print(self.pushButtons[pos[1]-1][pos[0]-1].objectName()+' was opened')
        elif s=='R':
            #sender.setText(self.minefield.mark(x,y))
            status = self.minefield.mark(x,y)
            if status == 'f':
                sender.setIcon(QIcon('icons/flag.png'))
            elif status == 'q':
                sender.setIcon(QIcon('icons/questioned.png'))
            elif status == '':
                sender.setIcon(QIcon(None))
        self.refreshScore()
        #print(self.minefield.minenum - self.minefield.flagnum)

    def refreshScore(self):
        score = self.minefield.minenum - self.minefield.flagnum
        self.scoreDisplay.display(-99 if -99 > score
                          else 999 if score > 999.
                          else score)


    def setupUi(self,MainWindow, MineField):
        self.pause = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refreshTime)
        self.timer.start(1000)
        self.time = 0
        self.dy_up = 30
        self.dy_down = 21
        self.blocksize = 30
        self.mw = MainWindow
        self.minefield = MineField
        self.words=[]
        self.mw.setWindowIcon(QIcon('icons/title.ico'))
        self.minePixMap = QtGui.QPixmap('icons/mine.png').scaled(self.blocksize, self.blocksize)
        self.flagPixMap = QtGui.QPixmap('icons/flag.png').scaled(self.blocksize, self.blocksize)
        #MainWindow.setStyleSheet("QLabel{color::rgb(100,100,100,250);font-size:15px;font-weight=bold;font-famil:System}"
         #                        "QLabel:hover{color:rgb(100,100,100,0);}")
        self.font=QtGui.QFont()
        if not self.inited:
            self.timeDisplay = QtWidgets.QLCDNumber(MainWindow)
            self.scoreDisplay = QtWidgets.QLCDNumber(MainWindow)
            self.inited = True
        self.timeDisplay.setGeometry(QtCore.QRect(self.blocksize * (self.minefield.sizex-2), 0, 2 * self.blocksize, self.blocksize))
        self.timeDisplay.setObjectName("timeDisplay")
        self.timeDisplay.setDigitCount(3)
        self.timeDisplay.display(0)

        self.scoreDisplay.setGeometry(QtCore.QRect(0, 0, 2 * self.blocksize, self.blocksize))
        self.scoreDisplay.setObjectName("scoreDisplay")
        self.scoreDisplay.setDigitCount(3)
        #self.refreshScore()
        self.scoreDisplay.display(self.minefield.minenum)

        self.font.setFamily("System")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(self.blocksize*self.minefield.sizex,
                          self.blocksize * self.minefield.sizey
                          + self.dy_up + self.dy_down)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Show Keys
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect((0.5 * self.minefield.sizex - 0.4) * self.blocksize, 0.1 * self.blocksize,
                                                    0.8 * self.blocksize, 0.8 * self.blocksize))
        self.restartButton.clicked.connect(self.minefield.restartEnt)

        self.pushButtons=[[QP(self.centralwidget) for i in range(self.minefield.sizex)]
                          for j in range(self.minefield.sizey)]
        for i in range(0,self.minefield.sizex):
            for j in range(0,self.minefield.sizey):
                self.pushButtons[j][i].setGeometry(QtCore.QRect(self.blocksize*i,
                                                                self.blocksize*j+self.dy_up,
                                                                self.blocksize, self.blocksize))
                self.pushButtons[j][i].setObjectName(str(i)+' '+str(j))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        for Buttons in self.pushButtons:
            for butt in Buttons:
                butt._click.connect(self.clickfield)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def emptyUi(self):
        for butts in self.pushButtons:
            for butt in butts:
                if not butt.isHidden():
                    butt.hide()
        for posx in range(1, self.minefield.sizex+1):
            for posy in range(1, self.minefield.sizey+1):
                if self.minefield.field[posy][posx][0] != 0:
                    self.words.append(QtWidgets.QLabel(self.centralwidget))
                    self.words[-1].setObjectName(str(posx-1)+' '+str(posy-1))
                    if self.minefield.field[posy][posx][0] != 'x':
                        self.words[-1].setStyleSheet('QLabel{color:rgb(' +
                                                 self.colorTable[self.minefield.field[posy][posx][0] - 1] +
                                                 ',250);'
                                                 'font-size:19px;' +
                                                 'font-weight:bold;' +
                                                 'font-family:Microsoft YaHei UI;}'
                                                 )
                        self.words[-1].setFont(self.font)
                        self.words[-1].setText(str(self.minefield.field[posy][posx][0]))
                        self.words[-1].setGeometry(QtCore.QRect(self.blocksize*(posx-1) + self.blocksize/2,
                                                                self.blocksize*(posy-1) + self.dy_up,
                                                                self.blocksize, self.blocksize))
                    else:
                        self.words[-1].setPixmap(self.minePixMap)
                        self.words[-1].setGeometry(QtCore.QRect(self.blocksize*(posx-1) + 6,
                                                                self.blocksize*(posy-1) + self.dy_up,
                                                                self.blocksize, self.blocksize))

                    self.words[-1].show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('PyMine')

    def refreshTime(self):
        if not self.pause:
            self.time += 1
        self.timeDisplay.display(self.time if self.time < 999 else 999)

    def timerPause(self):
        self.pause = True
        return self.time


class Ui_OverDialog(object):

    def __init__(self):
        self.rec = []

    def Restart(self):
        if self.changed < 4:
            self.changePos()
            return
        self.Dialog.destroy()
        self.restartEnt()

    def setExec(self,exec):
        self.exec = exec

    def Exit(self):
        self.exec()

    def readRecord(self):
        self.rec = []
        try:
            with open('record', 'r') as file:
                for line in file:
                    line = line.split(' ')
                    noappend = False
                    for i in range(3):
                        if not line[i].isdigit():
                            noappend = True
                        line[i] = int(line[i])
                    if not noappend:
                        self.rec.append(line)
        except Exception as err:
            pass
        self.rec.sort(key=lambda x: x[2])

    def writeRecord(self, score):
        score.append(int(round(score[1] / score[0], 2) * 100))
        if len(self.rec) != 0:
            for i in range(0, len(self.rec)):
                if score[2] >= self.rec[i][2]:
                    self.rec.insert(i, score)
        else:
            self.rec.append(score)
        file = open('record', 'a')
        for item in score:
            file.write(str(item) + ' ')
        file.write('\n')
        file.close()

    def changePos(self):
        if self.changed % 2 == 0:
            self.labelAccept.setText("Leave&Study!")
            self.labelLeave.setText("Still wanna play?")
            self.restartButton.setText("Exit")
            self.leaveButton.setText("Restart")
            self.restartButton.disconnect()
            self.leaveButton.disconnect()
            self.restartButton.clicked.connect(self.Exit)
            self.leaveButton.clicked.connect(self.Restart)
        else:
            self.labelLeave.setText("Leave&Study!")
            self.labelAccept.setText("Still wanna play?")
            self.leaveButton.setText("Exit")
            self.restartButton.setText("Restart")
            self.restartButton.disconnect()
            self.leaveButton.disconnect()
            self.leaveButton.clicked.connect(self.Exit)
            self.restartButton.clicked.connect(self.Restart)
        self.changed += 1

    def setupUi(self, dialog, state, restartEnt, score):
        self.Dialog = dialog
        self.changed = 0

        if state:
            self.writeRecord(score)
            self.Dialog.setWindowTitle('You Win')
        else:
            self.Dialog.setWindowTitle('Boom')
        self.readRecord()

        self.restartEnt = restartEnt

        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(251, 201)

        self.Dialog.setWindowIcon(QIcon('icons/title.ico'))

        self.verticalLayoutWidget = QtWidgets.QWidget(self.Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.rec))

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)

        for i in range(len(self.rec)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            #print('A')

        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        font.setBold(False)
        for row in range(len(self.rec)):
            for col in range(3):
                item = QtWidgets.QTableWidgetItem()
                item.setFont(font)
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(62)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidget)

        self.labelLeave = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setBold(True)
        self.labelLeave.setFont(font)
        self.labelLeave.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLeave.setObjectName("labelLeave")
        self.verticalLayout.addWidget(self.labelLeave)
        self.leaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setBold(False)
        self.leaveButton.setFont(font)
        self.leaveButton.setObjectName("leaveButton")
        self.verticalLayout.addWidget(self.leaveButton)
        self.labelAccept = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setBold(True)
        self.labelAccept.setFont(font)
        self.labelAccept.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccept.setObjectName("labelAccept")
        self.verticalLayout.addWidget(self.labelAccept)
        self.restartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setBold(False)
        self.restartButton.setFont(font)
        self.restartButton.setObjectName("restartButton")
        self.verticalLayout.addWidget(self.restartButton)

        self.restartButton.clicked.connect(self.Restart)
        self.leaveButton.clicked.connect(self.Exit)

        self.setTextUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def setTextUi(self):
        for i in range(len(self.rec)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i + 1))

            item = self.tableWidget.item(i, 0)
            item.setText(str(self.rec[i][0]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item = self.tableWidget.item(i, 1)
            item.setText(str(self.rec[i][1]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item = self.tableWidget.item(i, 2)
            item.setText(str(self.rec[i][2] / 100))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Time")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Num")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Avg")
        self.labelLeave.setText("Leave&Study?")
        self.leaveButton.setText("Exit")
        self.labelAccept.setText("What?Play Again?!")
        self.restartButton.setText("Restart")
