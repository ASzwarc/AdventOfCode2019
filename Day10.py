import math

def solution_part_one(filename):
    asteroid_pos = []
    with open(filename) as file:
        for row_no, row in enumerate(file.readlines()):
            for col_no, col in enumerate(row.rstrip()):
                if col == "#":
                    asteroid_pos.append((col_no, row_no))
    print(get_asteroids_visibility(asteroid_pos))


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


if __name__ == '__main__':
    test_input_map = [
        ['.', '.', '.', '.', '.', '.', '#', '.', '#', '.'],
        ['#', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '#', '#', '#', '#', '#', '.'],
        ['.', '#', '.', '#', '.', '#', '#', '#', '.', '.'],
        ['.', '#', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '#', '.', '.', '.', '.', '#', '.'],
        ['.', '#', '#', '.', '#', '.', '.', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '#', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '.', '#', '#', '#', '#']
    ]
    positions = [(x, y) for y, row in enumerate(test_input_map)
                 for x, elem in enumerate(row) if elem == '#']
    # Result: best should be (5, 8) with 33 asteroids detected
    print(get_asteroids_visibility(positions))
    solution_part_one("Day10Input.txt")
