
import math

path = "R8,U5,L5,D3 U7,R6,D4,L4"
paths = path.split(" ")
path1 = paths[0].split(",")
path2 = paths[1].split(",")
w, h = 11, 10;
Matrix = [[0 for x in range(w)] for y in range(h)]
startX = 1
startY = 1
newStartX = 1
newStartY = 1
Matrix[startX][startY] = 3


def move(dir):
    if dir[0] == "R":
        global startX,newStartX,startY,newStartY
        for x in range(startX, int(dir[1:len(dir)])):
            Matrix[startY][startX+x] = 1
            newStartX+=1
        else:
            startX = newStartX
    elif dir[0] == "U":
        for x in range(startY,int(dir[1:len(dir)])):
            Matrix[startY+x][startX] = 1
            newStartY+=1
        else:
            startY = newStartY
    elif dir[0] == "L":
        for x in range(startX, int(dir[1:len(dir)])):
            Matrix[startY][startX-x] = 1
            newStartX-=1
        else:
            startX = newStartX



def manhattan(x,y):
    print(x," ",y)
    d = (abs(x-500)) + (abs(y-500))
    return d

move("R8")
move("U5")
print(startX," ",startY)
move("L5")

for x in range(len(Matrix)-1, -1, -1):
    print(Matrix[x])
