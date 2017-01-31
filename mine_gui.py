import os
from random import randrange
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt5 import QtCore
from pyqt1 import *
from inc_gui import *
from init import *
class MineField:
    def __init__(self,minenum=3,sizex=5,sizey=5):
        self.minenum=minenum
        self.sizex=sizex
        self.sizey=sizey
        self.field=[[[0,'c'] for i in range(sizex+2)] for j in range(sizey+2)]       #c:covered o:open f:flag q:questioned
        self.first=True
        self.start=False
        self.flagnum=0
        self.existmine=minenum
        self.printfield=None
    def resize(self,minenum,sizex,sizey):
        self.__init__(minenum,sizex,sizey)
    def gen_field(self,x,y):
        for i in range(self.minenum):
            mx=randrange(1,self.sizex+1)
            my=randrange(1,self.sizey+1)
            if not(-1<=mx-x<=1 and -1<=my==y<=1 or self.field[my][mx][0]=='x'):
                self.field[my][mx][0]='x'
                for j in range(-1,2):
                    for k in range(-1,2):
                        if self.field[my+j][mx+k][0]!='x':
                            self.field[my+j][mx+k][0]+=1
        print(self.field)
    def show(self,px,py):
        #os.system('cls')
        for i in range(1,self.sizey+1):
            outs=''
            for j in range(1,self.sizex+1):
                if i==py and j==px:			#Show Pointer
                    outs+='>'
                else:
                    outs+=' '
                if self.field[i][j][1]=='o':
                    outs+=str(self.field[i][j][0])
                elif self.field[i][j][1]=='c':
                    outs+='*'
                else:
                    outs+=self.field[i][j][1]
            outs+='|'
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
        print('cp',cp)
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
            print('Boom')
        return self.open_empty_field(x,y)
    def mark(self,x,y):
        x+=1
        y+=1
        if self.field[y][x][1]=='c':
            self.field[y][x][1]='f'
            if self.field[y][x][0]=='x':
                self.existmine-=1
            self.flagnum+=1
            if self.existmine==0:
                print('Win')
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
def main(): 
    #(field_x,field_y)=map(int,input('Input Field Size:').split(' '))
   # minenum=int(input('Input The Number of Mine:'))
   # while minenum>(field_x*field_y/2):
    #    minenum=int(input('\rInput The Number of Mine:'))
    minefield=MineField()
    start_time=0
    end_time=0
    start=False
    #GUI
    app = QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Ui_MainWindow()
    print(id(mainWindow))
    def gamestart(minenum,sizex,sizey):
        minefield.resize(minenum,sizex,sizey)
        ui.setupUi(mainWindow,minefield)
        mainWindow.show()
        print(id(mainWindow))

    diag=QDialog()
    diag_init=Ui_InitDialog()
    diag_init.setupUi(diag,gamestart)
    diag.show()
    
    sys.exit( app.exec_() )

if __name__=='__main__':
    main()

