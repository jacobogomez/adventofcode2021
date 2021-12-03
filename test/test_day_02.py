import pytest

from adventofcode2021 import day_02

from .utils import load_file


@pytest.fixture
def input_file():
    return load_file("input/day_02.txt")


def test_day02_part_one(input_file):
    part_one_answer = day_02.dive(input_file)
    assert part_one_answer == 2117664


def test_day02_part_two(input_file):
    part_two_answer = day_02.dive_with_aim(input_file)
    assert part_two_answer == 2073416724
