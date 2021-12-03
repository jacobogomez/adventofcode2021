"""Solution for Advent of Code 2021 - Day 1: Sonar Sweep

Puzzle prompt available at https://adventofcode.com/2021/day/1.
"""


def sonar_sweep(measurements: list) -> int:
    larger_measurements = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            larger_measurements += 1

    return larger_measurements


def sonar_sweep_sliding_window(measurements: list) -> int:
    larger_sums = 0

    for i in range(len(measurements) - 3):
        first_window = sum(measurements[i : i + 3])
        second_window = sum(measurements[i + 1 : i + 4])

        if second_window > first_window:
            larger_sums += 1

    return larger_sums
