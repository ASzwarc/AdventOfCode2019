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
    print(parse_input_file("Day14Input.txt"))
