import math

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
    vaporisation_order = []
    asteroids_pos.remove(laser_pos)
    for x, y in asteroids_pos:
        in_line = []
        angle = -math.atan2(y - laser_pos[1], x - laser_pos[0])
        d = math.sqrt((x - laser_pos[0]) ** 2 + (y - laser_pos[1]) ** 2)
        for x2, y2 in asteroids_pos:
            if (x, y) != (x2, y2):
                angle2 = -math.atan2(y2 - laser_pos[1], x2 - laser_pos[0])
                if angle == angle2:
                    d2 = math.sqrt((x2 - laser_pos[0]) ** 2 +
                                   (y2 - laser_pos[1]) ** 2)
                    in_line.append((x2, y2, d2))
        in_line.append((x, y, d))
        in_line.sort(key=lambda tup: tup[2])
        offset = 0
        for x, y, _ in in_line:
            vaporisation_order.append((x, y, angle + offset))
            offset += 2*math.pi
    vaporisation_order.sort(key=lambda tup: tup[2])
    for no, element in enumerate(vaporisation_order):
        print(f"{no+1}: ({element[0]}, {element[1]}) = {element[2]}")
    # return vaporisation_order[199]


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
