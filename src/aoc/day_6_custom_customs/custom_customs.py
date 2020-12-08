from functools import reduce
from itertools import chain
from typing import List

from more_itertools import split_at

from aoc.utils.io import open_input


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        groups: List[List[str]] = list(split_at(lines, lambda line: line == ""))

        # part 1
        result = sum(len(set(chain.from_iterable(group))) for group in groups)
        print(result)

        # part 2
        result = sum(
            len(reduce(set.intersection, map(set, group)))  # type: ignore
            for group in groups
        )
        print(result)


if __name__ == "__main__":
    run()