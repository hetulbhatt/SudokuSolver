import os
import time

hardCells = [[0]*9 for i in range(0,9)]
count = 0

def checkBlock(x, y, val, arr):
    bx,x = divmod(x,3)
    by,y = divmod(y,3)
    bx = bx*3
    by = by*3
#     print(bx,x,by,y)
    
    for i in range(bx,bx+3):
        for j in range(by,by+3):
            if(arr[i][j] == val):
#             print('blk: ',i,j)
                return False
    return True

def checkCol(x, val, arr):
    for i in range(0,9):
        if(arr[i][x] == val):
#             print('col: ',i,x)
            return False
    return True

def checkRow(y, val, arr):
    for i in range(0,9):
        if(arr[y][i] == val):
#             print('row: ',y,i)
            return False
    return True

def check(x,y,val,arr):
    return (checkBlock(x,y,val,arr) & checkCol(y,val,arr) & checkRow(x,val,arr))


def display(arr):
    os.system('cls')
    print(count)
    for i in arr:
        print(i)
    time.sleep(0.2)

def sudokuSolver(x,y,arr):
    global count
    count+=1
    if(count%1000 == 0):
        display(arr)
    if(hardCells[x][y] != 0):
        if(y>=8): 
            if(x>=8):
                display(arr)
                print('Brought down from: 3.3813919e+51 to: ',count)
#                 display(hardCells)
                input()
                quit()
            sudokuSolver(x+1,0,arr)
        else:
            sudokuSolver(x,y+1,arr)
    else:            
        for i in range(1,10):
            if(check(x,y,i,arr)):
                arr[x][y] = i
                if(y>=8): 
                    if(x>=8):
                        os.system('cls')
                        display(arr)
                        print('Brought down from: 3.3813919e+51 to: ',count)
#                         display(hardCells)
                        input()
                        quit()
                    sudokuSolver(x+1,0,arr)
                else:
                    sudokuSolver(x,y+1,arr)
        arr[x][y] = 0
        return

arr = [[0]*9 for i in range(0,9)]


arr[0][0] = 7
arr[0][2] = 5
arr[0][3] = 2
arr[0][5] = 6
arr[1][1] = 8
arr[1][2] = 9
arr[1][3] = 5
arr[1][5] = 7
arr[1][6] = 2
arr[2][4] = 4
arr[3][1] = 5
arr[3][8] = 4
arr[4][1] = 9
arr[4][3] = 6
arr[4][5] = 4
arr[4][7] = 1
arr[5][0] = 1
arr[5][7] = 5
arr[7][2] = 8
arr[7][3] = 9
arr[7][5] = 1
arr[7][6] = 6
arr[7][7] = 7
arr[8][3] = 4
arr[8][5] = 5
arr[8][6] = 1
arr[8][8] = 2

# display(arr)
# os.system('cls')
# print()
for i in range(0,9):
    for j in range(0,9):
        if(arr[i][j] != 0):
            hardCells[i][j] = 1
sudokuSolver(0,0,arr)


# print(arr)