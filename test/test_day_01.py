import pytest

from adventofcode2021 import day_01

from .utils import load_file


@pytest.fixture
def input_file():
    return list(map(int, load_file("input/day_01.txt")))


def test_day01_part_one(input_file):
    part_one_answer = day_01.sonar_sweep(input_file)
    assert part_one_answer == 1393


def test_day01_part_two(input_file):
    part_two_answer = day_01.sonar_sweep_sliding_window(input_file)
    assert part_two_answer == 1359
