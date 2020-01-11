from IntcodeComputer import IntcodeComputer
from matplotlib import pyplot as plt

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

def solution_part_two(filename):
    painted_positions = run_painting_program(filename, 1)
    x = []
    y = []
    for position, color in painted_positions.items():
        if color == 1:
            x.append(position[0])
            y.append(position[1])

    plt.scatter(x, y, marker='o')
    plt.show()

if __name__ == '__main__':
    solution_part_one("Day11Input.txt")
    solution_part_two("Day11Input.txt")
