from itertools import combinations
from typing import Iterator, List, Sequence

from aoc.utils.io import open_input


def is_valid(number: int, predecessors: Sequence[int]) -> bool:
    return any(
        lhs != rhs and lhs + rhs == number for lhs, rhs in combinations(predecessors, 2)
    )


def all_consecutive_subsequences_of(sequence: Sequence[int]) -> Iterator[List[int]]:
    length = len(sequence)
    for i in range(length):
        for j in range(i, length):
            yield list(sequence[i : j + 1])


def find_first_invalid_number_in(
    sequence: Sequence[int], *, preamble_length: int
) -> int:
    return next(
        sequence[checked_index]
        for checked_index in range(preamble_length, len(sequence))
        if not is_valid(
            sequence[checked_index],
            predecessors=sequence[checked_index - preamble_length : checked_index],
        )
    )


def find_subsequence_that_sums_to(
    sum_value: int, sequence: Sequence[int], min_subsequence_length: int
) -> List[int]:
    return next(
        subsequence
        for subsequence in all_consecutive_subsequences_of(sequence)
        if len(subsequence) >= min_subsequence_length and sum(subsequence) == sum_value
    )


def run() -> None:
    with open_input(__file__) as file:
        sequence = list(map(int, file.read().splitlines()))

        # part 1
        first_invalid_number = find_first_invalid_number_in(
            sequence, preamble_length=25
        )
        print(first_invalid_number)

        # part 2
        subsequence = find_subsequence_that_sums_to(
            first_invalid_number, sequence, min_subsequence_length=2
        )
        print(min(subsequence) + max(subsequence))


if __name__ == "__main__":
    run()
