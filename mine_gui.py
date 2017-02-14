from random import randrange
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from inc_gui import *


class MineField:
    def __init__(self, mainWindow, ui):
        self.minenum=3
        self.sizex=5
        self.sizey=5
        self.field=[[[0,'c'] for i in range(self.sizex+2)] for j in range(self.sizey+2)]       #c:covered o:open f:flag q:questioned
        self.first=True
        self.start=False
        self.flagnum=0
        self.existmine=self.minenum
        self.mainWindow = mainWindow
        self.ui = ui
        self.firstGame = True

    def resize(self,minenum,sizex,sizey):
        self.__init__(self.mainWindow, self.ui)
        self.minenum = minenum
        self.sizex = sizex
        self.sizey = sizey
        self.existmine = self.minenum
        self.field=[[[0,'c'] for i in range(self.sizex+2)] for j in range(self.sizey+2)]       #c:covered o:open f:flag q:questioned

    def gen_field(self,x,y):
        for i in range(self.minenum):
            setMine = False
            while not setMine:
                mx=randrange(1,self.sizex+1)
                my=randrange(1,self.sizey+1)
                if not(-1<=mx-x<=1 and -1<=my==y<=1 or self.field[my][mx][0]=='x'):
                    self.field[my][mx][0]='x'
                    setMine = True
                    for j in range(-1,2):
                        for k in range(-1,2):
                            if self.field[my+j][mx+k][0]!='x':
                                self.field[my+j][mx+k][0]+=1
        #print(self.field)

    def show(self, px, py):
        #os.system('cls')
        for i in range(1, self.sizey+1):
            outs=''
            for j in range(1,self.sizex+1):
                if i == py and j == px:			#Show Pointer
                    outs += '>'
                else:
                    outs += ' '
                if self.field[i][j][1]=='o':
                    outs += str(self.field[i][j][0])
                elif self.field[i][j][1]=='c':
                    outs += '*'
                else:
                    outs += self.field[i][j][1]
            outs += '|'
            print(outs)

    def open_empty_field(self,x,y):
        if self.field[y][x][0]=='x' or self.field[y][x][1]!='c':
            return []
        if x==0 or x==self.sizex+1 or y==0 or y==self.sizey+1:
            return []
        if 1<=self.field[y][x][0]<=9:
            self.field[y][x][1]='o'
            return [(x,y)]
        cp=[]
        #print('cp',cp)
        self.field[y][x][1]='o'
        cp.append((x,y))
        for i in range(-1,2):
            for j in range(-1,2):
                if i!=0 or j!=0:
                    cp+=self.open_empty_field(x+i,y+j)
        return cp

    def open(self,x,y):
        x+=1
        y+=1
        if self.first:
            self.gen_field(x,y)
            #self.printfield()
            self.first=False
        if self.field[y][x][0]=='x':
            #print('Boom')
            self.gameover(False)
        return self.open_empty_field(x,y)

    def mark(self,x,y):
        x+=1
        y+=1
        if self.field[y][x][1]=='c':
            self.field[y][x][1]='f'
            if self.field[y][x][0]=='x':
                self.existmine-=1
            self.flagnum+=1
            if self.existmine==0 and self.flagnum == self.minenum:
                #print('Win')
                self.gameover(True)
            return 'f'
        if self.field[y][x][1]=='f':
            self.field[y][x][1]='q'
            if self.field[y][x][0]=='x':
                self.existmine+=1
            self.flagnum-=1
            return 'q'
        if self.field[y][x][1]=='q':
            self.field[y][x][1]='c'
            return ''
        return ''

    def gamestart(self, minenum, sizex, sizey):
        self.resize(minenum, sizex, sizey)
        self.ui.setupUi(self.mainWindow, self)
        self.firstGame = False
        self.mainWindow.show()

    def setRestartEnt(self,restartEnt):
        self.restartEnt = restartEnt

    def setExec(self, appexec):
        self.exec = appexec

    def gameover(self, state):
        self.ui.emptyUi()
        time = self.ui.timerPause()
        _overdiag = QDialog(self.mainWindow)
        self.overdiag = Ui_OverDialog()
        self.overdiag.setupUi(_overdiag, state, self.restartEnt, [self.minenum, time])
        self.overdiag.setExec(self.appExec)
        self.overdiag.Dialog.show()

    def appExec(self):
        self.mainWindow.close()


def main():
    app = QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Ui_MainWindow()
    minefield = MineField(mainWindow, ui)
    diag_init = Ui_InitDialog(mainWindow)
    minefield.setRestartEnt(diag_init.restart)
    diag_init.setupUi(minefield.gamestart)

    sys.exit( app.exec_() )

if __name__=='__main__':
    main()

