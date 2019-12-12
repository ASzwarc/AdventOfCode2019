import re

def parse_input(filename):
    input_list = []
    pattern = re.compile(r"(\S{3})\)(\S{3})")

    with open(filename) as file:
        input_list = [re.match(pattern, line).group(1, 2)
                      for line in file.readlines()]
    return input_list


def solution_part_one(input_list):
    pass

if __name__ == '__main__':
    input_list = parse_input("Day6Input.txt")
    solution_part_one(input_list)
