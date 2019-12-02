def part_1() -> None:
    out = 0
    with open(r'datafiles/day1.txt', mode='r') as f:
        for module in f.readlines():
            current_module_fuel_requirements = int(int(module)/3) - 2
            out += current_module_fuel_requirements
    print(out)


def calculate_fuel_part_2(mass: int) -> int:
    new_mass = int(mass / 3) - 2
    if new_mass >= 0:
        return new_mass + calculate_fuel_part_2(new_mass)
    else:
        return 0


def part_2() -> None:
    out = 0
    with open(r'datafiles/day1.txt', mode='r') as f:
        for module in f.readlines():
            out += calculate_fuel_part_2(int(module))
    print(out)


if __name__ == '__main__':
    part_1()
    part_2()