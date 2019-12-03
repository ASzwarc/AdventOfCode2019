from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
starting_point = Point(8000, 8000)

def solution_part_one(filename):
    def create_segments(wire_path):
        segment_list = [starting_point]
        for path in wire_path:
            if path[0] == 'R':
                new_point = Point(segment_list[-1].x + int(path[1:]),
                                  segment_list[-1].y)
            elif path[0] == 'L':
                new_point = Point(segment_list[-1].x - int(path[1:]),
                                  segment_list[-1].y)
            elif path[0] == 'U':
                new_point = Point(segment_list[-1].x,
                                  segment_list[-1].y + int(path[1:]))
            elif path[0] == 'D':
                new_point = Point(segment_list[-1].x,
                                  segment_list[-1].y - int(path[1:]))
            else:
                print(f"This shouldn't happen on {path}")
                return
            segment_list.append(new_point)
        return segment_list

    wire_one = []
    wire_two = []
    with open(filename) as input:
        wire_one = input.readline().rstrip('\n').split(',')
        wire_two = input.readline().rstrip('\n').split(',')

    wire_one_segments = create_segments(wire_one)
    wire_two_segments = create_segments(wire_two)
    distance = 1000000000
    for a in range(len(wire_one_segments) - 1):
        for b in range(len(wire_two_segments) - 1):
            point_a = Point(wire_one_segments[a].x, wire_one_segments[a].y)
            point_a_prim = Point(wire_one_segments[a+1].x, wire_one_segments[a+1].y)
            point_b = Point(wire_two_segments[b].x, wire_two_segments[b].y)
            point_b_prim = Point(wire_two_segments[b+1].x, wire_two_segments[b+1].y)
            # a horizontal, b vertical
            if (point_a.y - point_a_prim.y == 0) and (point_b.x - point_b_prim.x == 0):
                x_in_range = ((point_a.x <= point_b.x and
                               point_b.x <= point_a_prim.x)
                              or (point_a_prim.x <= point_b.x and
                                  point_b.x <= point_a.x))
                y_in_range = ((point_b.y <= point_a.y and
                               point_a.y <= point_b_prim.y)
                             or (point_b_prim.y <= point_a.y and
                                 point_a.y <= point_b.y))
                if x_in_range and y_in_range:
                    found_distance = abs(point_b.x - starting_point.x) + abs(point_a.y - starting_point.y)
                    if found_distance < distance:
                        distance = found_distance
                    print(f"Found intersection I = ({point_b.x}, {point_a.y}) between Pa = [({point_a.x}, {point_a.y}), ({point_a_prim.x}, {point_a_prim.y})] and Pb [({point_b.x}, {point_b.y}), ({point_b_prim.x}, {point_b_prim.y})]")
                    print(f"Found distance: {found_distance}")
            # a vertical, b horizontal
            elif (point_a.x - point_a_prim.x == 0) and (point_b.y - point_b_prim.y == 0):
                x_in_range = ((point_b.x <= point_a.x and
                               point_a.x <= point_b_prim.x) or
                             (point_b_prim.x <= point_a.x and
                              point_a.x <= point_b.x))
                y_in_range = ((point_a.y <= point_b.y and
                               point_b.y <= point_a_prim.y) or
                             (point_a_prim.y <= point_b.y and
                              point_b.y <= point_a.y))
                if x_in_range and y_in_range:
                    found_distance = abs(point_a.x - starting_point.x) + abs(point_b.y - starting_point.y)
                    if found_distance < distance:
                        distance = found_distance
                    print(f"Found intersection I = ({point_a.x}, {point_b.y}) between Pa = [({point_a.x}, {point_a.y}), ({point_a_prim.x}, {point_a_prim.y})] and Pb [({point_b.x}, {point_b.y}), ({point_b_prim.x}, {point_b_prim.y})]")
                    print(f"Found distance: {found_distance}")
    print(f"DISTANCE: {distance}")

if __name__ == '__main__':
    solution_part_one("Day3Input.txt")