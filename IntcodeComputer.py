from collections import defaultdict
import unittest

class IntcodeComputer():
    def __init__(self):
        self._program = []
        self._ptr = 0
        self._relative_base = 0
        self._memory = defaultdict(int)
        self._is_finished = False

    def get_val_at(self, index):
        if index < len(self._program):
            return self._program[index]
        else:
            return self._memory[index]

    def set_val_at(self, index, value):
        if index < len(self._program):
            self._program[index] = value
        else:
            self._memory[index] = value

    def read_program_instructions(self, program_list):
        self._program = program_list[:]

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
            elif mode == "1": # immediate mode
                indexes.append(ptr)
            else: # relative mode
                indexes.append(self._program[ptr] + self._relative_base)
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
        if self.get_val_at(indexes[0]) < self.get_val_at(indexes[1]):
            self.set_val_at(indexes[2], 1)
        else:
            self.set_val_at(indexes[2], 0)
        self._ptr += 4

    def equals(self, indexes):
        if self.get_val_at(indexes[0]) == self.get_val_at(indexes[1]):
            self.set_val_at(indexes[2], 1)
        else:
            self.set_val_at(indexes[2], 0)
        self._ptr += 4

    def add(self, indexes):
        result = self.get_val_at(indexes[0]) + self.get_val_at(indexes[1])
        self.set_val_at(indexes[2], result)
        self._ptr += 4

    def multiply(self, indexes):
        result = self.get_val_at(indexes[0]) * self.get_val_at(indexes[1])
        self.set_val_at(indexes[2], result)
        self._ptr += 4

    def save_input_value(self, input_value, indexes):
        self.set_val_at(indexes[0], input_value)
        self._ptr += 2

    def read_output_value(self, indexes):
        output_val = self.get_val_at(indexes[0])
        self._ptr += 2
        return output_val

    def jump_if_true(self, indexes):
        if self.get_val_at(indexes[0]) != 0:
            self._ptr = self.get_val_at(indexes[1])
        else:
            self._ptr += 3

    def jump_if_false(self, indexes):
        if self.get_val_at(indexes[0]) == 0:
            self._ptr = self.get_val_at(indexes[1])
        else:
            self._ptr += 3

    def change_relative_base(self, indexes):
        self._relative_base += self.get_val_at(indexes[0])
        self._ptr += 2

    def run_intcode_program(self, input_value=None):
        while not self._is_finished:
            oper, indexes = self._analyze_opcode()
            # print(f"Operation {oper} on indexes {indexes}")
            if oper == 1:
                self.add(indexes)
            elif oper == 2:
                self.multiply(indexes)
            elif oper == 3:
                self.save_input_value(input_value, indexes)
            elif oper == 4:
                return self.read_output_value(indexes)
            elif oper == 5:
                self.jump_if_true(indexes)
            elif oper == 6: # jump-if-false
                self.jump_if_false(indexes)
            elif oper == 7: # less than
                self.less_than(indexes)
            elif oper == 8: # equals
                self.equals(indexes)
            elif oper == 9:
                self.change_relative_base(indexes)
            elif oper == 99:
                print(f"Intcode FINISHED")
                self._is_finished = True
                return None


class TestIntcodeComputer(unittest.TestCase):

    def test_quine(self):
        computer = IntcodeComputer()
        input_list = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        computer.read_program_instructions(input_list)
        output_list = []
        is_finished = False
        while not is_finished:
            ret_val = computer.run_intcode_program()
            if ret_val is None:
                is_finished = True
            else:
                output_list.append(ret_val)

        self.assertTrue(computer._is_finished)
        self.assertEqual(output_list, input_list)

    def test_return_16_digit_number(self):
        computer = IntcodeComputer()
        input_list = [1102,34915192,34915192,7,4,7,99,0]
        computer.read_program_instructions(input_list)
        ret_val = computer.run_intcode_program()
        final_code = computer.run_intcode_program()

        self.assertTrue(computer._is_finished)
        self.assertEqual(ret_val, 1219070632396864)
        self.assertIsNone(final_code)

    def test_return_number_in_the_middle_of_output(self):
        computer = IntcodeComputer()
        input_list = [104,1125899906842624,99]
        computer.read_program_instructions(input_list)
        ret_val = computer.run_intcode_program()
        final_code = computer.run_intcode_program()

        self.assertTrue(computer._is_finished)
        self.assertEqual(ret_val, 1125899906842624)
        self.assertIsNone(final_code)

if __name__ == '__main__':
    unittest.main()
