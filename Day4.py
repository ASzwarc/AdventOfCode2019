
def solution_part_one(range_min, range_max):
    def check_conditions(number):
        not_decrease = True
        two_same = False
        digit_list = [int(digit) for digit in str(number)]
        for i in range(len(digit_list) - 1):
            if digit_list[i] > digit_list[i+1]:
                not_decrease = False
                break
            if digit_list[i] == digit_list[i+1]:
                two_same = True
        return not_decrease, two_same

    password_no = 0
    for number in range(range_min, range_max):
        digits_not_decrease, two_same_digits = check_conditions(number)
        if digits_not_decrease and two_same_digits:
            password_no += 1
    print(f"Number of passwords in [{range_min}, {range_max}] = {password_no}")

if __name__ == '__main__':
    solution_part_one(124075, 580769)