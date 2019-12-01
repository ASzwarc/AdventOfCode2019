
def basic_fuel_requirement(file):
    fuel_requirement = 0
    for line in file.readlines():
        fuel_requirement += (int(line.rstrip('\n')) // 3 - 2)
    print(f"Full fuel requirement {fuel_requirement}")

def main(filename):
    with open(filename) as file:
        basic_fuel_requirement(file)

if __name__ == "__main__":
    main("Day1Input.txt")