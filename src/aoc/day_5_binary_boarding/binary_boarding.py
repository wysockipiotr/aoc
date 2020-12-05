from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Iterable, Set

from more_itertools import one, windowed

from aoc.utils.io import open_input

FRONT: Final = "F"
BACK: Final = "B"
LEFT: Final = "L"
RIGHT: Final = "R"


@dataclass
class BoardingPass:
    row: int
    column: int
    seat: int

    @classmethod
    def decode_from(cls, sequence: str) -> BoardingPass:
        symbols_to_bits = {
            FRONT: "0",
            BACK: "1",
            LEFT: "0",
            RIGHT: "1",
        }
        seat_number_bits = "".join(symbols_to_bits[symbol] for symbol in sequence)
        seat = int(seat_number_bits, base=2)
        row = seat >> 3
        column = seat & 7
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
        seats = [BoardingPass.decode_from(line).seat for line in lines]
        print(max(seats))

        # part 2
        my_seat = one(get_free_seats(seats))
        print(my_seat)


if __name__ == "__main__":
    run()
