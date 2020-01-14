import math

def solution_part_one(filename):
    with open(filename) as file:
        asteroid_map = [[sign for sign in input_line.rstrip()] for input_line
                        in file.readlines()]
    result = get_asteroids_visibility(asteroid_map)
    return max(result, key=lambda k: result[k])

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_between(point_start, point_between, point_end):
    return (distance(point_start, point_between)
            + distance(point_between, point_end)
            == distance(point_start, point_end))

def get_asteroids_visibility(asteroids_map):
    asteroids_visibility = {}
    return asteroids_visibility


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
    # Result: best should be (5, 8) with 33 asteroids detected
    print(get_asteroids_visibility(test_input_map))
    solution_part_one("Day10Input.txt")