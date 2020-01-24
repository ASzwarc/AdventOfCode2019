from IntcodeComputer import IntcodeComputer
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])

def solution_part_one(input_file):
    comp = IntcodeComputer()
    comp.read_program_from_file(input_file)
    output = []
    while True:
        ret_val = comp.run_intcode_program()
        if comp._is_finished:
            break
        output.append(ret_val)

    blocks = []
    ball_pos = Pos(0, 0)

    for i in range(0, len(output), 3):
        x, y, elem = output[i:i+3]
        if elem == 2:
            block = Pos(x, y)
            if block in blocks:
                blocks.remove(block)
            else:
                blocks.append(block)
        elif elem == 4:
            ball_pos = Pos(x, y)
    print(len(blocks))


if __name__ == '__main__':
    solution_part_one("Day13Input.txt")
