import typing as t
from collections import Counter
from functools import reduce
from itertools import permutations
from operator import mul
from typing import Dict, Iterator, List, Sequence

from more_itertools import last, windowed

from aoc.utils.io import open_input


def iterate_differences(joltages: Sequence[int]) -> Iterator[int]:
    joltages = [0, *joltages]
    for prev, nxt in windowed(joltages, n=2):
        yield nxt - prev  # type: ignore
    yield 3


def is_valid_adapters_chain(joltages: Sequence[int]) -> bool:
    return (
        joltages[0] in {1, 2, 3}
        and max(joltages) == last(joltages)
        and all(
            (nxt - prev) in {1, 2, 3}  # type: ignore
            for prev, nxt in windowed(joltages, 2)
        )
    )


def count_possible_arrangements(joltages: List[int]) -> int:
    target_rating = max(joltages) + 3
    visited: Dict[int, int] = {}
    joltages = [*joltages, target_rating]

    def count_possible_arrangements_after(rating: int) -> int:
        if rating == target_rating:
            return 1
        if rating in visited:
            return visited[rating]
        visited[rating] = sum(
            count_possible_arrangements_after(rating + offset)
            for offset in {1, 2, 3}
            if (rating + offset) in joltages
        )
        return visited[rating]

    return count_possible_arrangements_after(0)


def run() -> None:
    with open_input(__file__) as file:
        joltages = list(map(int, file.read().splitlines()))

        # part 1
        valid_adapters_chain = next(
            chain
            for chain in permutations(sorted(joltages))
            if is_valid_adapters_chain(chain)
        )
        differences_counts: t.Counter[int] = Counter(
            iterate_differences(valid_adapters_chain)
        )
        print(reduce(mul, differences_counts.values(), 1))

        # part 2
        print(count_possible_arrangements(joltages))


if __name__ == "__main__":
    run()
