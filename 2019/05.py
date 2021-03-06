#! python3

# this code is copied from https://github.com/Cloudan29/AdventOfCode_2019/blob/master/day05.py

puzzle = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,9,19,225,1,136,139,224,101,-17,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,2,218,213,224,1001,224,-4560,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,25,63,224,101,-1575,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,55,31,225,1101,38,15,225,1001,13,88,224,1001,224,-97,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1002,87,88,224,101,-3344,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1102,39,10,225,1102,7,70,225,1101,19,47,224,101,-66,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,49,72,225,102,77,166,224,101,-5544,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,101,32,83,224,101,-87,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,80,5,225,1101,47,57,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,344,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,524,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,569,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,599,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,614,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,644,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226"

# opcode
# 1 addition
# 2 multiplication
# 3 input
# 4 output
# 99 halt

# mode
# 0 position mode
# 1 immediate mode (direct value)

# 1002,4,3,4,33

# ABCDE
#  1002

# DE - two-digit opcode,      02 == opcode 2
#  C - mode of 1st parameter,  0 == position mode
#  B - mode of 2nd parameter,  1 == immediate mode
#  A - mode of 3rd parameter,  0 == position mode,
#                                   omitted due to being a leading zero

def transform_to_int_list(str):
    return [int(x) for x in str.split(',')]

inp = transform_to_int_list(puzzle)

def run_machine(value):
    instructions = [j for j in inp]
    i = 0
    while True:
        instruction = instructions[i]
        if instruction == 99:
            break
        parse_instruction = [int(str(instruction)[j]) for j in range(len(str(instruction))-1, -1, -1)]
        opcode = parse_instruction[0]
        address_modes = []
        for j in parse_instruction[2:]:
            address_modes.append(j)
        while len(address_modes) < 3:
            address_modes.append(0)

        value1 = i+1 if address_modes[0] == 1 else instructions[i+1]
        value2 = i+2 if address_modes[1] == 1 else instructions[i+2]
        value3 = i+3 if address_modes[2] == 1 else instructions[i+3]

        if opcode == 1:
            instructions[value3] = instructions[value1] + instructions[value2]
            i+=4
        elif opcode == 2:
            instructions[value3] = instructions[value1] * instructions[value2]
            i+=4
        elif opcode == 3:
            instructions[value1] = value
            i+=2
        elif opcode == 4:
            print (instructions[value1])
            i+=2
        elif opcode == 5:
            if instructions[value1] != 0:
                i = instructions[value2]
            else:
                i+=3
        elif opcode == 6:
            if instructions[value1] == 0:
                i = instructions[value2]
            else:
                i+=3
        elif opcode == 7:
            if instructions[value1] < instructions[value2]:
                instructions[value3] = 1
            else:
                instructions[value3] = 0
            i+=4
        elif opcode == 8:
            if instructions[value1] == instructions[value2]:
                instructions[value3] = 1
            else:
                instructions[value3] = 0
            i+=4

run_machine(1)
run_machine(5)