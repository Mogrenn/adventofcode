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
        opcode = breakdown_codes(values[index])
        operation = opcode[3]
        mode_1 = opcode[2]
        mode_2 = opcode[1]
        mode_3 = opcode[0]

        index_1 = values[index + 1] if mode_1 == 0 and index + 1 < len(values) else index + 1
        index_2 = values[index + 2] if mode_2 == 0 and index + 2 < len(values) else index + 2
        index_3 = values[index + 3] if mode_3 == 0 and index + 3 < len(values) else index + 3

        if operation == 99:
            if getVals:
                return values
            return values[0]

        elif operation == 1:
            number_1 = values[index_1]
            number_2 = values[index_2]
            values[index_3] = number_1 + number_2
            index += 4

        elif operation == 2:
            number_1 = values[index_1]
            number_2 = values[index_2]
            values[index_3] = number_1 * number_2
            index += 4

        elif operation == 3:
            values[values[index + 1]] = input
            index += 2

        elif operation == 4:
            output = values[index_1]
            values[0] = output
            index += 2

        elif operation == 5:
            number_1 = values[index_1]
            if number_1 != 0:
                index = values[index_2]
            else:
                index += 3

        elif operation == 6:
            number_1 = values[index_1]
            if number_1 == 0:
                index = values[index_2]
            else:
                index += 3

        elif operation == 7:
            if values[index_1] < values[index_2]:
                values[index_3] = 1
            else:
                values[index_3] = 0
            index += 4

        elif operation == 8:
            if values[index_1] == values[index_2]:
                values[index_3] = 1
            else:
                values[index_3] = 0
            index += 4

values = [int(numeric_string) for numeric_string in splitNum]
print(process_data(values, 5, 0))
