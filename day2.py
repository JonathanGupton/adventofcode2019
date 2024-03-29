from typing import List, NewType


IntCode = NewType("IntCode", List[int])


def add(a: int, b: int) -> int:
    return a + b


def multi(a: int, b: int) -> int:
    return a * b


def parse_int_code(int_code: IntCode, param_1: int, param_2: int) -> IntCode:
    """
    Process int code instructions over four-integer groups:
    Int 1 -  Action - 1: add, 2: multi, 99: halt
    Int 2 & 3 - Indicate the values in the list to perform the action on
    Int 4 - Where to store the new value in the list
    """
    int_code = int_code.copy()
    int_code[1], int_code[2] = param_1, param_2
    instr_ptr = 0
    action = {1: add, 2: multi}
    while not int_code[instr_ptr] == 99:
        int_code[int_code[instr_ptr + 3]] = action[int_code[instr_ptr]](
            int_code[int_code[instr_ptr + 1]], int_code[int_code[instr_ptr + 2]]
        )
        instr_ptr += 4
    else:
        return int_code


def part1(int_code: IntCode) -> None:
    """Prints the answer for Day 2 Part 1"""
    print(parse_int_code(int_code, 12, 2)[0])


def part2(int_code, max_i=100, max_j=100) -> None:
    """prints the answer for Day 2 Part 2"""
    for i in range(max_i):
        for j in range(max_j):
            if parse_int_code(int_code, i, j)[0] == 19690720:
                print(100 * i + j)
                return


if __name__ == "__main__":
    with open(r"datafiles\day2.txt", mode="r") as f:
        input_code = [int(code) for code in f.readline().split(",")]

    part1(input_code)
    part2(input_code)
