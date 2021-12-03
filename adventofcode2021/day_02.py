"""Solution for Advent of Code 2021 - Day 2: Dive!

Puzzle prompt available at https://adventofcode.com/2021/day/2.
"""


def dive(instructions: list) -> int:
    horizontal_position = 0
    depth = 0

    for instruction in instructions:
        split_instruction = instruction.split()
        if split_instruction[0] == "forward":
            horizontal_position += int(split_instruction[1])
        if split_instruction[0] == "down":
            depth += int(split_instruction[1])
        if split_instruction[0] == "up":
            depth -= int(split_instruction[1])

    return horizontal_position * depth


def dive_with_aim(instructions: list) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        split_instruction = instruction.split()
        if split_instruction[0] == "forward":
            horizontal_position += int(split_instruction[1])
            depth += aim * int(split_instruction[1])
        if split_instruction[0] == "down":
            aim += int(split_instruction[1])
        if split_instruction[0] == "up":
            aim -= int(split_instruction[1])

    return horizontal_position * depth
