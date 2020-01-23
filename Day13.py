from IntcodeComputer import IntcodeComputer

def solution_part_one(input_file):
    comp = IntcodeComputer()
    comp.read_program_from_file(input_file)
    output = []
    while True:
        ret_val = comp.run_intcode_program()
        if comp._is_finished:
            break
        output.append(ret_val)
    print(output)


if __name__ == '__main__':
    solution_part_one("Day13Input.txt")
