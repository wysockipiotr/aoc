from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Iterable, Set, Tuple

from more_itertools import divide, first, last, one, windowed

from aoc.utils.io import open_input

NUMBER_OF_ROWS: Final = 128
NUMBER_OF_COLUMNS: Final = 8
FRONT: Final = "F"
BACK: Final = "B"
LEFT: Final = "L"
RIGHT: Final = "R"


def take_lower_half(rng: range) -> range:
    items = list(first(divide(2, rng)))
    return range(first(items), last(items) + 1)


def take_upper_half(rng: range) -> range:
    items = list(last(divide(2, rng)))
    return range(first(items), last(items) + 1)


def narrow_ranges(
    sequence: str, row_range: range, col_range: range
) -> Tuple[str, range, range]:
    symbol, sequence = sequence[0], sequence[1:]
    if symbol == FRONT:
        row_range = take_lower_half(row_range)
    elif symbol == BACK:
        row_range = take_upper_half(row_range)
    elif symbol == LEFT:
        col_range = take_lower_half(col_range)
    elif symbol == RIGHT:
        col_range = take_upper_half(col_range)
    else:
        raise ValueError

    return sequence, row_range, col_range


@dataclass
class BoardingPass:
    row: int
    column: int
    seat: int

    @classmethod
    def decode(cls, sequence: str) -> BoardingPass:
        row_range = range(NUMBER_OF_ROWS)
        col_range = range(NUMBER_OF_COLUMNS)
        while sequence:
            sequence, row_range, col_range = narrow_ranges(
                sequence, row_range, col_range
            )
        row, column = one(row_range), one(col_range)
        seat = row * NUMBER_OF_COLUMNS + column
        return cls(row, column, seat)


def get_free_seats(occupied_seats: Iterable[int]) -> Set[int]:
    return {
        previous + 1
        for previous, next in windowed(sorted(occupied_seats), n=2)
        if (previous and next)
        and (previous + 1 not in occupied_seats)
        and (next - previous == 2)
    }


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        # part 1
        seats = [BoardingPass.decode(line).seat for line in lines]
        print(max(seats))

        # part 2
        my_seat = one(get_free_seats(seats))
        print(my_seat)


if __name__ == "__main__":
    run()
