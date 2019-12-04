
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

        start = 0
        end = 1
        while end < len(digit_list):
            if digit_list[start] != digit_list[end]:
                if end - start == 2:
                    return True
                start = end
            end += 1
        if end - start == 2:
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
