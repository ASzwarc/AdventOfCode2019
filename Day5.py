def solution_part_one(filename):
    def analyze_opcode(opcode):
        parsed_instruction = []
        opcode_list = [digit for digit in str(opcode)].reverse()
        oper = int("".join(opcode_list[0:2]))


    input_list = []
    with open(filename) as file:
        input_list = [int(x) for x in file.readlines()[0].rstrip().split(",")]
    input_val = 1
    output_val = None
    ptr = 0
    while True:
        opcode = input_list[ptr]
        if opcode == 1:
            input_list[input_list[ptr + 3]] = (
                input_list[input_list[ptr + 1]] +
                input_list[input_list[ptr + 2]])
            ptr += 4
        elif opcode == 2:
            input_list[input_list[ptr + 3]] = (
                input_list[input_list[ptr + 1]] *
                input_list[input_list[ptr + 2]])
            ptr += 4
        elif opcode == 3:
            input_list[input_list[ptr + 1]] = input_val
            ptr += 2
        elif opcode == 4:
            output_val = input_list[input_list[ptr + 1]]
            print(f"Opcode 4 at {ptr} OUTPUT is {output_val}")
            ptr += 2
        elif opcode == 99:
            print("Finished processing opcode")
            break
    print(f"Diagnostic code is {output_val}")

if __name__ == '__main__':
    solution_part_one("Day5Input.txt")
