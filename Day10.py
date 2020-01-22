import math
from collections import OrderedDict

def parse_input(filename):
    asteroid_pos = []
    with open(filename) as file:
        for row_no, row in enumerate(file.readlines()):
            for col_no, col in enumerate(row.rstrip()):
                if col == "#":
                    asteroid_pos.append((col_no, row_no))
    return asteroid_pos

def get_asteroids_visibility(asteroids_pos):
    best_score = 0
    best_x, best_y = -1, -1
    for x, y in asteroids_pos:
        visible_asteroids = set()
        for x2, y2 in asteroids_pos:
            if (x, y) != (x2, y2):
                visible_asteroids.add(math.atan2(y2 - y, x2 - x))
        if len(visible_asteroids) > best_score:
            best_score = len(visible_asteroids)
            best_x, best_y = x, y
    return best_score, (best_x, best_y)


def get_200th_vaporized_asteroid(asteroids_pos, laser_pos):
    a_by_angle = {}
    asteroids_pos.remove(laser_pos)
    half_pi = math.pi / 2
    for x, y in asteroids_pos:
        asteroids = []
        angle = math.degrees(math.atan2(y - laser_pos[1], x - laser_pos[0]) + half_pi)
        if angle < 0:
            angle += 360.0
        d = math.sqrt((x - laser_pos[0]) ** 2 + (y - laser_pos[1]) ** 2)
        if angle in a_by_angle:
            asteroids = a_by_angle[angle][:]
        asteroids.append((x, y, d))
        asteroids.sort(key=lambda tup: tup[2])
        a_by_angle[angle] = asteroids
    sorted_a_by_angle = OrderedDict(sorted(a_by_angle.items(),
                                           key=lambda x: x[0]))

    a_index = 200 // len(sorted_a_by_angle)
    key_no = 199 - a_index * len(sorted_a_by_angle)
    a_key = list(sorted_a_by_angle.keys())[key_no]
    asteroid = sorted_a_by_angle[a_key][a_index]
    print(f"200th asteroid is ({asteroid[0]},{asteroid[1]})")
    return asteroid[0] * 100 + asteroid[1]

if __name__ == '__main__':
    test_input_map = [
        ['.', '#', '.', '.', '#', '#', '.', '#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.'],
        ['.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '.'],
        ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '.', '#', '#', '#', '.', '#', '#'],
        ['.', '.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.', '#', '.', '#', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.'],
        ['.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '.', '#', '#', '.', '.', '#'],
        ['.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
        ['.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#'],
        ['.', '.', '.', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#'],
        ['.', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#']
    ]
    positions = [(x, y) for y, row in enumerate(test_input_map)
                 for x, elem in enumerate(row) if elem == '#']
    # Result: best should be (5, 8) with 33 asteroids detected
    print(get_asteroids_visibility(positions))
    part_one_result = get_asteroids_visibility(parse_input("Day10Input.txt"))
    print(f"Part one result: {part_one_result}")

    test2_input_map = [
        ['.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '.', '.'],
        ['#', '#', '.', '.', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '.', '#', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '#', '#', '#', '#', '#', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '#', '#', '.', '.'],
        ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#']
    ]
    positions = [(x, y) for y, row in enumerate(test2_input_map)
                 for x, elem in enumerate(row) if elem == '#']
    get_200th_vaporized_asteroid(positions, (8, 3))
