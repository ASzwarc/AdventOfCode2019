import re

def parse_input_file(filename):
    input_dict = {}
    pattern = re.compile(r"(.*) => (.*)")
    with open(filename) as f:
        for line in f:
            m = re.match(pattern, line)
            if m:
                input_dict[m.group(2)] = m.group(1)
    return input_dict

if __name__ == '__main__':
    # Simple testing input
    test_input1 = {'2 A': '9 ORE',
                   '3 B': '8 ORE',
                   '5 C': '7 ORE',
                   '1 AB': '3 A, 4 B',
                   '1 BC': '5 B, 7 C',
                   '1 CA': '4 C, 1 A',
                   '1 FUEL': '2 AB, 3 BC, 4 CA'}
    assert(165 == solution_part_one(test_input1))
