from itertools import combinations
from copy import deepcopy
from math import gcd

def solution_part_one(position_list, steps_no):
    velocity_list = [[0, 0, 0] for _ in range(4)]
    for step in range(steps_no):
        for moon_pair in combinations(range(4), 2):
            for axis in range(3):
                moon_one = moon_pair[0]
                moon_two = moon_pair[1]
                if position_list[moon_one][axis] < position_list[moon_two][axis]:
                    velocity_list[moon_one][axis] += 1
                    velocity_list[moon_two][axis] -= 1
                elif position_list[moon_one][axis] > position_list[moon_two][axis]:
                    velocity_list[moon_one][axis] -= 1
                    velocity_list[moon_two][axis] += 1
        for moon_no, _ in enumerate(position_list):
            for axis in range(3):
                position_list[moon_no][axis] += velocity_list[moon_no][axis]
    total_energy = 0
    for moon in range(4):
        total_energy += (sum([abs(axis) for axis in position_list[moon]]) *
                         sum([abs(axis) for axis in velocity_list[moon]]))
    print(f"TOTAL ENERGY: {total_energy}")


def solution_part_two(position_list):
    velocity_list = [[0, 0, 0] for _ in range(4)]
    starting_points_list = deepcopy(position_list)
    found_steps = [-1 for _ in range(3)]
    step = 1
    points_to_find = 3
    while points_to_find > 0:
        for moon_pair in combinations(range(4), 2):
            for axis in range(3):
                moon_one = moon_pair[0]
                moon_two = moon_pair[1]
                if position_list[moon_one][axis] < position_list[moon_two][axis]:
                    velocity_list[moon_one][axis] += 1
                    velocity_list[moon_two][axis] -= 1
                elif position_list[moon_one][axis] > position_list[moon_two][axis]:
                    velocity_list[moon_one][axis] -= 1
                    velocity_list[moon_two][axis] += 1
        for moon_no, _ in enumerate(position_list):
            for axis in range(3):
                position_list[moon_no][axis] += velocity_list[moon_no][axis]
        for axis_no in range(len(position_list[0])):
            moon_count = 0
            for moon_no in range(len(position_list)):
                if ((starting_points_list[moon_no][axis_no] ==
                        position_list[moon_no][axis_no]) and
                    (velocity_list[moon_no][axis_no] == 0) and
                    (found_steps[axis_no] == -1)):
                    moon_count += 1
            if moon_count == len(position_list):
                found_steps[axis_no] = step
                points_to_find -= 4
                print(f"Found point for axis {axis_no} in step {step}")
        step += 1
    unique_steps = list(set(found_steps))
    lcm = unique_steps[0]
    for step in unique_steps[1:]:
        lcm = (lcm * step) // gcd(lcm, step)
    print(f"Moon will return to starting point in {lcm} steps")


if __name__ == '__main__':
    # Test input
    input_list = [[-1, 0, 2],
                  [2, -10, -7],
                  [4, -8, 8],
                  [3, 5, -1]]
    # input_list = [[-14,  -4, -11],
    #               [ -9,   6,  -7],
    #               [  4,   1,   4],
    #               [  2, -14,  -9]]

    # solution_part_one(input_list, 1000)
    solution_part_two(input_list)