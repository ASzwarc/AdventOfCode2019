from IntcodeComputer import IntcodeComputer

def solution_part_one(filename):
    # convention: (x, y)
    # directions: left, up, right, down
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 1

    def turn_robot(position, turn):
        global dir_index
        if turn == 0: #left 90 degrees
            dir_index = (dir_index - 1) & 3
        else: #right 90 degrees
            dir_index = (dir_index + 1) & 3
        return (position[0] + directions[dir_index][0],
                position[1] + directions[dir_index][1])

    comp = IntcodeComputer()
    visited_positions = {}
    position = (0, 0)
    comp.read_program_from_file(filename)
    colored_panels_no = 0

    while not comp._is_finished:
        color_of_panel = visited_positions.get(position, default=0)
        new_color, turn = comp.run_intcode_program(color_of_panel)
        if new_color != color_of_panel:
            colored_panels_no += 1

        position = turn_robot(position, turn)

    print(f"Number of colored panels is {colored_panels_no}")

if __name__ == '__main__':
    solution_part_one("Day11Input.txt")