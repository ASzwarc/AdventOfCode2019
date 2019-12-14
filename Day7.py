from itertools import permutations

def run_intcode_program(input_list, phase_setting, amp_input_signal):

    def analyze_opcode(ptr):
        opcode_list = [digit for digit in str(input_list[ptr])]
        oper = int("".join(opcode_list[-2::]))
        indexes = []
        for mode in opcode_list[-3::-1]:
            ptr += 1
            if mode == "0": # position mode
                indexes.append(input_list[ptr])
            else: # immediate mode
                indexes.append(ptr)
        if (oper == 1 or oper == 2 or oper == 7 or oper == 8):
            required_length = 3
        elif oper == 5 or oper == 6:
            required_length = 2
        else: # oper == 3 or oper == 4
            required_length = 1

        while len(indexes) < required_length:
            ptr += 1
            indexes.append(input_list[ptr])
        return oper, indexes

    output_val = None
    ptr = 0
    phase_setting_set = False
    while True:
        oper, indexes = analyze_opcode(ptr)
        if oper == 1:
            input_list[indexes[2]] = (input_list[indexes[0]] +
                input_list[indexes[1]])
            if ptr != indexes[2]:
                ptr += 4
        elif oper == 2:
            input_list[indexes[2]] = (input_list[indexes[0]] *
                input_list[indexes[1]])
            if ptr != indexes[2]:
                ptr += 4
        elif oper == 3:
            if phase_setting_set:
                input_list[input_list[ptr + 1]] = amp_input_signal
            else:
                input_list[input_list[ptr + 1]] = phase_setting
                phase_setting_set = True
            ptr += 2
        elif oper == 4:
            output_val = input_list[input_list[ptr + 1]]
            ptr += 2
        elif oper == 5: # jump-if-true
            if input_list[indexes[0]] != 0:
                ptr = input_list[indexes[1]]
            else:
                ptr += 3
        elif oper == 6: # jump-if-false
            if input_list[indexes[0]] == 0:
                ptr = input_list[indexes[1]]
            else:
                ptr += 3
        elif oper == 7: # less than
            if input_list[indexes[0]] < input_list[indexes[1]]:
                input_list[indexes[2]] = 1
            else:
                input_list[indexes[2]] = 0
            if ptr != indexes[2]:
                ptr += 4
        elif oper == 8: # equals
            if input_list[indexes[0]] == input_list[indexes[1]]:
                input_list[indexes[2]] = 1
            else:
                input_list[indexes[2]] = 0
            if ptr != indexes[2]:
                ptr += 4
        elif oper == 99:
            return output_val


def solution_part_one(input_list):
    max_configuration = None
    max_output_signal = 0
    for phase_configuration in permutations(range(5), 5):
        amp_signal = 0
        for phase_setting in phase_configuration:
            amp_signal = run_intcode_program(input_list, phase_setting,
                                             amp_signal)
        if amp_signal > max_output_signal:
            max_output_signal = amp_signal
            max_configuration = phase_configuration
    print(f"{max_configuration} -> {max_output_signal}")

if __name__ == '__main__':
    filename = "Day7Input.txt"

    with open(filename) as file:
        input_list = [int(x) for x in file.readlines()[0].rstrip().split(",")]
    # Test input
    # input_list = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    # input_list = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,
    #               23,4,23,99,0,0]
    # input_list = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,
    #               33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    solution_part_one(input_list)
