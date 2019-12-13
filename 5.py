import math
file = open("5.txt", "rt")
num = file.read()
splitNum = num.split(",")

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
        operation = opCode[3]
        mode1 = opCode[2]
        mode2 = opCode[1]
        mode3 = opCode[0]

        index1 = values[index + 1] if mode1 == 0 and index + 1 < len(values) else index + 1
        index2 = values[index + 2] if mode2 == 0 and index + 2 < len(values) else index + 2
        index3 = values[index + 3] if mode3 == 0 and index + 3 < len(values) else index + 3

        if operation == 99:
            if getVals:
                return values
            return values[0]

        elif operation == 1:
            number1 = values[index1]
            number2 = values[index2]
            values[index3] = number1 + number2
            index += 4

        elif operation == 2:
            number1 = values[index1]
            number2 = values[index2]
            values[index3] = number1 * number2
            index += 4

        elif operation == 3:
            values[values[index + 1]] = input
            index += 2

        elif operation == 4:
            output = values[index1]
            values[0] = output
            index += 2

        elif operation == 5:
            number1 = values[index1]
            if number1 != 0:
                index = values[index2]
            else:
                index += 3

        elif operation == 6:
            number1 = values[index1]
            if number1 == 0:
                index = values[index2]
            else:
                index += 3

        elif operation == 7:
            if values[index1] < values[index2]:
                values[index3] = 1
            else:
                values[index3] = 0
            index += 4

        elif operation == 8:
            if values[index1] == values[index2]:
                values[index3] = 1
            else:
                values[index3] = 0
            index += 4

values = [int(numeric_string) for numeric_string in splitNum]
print(process_data(values, 5, 0))
