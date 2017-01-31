import os
from random import randrange
import time
def gen_field(minenum,x,y,field):
    for i in range(minenum):
        mx=randrange(1,len(field[0])-1)
        my=randrange(1,len(field)-1)
        if not(-1<=mx-x<=1 and -1<=my==y<=1 or field[my][mx][0]=='x'):
            field[my][mx][0]='x'
            for j in range(-1,2):
                for k in range(-1,2):
                    if field[my+j][mx+k][0]!='x':
                        field[my+j][mx+k][0]+=1
    print(field)
    return field
def show(px,py,field):
    os.system('cls')
    for i in range(1,len(field)-1):
        outs=''
        for j in range(1,len(field[i])-1):
            if i==py and j==px:			#Show Pointer
                outs+='>'
            else:
                outs+=' '
            if field[i][j][1]=='o':
                outs+=str(field[i][j][0])
            elif field[i][j][1]=='c':
                outs+='*'
            else:
                outs+=field[i][j][1]
        outs+='|'
        print(outs)
def open_empty_field(x,y,field):
    if field[y][x][0]=='x' or field[y][x][1]!='c':
        return field
    if x==0 or x==len(field[0])-1 or y==0 or y==len(field)-1:
        return field
    if 1<=field[y][x][0]<=9:
        field[y][x][1]='o'
        return field
    field[y][x][1]='o'
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=0 or j!=0:
                open_empty_field(x+i,y+j,field)
    return field
def main():
    os.system('cls')
    print('/***********PyMine**********/')
    (field_x,field_y)=map(int,input('Input Field Size:').split(' '))
    minenum=int(input('Input The Number of Mine:'))
    while minenum>(field_x*field_y/2):
        minenum=int(input('\rInput The Number of Mine:'))
    os.system('cls')
    field=[[[0,'c'] for i in range(field_x+2)] for j in range(field_y+2)]       #c:covered o:open f:flag q:questioned
    x=1
    y=1
    flags=0
    start_time=0
    end_time=0
    exist_mines=minenum
    print('MineNum:',minenum-flags)
    first=True
    start=False
    while True:
        show(x,y,field)
        print('MineNum:',minenum-flags)
        if start:
            print('Time:',int(time.time()-start_time))
        act=input()
        if act=='w':
            if y>1:
                y-=1
        elif act=='s':
            if y<field_y:
                y+=1
        elif act=='a':
            if x>1:
                x-=1
        elif act=='d':
            if x<field_x:
                x+=1
        elif act=='q' and field[y][x][1]!='o':
            field[y][x][1]='q' if field[y][x][1]!='q' else 'c'
        elif act=='f' and field[y][x][1]!='o':
            if field[y][x][1]!='f':
                field[y][x][1]='f'
                if field[y][x][0]=='x':
                    exist_mines-=1
                flags+=1
            else:
                field[y][x][1]='c'
                if field[y][x][0]=='x':
                    exist_mines+=1
                flags-=1
        elif act=='e' and field[y][x]!='f' and field[y][x]!='q':
            if first:
                field=gen_field(minenum,x,y,field)
                start_time=time.time()
                first=False
                start=True
            #field[y][x][1]='o'
            field=open_empty_field(x,y,field)
        elif act=='quit':
            break
        elif act=='c':
            field[y][x][1]='c'
        elif act=='oo':
            field=open_empty_field(x,y,field)
        if exist_mines==0:
            print('You Win')
            time.sleep(0.5)
            break
if __name__=='__main__':
    main()

