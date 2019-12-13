
import math
file = open("3.txt","rt")
#path = file.read()
path = "R8,U5,L5,D3 U7,R6,D4,L4"
paths = path.split(" ")
path1 = paths[0].split(",")
path2 = paths[1].split(",")
startValue = 1
vector = set()
vectorCheck = set()
vectorInter = set()

def insertPath(path,vector):
    x,y=startValue,startValue
    for z in path:
        if(z[0] == "R"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                x+=1

        elif(z[0] == "L"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                x-=1

        elif(z[0] == "U"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                y+=1

        elif(z[0] == "D"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                y-=1

def checkForInter(vectorCheck,vector):
    for cords in vectorCheck:
        if cords in vector:
            if(cords != (startValue,startValue)):
                vectorInter.add(cords)

def findMinDistance(vectorInter):
    insertPath(path1,vector)
    insertPath(path2,vectorCheck)
    checkForInter(vectorCheck,vector)
    dist = 0
    for x in vectorInter:
        temp = (abs(x[0]-startValue)) + (abs(x[1]-startValue))
        if temp < dist:
            dist = temp
        elif dist == 0:
            dist = temp
    else:
        return dist

print(findMinDistance(vectorInter))
