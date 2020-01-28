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

def solution_part_one(input_dict):
    def get_basic_ingredients_for(name, count, basic_formula):
        formula = reactions.get(name)
        for elem, quan in formula['ing'].items():
            if len(reactions.get(elem)['ing']) == 1:
                print(f"Adding {quan} {elem}")
                if elem in basic_formula:
                    basic_formula[elem] += quan * count
                else:
                    basic_formula[elem] = quan * count
            else:
                print("Searching ingredients for " + elem)
                get_basic_ingredients_for(elem, quan, basic_formula)

    reactions = {}
    for key, value in input_dict.items():
        reactions[key.split()[1]] = {'no': int(key.split()[0]),
            'ing': {e.split()[1]: int(e.split()[0]) for
                    e in value.split(', ')}}
    basic_formula = {}
    get_basic_ingredients_for('FUEL', 1, basic_formula)
    ore_count = 0
    for key, value in basic_formula.items():
        a = reactions[key]['no']
        b = reactions[key]['ing']['ORE']
        mod = value % a
        if mod == 0:
            ore_count += (value // a) * b
        else:
            ore_count += ((value // a) + 1) * b
    return ore_count


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
