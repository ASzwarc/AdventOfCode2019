from IntcodeComputer import IntcodeComputer

def turn_robot(position, turn, dir_index):
    # convention: (x, y)
    # directions: left, up, right, down
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if turn == 0: #left 90 degrees
        dir_index = (dir_index - 1) & 3
    else: #right 90 degrees
        dir_index = (dir_index + 1) & 3
    return (position[0] + directions[dir_index][0],
            position[1] + directions[dir_index][1]), dir_index

def run_painting_program(filename, starting_color):
    comp = IntcodeComputer()
    visited_positions = {(0,0): starting_color}
    dir_index = 1
    position = (0, 0)
    comp.read_program_from_file(filename)

    while True:
        color_of_panel = visited_positions.get(position, 0)
        new_color = comp.run_intcode_program(color_of_panel)
        turn = comp.run_intcode_program()

        if comp._is_finished:
            break

        if new_color != color_of_panel:
            visited_positions[position] = new_color
        position, dir_index = turn_robot(position, turn, dir_index)
    return visited_positions

def solution_part_one(filename):
    painted_positions = run_painting_program(filename, 0)
    print(f"Number of colored panels is {len(painted_positions)}")

if __name__ == '__main__':
    solution_part_one("Day11Input.txt")
