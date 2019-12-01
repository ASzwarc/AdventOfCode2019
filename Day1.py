
def basic_fuel_requirement(rows):
    fuel_requirement = 0
    for line in rows:
        fuel_requirement += (int(line.rstrip('\n')) // 3 - 2)
    print(f"Full fuel requirement {fuel_requirement}")

def module_full_fuel_requirement(rows):
    def calculate_full_fuel(basic_fuel: int) -> int:
        full_fuel = 0
        while basic_fuel > 0:
            full_fuel += basic_fuel
            basic_fuel = basic_fuel // 3 - 2
        return full_fuel

    full_fuel_requirement = 0
    for line in rows:
        basic_fuel = int(line.rstrip('\n')) // 3 - 2
        full_fuel_requirement += calculate_full_fuel(basic_fuel)
    print(f"Full fuel requirement for each module {full_fuel_requirement}")

def main(filename):
    with open(filename) as file:
        rows = file.readlines()
        basic_fuel_requirement(rows)
        module_full_fuel_requirement(rows)

if __name__ == "__main__":
    main("Day1Input.txt")
