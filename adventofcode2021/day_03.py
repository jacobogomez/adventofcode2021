"""Solution for Advent of Code 2021 - Day 3: Binary Diagnostic

Puzzle prompt available at https://adventofcode.com/2021/day/3.
"""


def calculate_power_consumption(report: list) -> int:
    number_of_zeros = [0 for _ in range(len(report[0].strip()))]
    number_of_ones = [0 for _ in range(len(report[0].strip()))]

    for diagnostic in report:
        for index, value in enumerate(diagnostic.strip()):
            if value == "0":
                number_of_zeros[index] += 1
            else:
                number_of_ones[index] += 1

    gamma_rate = ""
    epsilon_rate = ""

    for index, value in enumerate(number_of_zeros):
        if value > number_of_ones[index]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    decimal_gamma_rate = int(gamma_rate, 2)
    decimal_epsilon_rate = int(epsilon_rate, 2)

    return decimal_gamma_rate * decimal_epsilon_rate
