import pytest

from adventofcode2021 import day_03

from .utils import load_file


@pytest.fixture
def input_file():
    return load_file("input/day_03.txt")


def test_day_03_part_one(input_file):
    part_one_answer = day_03.calculate_power_consumption(input_file)
    assert part_one_answer == 3958484
