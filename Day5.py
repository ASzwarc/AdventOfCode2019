def solution_part_one(filename):
    input_list = []

    def analyze_opcode(ptr):
        opcode_list = [digit for digit in str(input_list[ptr])]
        oper = int("".join(opcode_list[-2::]))
        indexes = []
        for mode in opcode_list[-3::-1]:
            ptr += 1
            if mode == "0": # position mode
                indexes.append(input_list[ptr])
            elif mode == "1": # immediate mode
                indexes.append(ptr)
            else:
                print("This shouldn't happen in analyze opcode")
        if (oper == 1 or oper == 2) and len(indexes) != 3:
            while len(indexes) < 3:
                ptr += 1
                indexes.append(input_list[ptr])
        return oper, indexes


    with open(filename) as file:
        input_list = [int(x) for x in file.readlines()[0].rstrip().split(",")]
    input_val = 1
    output_val = None
    ptr = 0
    while True:
        oper, indexes = analyze_opcode(ptr)
        if oper == 1:
            input_list[indexes[2]] = (input_list[indexes[0]] +
                input_list[indexes[1]])
            ptr += 4
        elif oper == 2:
            input_list[indexes[2]] = (input_list[indexes[0]] *
                input_list[indexes[1]])
            ptr += 4
        elif oper == 3:
            input_list[input_list[ptr + 1]] = input_val
            ptr += 2
        elif oper == 4:
            output_val = input_list[input_list[ptr + 1]]
            print(f"Opcode 4 at {ptr} OUTPUT is {output_val}")
            ptr += 2
        elif oper == 99:
            print("Finished processing opcode")
            break
    print(f"Diagnostic code is {output_val}")

if __name__ == '__main__':
    solution_part_one("Day5Input.txt")
