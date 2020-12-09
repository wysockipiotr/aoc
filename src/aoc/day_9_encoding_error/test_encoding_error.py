from typing import List

import pytest

from aoc.day_9_encoding_error.encoding_error import (
    find_first_invalid_number_in,
    find_subsequence_that_sums_to,
    is_valid,
)


@pytest.fixture
def sequence() -> List[int]:
    return [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


def test_is_valid_returns_true_if_any_two_predecessors_sum_to_given_number() -> None:
    assert is_valid(4, predecessors=[1, 2, 3])


def test_is_valid_returns_false_if_no_two_predecessors_sum_to_a_given_number() -> None:
    assert not is_valid(10, predecessors=[1, 1, 1])


def test_find_first_invalid_number(sequence: List[int]) -> None:
    assert find_first_invalid_number_in(sequence, preamble_length=5) == 127


def test_find_subsequence_that_sums_to(sequence: List[int]) -> None:
    subsequence = find_subsequence_that_sums_to(127, sequence, min_subsequence_length=2)
    assert min(subsequence) + max(subsequence) == 62
