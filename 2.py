import math

file = open("2.txt", "rt")
num = file.read()

splitNum = num.split(",")

splitNum[1] = "12"
splitNum[2] = "2"

for x in range(0,len(splitNum),4):
    if splitNum[x] == "1" or splitNum[x] == 1:
        splitNum[int(splitNum[x+3])] = (int(splitNum[int(splitNum[x+1])])+int(splitNum[int(splitNum[x+2])]))
    elif splitNum[x] == "2" or splitNum[x] == 2 :
        splitNum[int(splitNum[x+3])] = (int(splitNum[int(splitNum[x+1])])*int(splitNum[int(splitNum[x+2])]))
    else:
        break;

print(splitNum)
