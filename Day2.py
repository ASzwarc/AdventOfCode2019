
def solution_part_one(filename):
    input_list = []
    with open(filename) as file:
        input_list = [int(x) for x in file.readlines()[0].rstrip().split(",")]
    ptr = 0
    input_list[1] = 12
    input_list[2] = 2
    while True:
        opcode = input_list[ptr]
        if opcode == 1:
            input_list[input_list[ptr + 3]] = (
                input_list[input_list[ptr + 1]] +
                input_list[input_list[ptr + 2]])
        elif opcode == 2:
            input_list[input_list[ptr + 3]] = (
                input_list[input_list[ptr + 1]] *
                input_list[input_list[ptr + 2]])
        elif opcode == 99:
            print("Finished processing opcode")
            break
        ptr += 4
    print(f"Value at position 0: {input_list[0]}")


def solution_part_two(filename):
    input_list = []
    with open(filename) as file:
        input_list = [int(x) for x in file.readlines()[0].rstrip().split(",")]

    for noun in range(0, 100):
        for verb in range(0, 100):
            ptr = 0
            test_list = input_list[:]
            test_list[1] = noun
            test_list[2] = verb
            while True:
                opcode = test_list[ptr]
                if opcode == 1:
                    test_list[test_list[ptr + 3]] = (
                        test_list[test_list[ptr + 1]] +
                        test_list[test_list[ptr + 2]])
                elif opcode == 2:
                    test_list[test_list[ptr + 3]] = (
                        test_list[test_list[ptr + 1]] *
                        test_list[test_list[ptr + 2]])
                elif opcode == 99:
                    break
                ptr += 4
            if test_list[0] == 19690720:
                result = 100 * noun + verb
                print(f"Answer: {result}")

if __name__ == '__main__':
    solution_part_one("Day2Input.txt")
    solution_part_two("Day2Input.txt")
