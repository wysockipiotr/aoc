from contextlib import suppress
from functools import reduce
from itertools import product
from operator import mul
from pathlib import Path
from typing import Iterable, Iterator, Set


def read_numbers_from_file(path: Path) -> Iterator[int]:
    with path.open("r") as file:
        for line in file.readlines():
            with suppress(ValueError):
                yield int(line)


def pick_numbers_that_sum_to(
    sum_value: int, *, n_picked_numbers: int, numbers: Iterable[int]
) -> Iterator[Set[int]]:
    for number_pair in product(numbers, repeat=n_picked_numbers):
        if sum(number_pair) == sum_value:
            yield set(number_pair)


def run() -> None:
    filepath = Path(__file__).parent / "input"
    numbers = next(
        pick_numbers_that_sum_to(
            2020,
            n_picked_numbers=3,
            numbers=read_numbers_from_file(filepath),
        )
    )
    print(numbers)
    print(reduce(mul, numbers, 1))


if __name__ == "__main__":
    run()
