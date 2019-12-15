def solution_part_one(input_list, image_size):
    min_zeros = 10000000000
    one_times_two_len = 0
    step = image_size[0] * image_size[1]
    for it in range(0, len(input_list), step):
        zeros = input_list[it:it+step].count(0)
        if zeros < min_zeros:
            min_zeros = zeros
            ones = input_list[it:it+step].count(1)
            twos = input_list[it:it+step].count(2)
            one_times_two_len = ones * twos
    print(f"Number of 1s times number of 2s is {one_times_two_len}")

if __name__ == '__main__':
    filename = "Day8Input.txt"
    with open(filename) as file:
        input_list = [int(digit) for digit in file.readlines()[0].rstrip()]

    image_size = (25, 6)
    solution_part_one(input_list, image_size)