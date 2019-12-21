
class IntcodeComputer():
    def __init__(self):
        self._program = []
        self._ptr = 0
        self._relative_base = 0

    def read_program_instructions(self, program_list):
        self._program = program_list[:]
        self._ptr = 0

    def read_program_from_file(self, filename):
        with open(filename) as file:
            input_list = [int(x) for x in
                          file.readlines()[0].rstrip().split(",")]
        self.read_program_instructions(input_list)

    def _analyze_opcode(self):
        ptr = self._ptr
        opcode_list = [digit for digit in str(self._program[ptr])]
        oper = int("".join(opcode_list[-2::]))
        indexes = []
        for mode in opcode_list[-3::-1]:
            ptr += 1
            if mode == "0": # position mode
                indexes.append(self._program[ptr])
            else: # immediate mode
                indexes.append(ptr)
        if (oper == 1 or oper == 2 or oper == 7 or oper == 8):
            required_length = 3
        elif oper == 5 or oper == 6:
            required_length = 2
        elif oper == 3 or oper == 4 or oper == 9:
            required_length = 1
        else: # oper == 99:
            required_length = 0

        while len(indexes) < required_length:
            ptr += 1
            indexes.append(self._program[ptr])
        return oper, indexes

    def less_than(self, indexes):
        if self._program[indexes[0]] < self._program[indexes[1]]:
            self._program[indexes[2]] = 1
        else:
            self._program[indexes[2]] = 0
        if self._ptr != indexes[2]:
            self._ptr += 4

    def equals(self, indexes):
        if self._program[indexes[0]] == self._program[indexes[1]]:
            self._program[indexes[2]] = 1
        else:
            self._program[indexes[2]] = 0
        if self._ptr != indexes[2]:
            self._ptr += 4

    def add(self, indexes):
        self._program[indexes[2]] = (self._program[indexes[0]] +
            self._program[indexes[1]])
        if self._ptr != indexes[2]:
            self._ptr += 4

    def multiply(self, indexes):
        self._program[indexes[2]] = (self._program[indexes[0]] *
            self._program[indexes[1]])
        if self._ptr != indexes[2]:
            self._ptr += 4

    def save_input_value(self, input_value):
            self._program[self._program[self._ptr + 1]] = input_value
            self._ptr += 2

    def read_output_value(self):
            output_val = self._program[self._program[self._ptr + 1]]
            self._ptr += 2
            return output_val

    def jump_if_true(self, indexes):
        if self._program[indexes[0]] != 0:
            self._ptr = self._program[indexes[1]]
        else:
            self._ptr += 3

    def jump_if_false(self, indexes):
        if self._program[indexes[0]] == 0:
            self._ptr = self._program[indexes[1]]
        else:
            self._ptr += 3

    def run_intcode_program(self, input_value):
        output_val = None
        while True:
            oper, indexes = self._analyze_opcode()
            if oper == 1:
                self.add(indexes)
            elif oper == 2:
                self.multiply(indexes)
            elif oper == 3:
                self.save_input_value(input_value)
            elif oper == 4:
                output_val = self.read_output_value()
            elif oper == 5:
                self.jump_if_true(indexes)
            elif oper == 6: # jump-if-false
                self.jump_if_false(indexes)
            elif oper == 7: # less than
                self.less_than(indexes)
            elif oper == 8: # equals
                self.equals(indexes)
            elif oper == 99:
                print(f"Intcode finished! Output: {output_val}")
                return output_val

