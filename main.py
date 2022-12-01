import numpy

with open("code.txt", 'r') as code:
    input_code = code.read()

    limit = 2**32
    cells = 16
    pointer = 0

    regs = [0] * cells
    loop_indexes = [-1]

    index = 0
    reading = True
    kept = 0

    while True:
        char = input_code[index]
        if reading:
            if char == '[' and regs[pointer] != 0:  # if statement
                reading = False

            elif char == '=':
                if regs[pointer - 1] == kept:
                    regs[pointer] = 1
                else:
                    regs[pointer] = 0

            elif char == '+':  # increase by one
                regs[pointer] = (regs[pointer] + 1) % limit

            elif char == '-':  # decrease by one
                regs[pointer] = (regs[pointer] - 1) % limit

            elif char == '<':  # moves pointer left by one
                pointer = (pointer - 1) % cells

            elif char == '>':  # moves pointer right by one
                pointer = (pointer + 1) % cells

            elif char == '|':  # sets to number n before it
                regs[pointer] = regs[pointer - regs[pointer]]

            elif char == '_':  # sets to number n before it
                regs[pointer] = regs[pointer + regs[pointer]]

            elif char == '\'':  # prints number value
                print(regs[pointer], end='')

            elif char == '\"':  # prints ascii representation of value
                print(chr(regs[pointer]), end='')

            elif char == '\\':  # prints newline
                print()

            elif char == "^":  # gets int input
                regs[pointer] = int(input()) % limit

            elif char == "$":  # gets ascii input
                regs[pointer] = ord(input()) % limit

            elif char == "(":  # starts loop
                loop_indexes.append(index)

            elif char == ")":  #resets loop
                if regs[pointer] != 0:
                    index = loop_indexes[len(loop_indexes) - 1]
                else:
                    loop_indexes.pop()

            elif char == "~":
                print(f"\n{index}, {pointer}: {regs}")

            elif char == "!":
                print()
                exit("Terminated by Goldstein++ Code")

            elif char == "@":
                kept = regs[pointer]

            elif char == "#":
                regs[pointer] = kept

        if char == ']' and not reading:
            reading = True

        index += 1
