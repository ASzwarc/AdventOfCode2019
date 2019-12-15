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


def solution_part_two(input_list, image_size):
    def evaluate_layers(input_index):
        step = image_size[0] * image_size[1]
        for elem in range(input_index, len(input_list), step):
            if input_list[elem] == 0:
                return "#"
            elif input_list[elem] == 1:
                return "$"
            else: # elem == 2
                continue

    output_image = [["#" for row in range(image_size[0])]
                    for col in range(image_size[1])]

    for row in range(image_size[1]):
        for col in range(image_size[0]):
            input_index = row*image_size[0] + col
            output_image[row][col] = evaluate_layers(input_index)

    for row in output_image:
        print(row)

if __name__ == '__main__':
    filename = "Day8Input.txt"
    with open(filename) as file:
        input_list = [int(digit) for digit in file.readlines()[0].rstrip()]

    image_size = (25, 6)
    #solution_part_one(input_list, image_size)
    # Test input:
    # input_list = [0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0]
    # image_size = (2, 2)
    solution_part_two(input_list, image_size)