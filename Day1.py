
def basic_fuel_requirement(rows):
    fuel_requirement = 0
    for line in rows:
        fuel_requirement += (int(line.rstrip('\n')) // 3 - 2)
    print(f"Full fuel requirement {fuel_requirement}")

def main(filename):
    with open(filename) as file:
        rows = file.readlines()
        basic_fuel_requirement(rows)
        module_full_fuel_requirement(rows)

if __name__ == "__main__":
    main("Day1Input.txt")
