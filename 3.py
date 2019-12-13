
import math
file = open("3.txt","rt")
path = file.read()
#path = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51 U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
paths = path.split(" ")
path1 = paths[0].split(",")
path2 = paths[1].split(",")
startValue = 1
vector = set()
vectorCheck = set()
vectorInter = set()
tempVector = set()

def insertPath(path,vector, inter=0):
    x,y=startValue,startValue
    minStep = 0
    for z in path:
        if(z[0] == "R"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                x+=1
                if inter != 0:
                    if (x,y) == inter:
                        return minStep
                    else:
                        minStep+=1

        elif(z[0] == "L"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                x-=1
                if inter != 0:
                    if (x,y) == inter:
                        return minStep
                    else:
                        minStep+=1

        elif(z[0] == "U"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                y+=1
                if inter != 0:
                    if (x,y) == inter:
                        return minStep
                    else:
                        minStep+=1

        elif(z[0] == "D"):
            for i in range(0,int(z[1:len(z)])):
                vector.add((x,y))
                y-=1
                if inter != 0:
                    if (x,y) == inter:
                        return minStep
                    else:
                        minStep+=1

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

def findMinSteps(vectorInter):
    p1Steps = 0
    p2Steps = 0
    totalSteps = 0
    for x in vectorInter:
        p1Steps = 0
        p2Steps = 0
        tempSteps = 0
        tempVector = set()
        p1Steps = insertPath(path1,tempVector,x)
        tempVector = set()
        p2Steps = insertPath(path2,tempVector,x)
        tempSteps = (p1Steps+startValue) + (p2Steps+startValue)

        if tempSteps < totalSteps:
            totalSteps = tempSteps
        elif totalSteps == 0:
            totalSteps = tempSteps
    else:
        return totalSteps

print(findMinDistance(vectorInter))
print(findMinSteps(vectorInter))
