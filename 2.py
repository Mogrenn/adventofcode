import math
import random
while(True):
    file = open("2.txt", "rt")
    num = file.read()
    splitNum = num.split(",")
    splitNum[1] = str(random.randint(50,99))
    splitNum[2] = str(random.randint(0,49))

    for x in range(0,len(splitNum),4):
        if int(splitNum[x]) == 1:
            splitNum[int(splitNum[x+3])] = (int(splitNum[int(splitNum[x+1])])+int(splitNum[int(splitNum[x+2])]))
        elif int(splitNum[x]) == 2 :
            splitNum[int(splitNum[x+3])] = (int(splitNum[int(splitNum[x+1])])*int(splitNum[int(splitNum[x+2])]))
        else:
            break;

    if splitNum[0] == 19690720:
        break

print(100*int(splitNum[1])+int(splitNum[2]))
