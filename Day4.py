
def solution_part_one(range_min, range_max):
    def check_conditions(number):
        two_same = False
        digit_list = [int(digit) for digit in str(number)]
        for i in range(len(digit_list) - 1):
            if digit_list[i] > digit_list[i+1]:
                return False, two_same
            if digit_list[i] == digit_list[i+1]:
                two_same = True
        return True, two_same

    password_no = 0
    for number in range(range_min, range_max):
        digits_not_decrease, two_same_digits = check_conditions(number)
        if digits_not_decrease and two_same_digits:
            password_no += 1
    print(f"Number of passwords in [{range_min}, {range_max}] = {password_no}")

def solution_part_two(range_min, range_max):
    def conditions_met(number):
        digit_list = [int(digit) for digit in str(number)]
        for i in range(len(digit_list) - 1):
            if digit_list[i] > digit_list[i+1]:
                return False
        # I don't like this solution.
        # You could save two indexes: start and end, which would move as group
        # expands. In the end only size of group needs to be checked:
        # (end - start) + 1
        i = 1
        group_digit = digit_list[0]
        group_size = 1
        while i < len(digit_list):
            if group_digit == digit_list[i]:
                group_size += 1
                i += 1
            elif group_digit != digit_list[i]:
                if group_size == 2:
                    return True
                group_digit = digit_list[i]
                group_size = 1
                i += 1
        if group_size == 2:
            return True
        else:
            return False

    password_no = 0
    for number in range(range_min, range_max):
        if conditions_met(number):
            password_no += 1
    print(f"Number of passwords in [{range_min}, {range_max}] = {password_no}")

if __name__ == '__main__':
    solution_part_one(124075, 580769)
    solution_part_two(124075, 580769)
