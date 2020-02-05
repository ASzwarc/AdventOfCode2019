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
    def get_quantity(count, no):
        if count > no:
            a = count // no
            if count % no != 0:
                a += 1
        else:
            a = no
        return a

    reactions = {}
    for key, value in input_dict.items():
        reactions[key.split()[1]] = {'no': int(key.split()[0]),
            'ing': {e.split()[1]: int(e.split()[0]) for
                    e in value.split(', ')}}

    reactions_queue = [('FUEL', 1)]
    basic_ingredients = {}
    while reactions_queue:
        reaction = reactions_queue.pop(0)
        formula = reactions.get(reaction[0])
        print(f"{reaction} -> {formula}")
        for element, count in formula['ing'].items():
            if element == 'ORE':
                if reaction[0] in basic_ingredients:
                    basic_ingredients[reaction[0]] += reaction[1]
                else:
                    basic_ingredients[reaction[0]] = reaction[1]
            else:
                print(f"Added {count*reaction[1]} {element}")
                reactions_queue.append((element, count*reaction[1]))
    ore_count = 0
    for element, count in basic_ingredients.items():
        formula = reactions.get(element)
        a = get_quantity(count, formula['no']) * formula['ing']['ORE']
        print(f"For {count} {element} adding {a} ORE")
        ore_count += a
    print(basic_ingredients)
    print(ore_count)
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
    test_input2 = {'5 NZVS': '157 ORE',
                   '6 DCFZ': '165 ORE',
                   '1 FUEL': '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ',
                   '9 QDVJ': '12 HKGWZ, 1 GPVTF, 8 PSHF',
                   '7 PSHF': '179 ORE',
                   '5 HKGWZ': '177 ORE',
                   '2 XJWVT': '7 DCFZ, 7 PSHF',
                   '2 GPVTF': '165 ORE',
                   '8 KHKGT': '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF'}
    assert(165 == solution_part_one(test_input1))
    assert(13312 == solution_part_one(test_input2))
