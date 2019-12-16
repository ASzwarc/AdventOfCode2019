from itertools import combinations

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
        # print(f"After {step + 1} step:")
        # for moon in velocity_list:
        #     print(moon)
        # print("Positions:")
        # for moon in position_list:
        #     print(moon)
    total_energy = 0
    for moon in range(4):
        total_energy += (sum([abs(axis) for axis in position_list[moon]]) *
                         sum([abs(axis) for axis in velocity_list[moon]]))
    print(f"TOTAL ENERGY: {total_energy}")



if __name__ == '__main__':
    # Test input
    # input_list = [[-1, 0, 2],
    #               [2, -10, -7],
    #               [4, -8, 8],
    #               [3, 5, -1]]
    input_list = [[-14,  -4, -11],
                  [ -9,   6,  -7],
                  [  4,   1,   4],
                  [  2, -14,  -9]]

    solution_part_one(input_list, 1000)