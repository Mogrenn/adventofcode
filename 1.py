import math

sum = 0

file = open("1.txt", "rt")

def calcFuel(fuel):
    run = True
    sum = 0
    while(run):
        fuel /=3
        fuel = math.floor(fuel);
        fuel -= 2
        if(math.floor((fuel/3)-2) <= 0):
            sum+=fuel
            return sum
            run = False
        else:
            sum +=fuel

for num in file:
    intNum = int(num);
    sum += calcFuel(intNum)

print(sum)
