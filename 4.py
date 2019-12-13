
start = "124075"
slut = "580769"
sum = 0

def bubble(num):
    i = 0
    j = 0
    for x in str(num):
        j = 0
        for y in str(num):
            if(i != j):
                if(y > x):
                    return True
                j+=1
        i+=1
    else:
        return False

def adjecent(num):
    for x in range(0, 5):
        if str(num)[x] == str(num)[x+1]:
            return True
    else:
        return False

def group(num):
    for x in range(0,4):
        if str(num)[x] == str(num)[x+1] and str(num)[x] == str(num)[x+2]:
            if x >= 2:
                return False

            else:

                if str(num)[1] == str(num)[2] and str(num)[1] == str(num)[3] and str(num)[0] != str(num)[1]:
                    return False
                

    else:
        return True

for x in range(int(start),int(slut)+1):
    if not bubble(x):
        if adjecent(x):
            if group(x):
                print(x)
                sum+=1
            else:
                pass
print(sum)
