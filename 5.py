import math
file = open("5.txt", "rt")
num = file.read()
splitNum = num.split(",")

#Ta red på om de är i pos mode eller imid mode
def breakdown_codes(code):
    A = code // 10000 % 10
    B = code // 1000 % 10
    C = code // 100 % 10
    DE = code % 100

    return [A, B, C, DE]

def process_data(values, input, getVals=False):
    index = 0
    while True:

        opCode = breakdown_codes(values[index])
        #Sätter i ordning allt för att kunna kollas
        operation = opCode[3]
        mode1 = opCode[2]
        mode2 = opCode[1]
        mode3 = opCode[0]

        #om mode == 1 så är det pos mode annars imid mode
        index1 = values[index + 1] if mode1 == 0 and index + 1 < len(values) else index + 1
        index2 = values[index + 2] if mode2 == 0 and index + 2 < len(values) else index + 2
        index3 = values[index + 3] if mode3 == 0 and index + 3 < len(values) else index + 3

        #Stäng av
        if operation == 99:
            if getVals:
                return values
            return values[0]
        #Plusa två tal
        elif operation == 1:
            number1 = values[index1]
            number2 = values[index2]
            values[index3] = number1 + number2
            index += 4
        #Multiplicera två tal
        elif operation == 2:
            number1 = values[index1]
            number2 = values[index2]
            values[index3] = number1 * number2
            index += 4
        #Användare input
        elif operation == 3:
            values[values[index + 1]] = input
            index += 2
        #skriv ut
        elif operation == 4:
            output = values[index1]
            values[0] = output
            index += 2
        #sätt index lika med värdet om siffra inte är lika med 0 annars gör inget
        elif operation == 5:
            number1 = values[index1]
            if number1 != 0:
                index = values[index2]
            else:
                index += 3
        #sätt index lika med värdet om siffran är lika med 0 annars gör inget
        elif operation == 6:
            number1 = values[index1]
            if number1 == 0:
                index = values[index2]
            else:
                index += 3
        #om siffra ett är mindre än siffra två så sätt värdet lika med 1
        elif operation == 7:
            if values[index1] < values[index2]:
                values[index3] = 1
            else:
                values[index3] = 0
            index += 4
        #om de två siffrorna är lika med varandra sätt värdet lika med 1
        elif operation == 8:
            if values[index1] == values[index2]:
                values[index3] = 1
            else:
                values[index3] = 0
            index += 4
#Hämtar in värden från filen och konverterar till en int array istället för string
values = [int(numeric_string) for numeric_string in splitNum]

#Börja
print(process_data(values, 5, 0))
