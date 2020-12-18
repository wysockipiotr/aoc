from __future__ import annotations

from itertools import product, repeat
from operator import add
from typing import AbstractSet, Iterator, List, Literal, Set, Tuple

from aoc.utils.io import open_input


def iter_neighbours(cube: Tuple[int, ...]) -> Iterator[Tuple[int, ...]]:
    n_dims = len(cube)
    for offset in product((-1, 0, 1), repeat=n_dims):
        if offset != tuple(repeat(0, times=n_dims)):
            yield tuple(map(add, cube, offset))


class CubicGrid:
    def __init__(self, active: AbstractSet[Tuple[int, ...]]) -> None:
        self._active: Set[Tuple[int, ...]] = set(active)

    def is_active(self, cube: Tuple[int, ...]) -> bool:
        return cube in self._active

    def count_active(self) -> int:
        return len(self._active)

    def count_active_neighbours(self, cube: Tuple[int, ...]) -> int:
        return sum(self.is_active(neighbour) for neighbour in iter_neighbours(cube))

    def __next__(self) -> CubicGrid:
        to_be_active = set()

        for active_cube in self._active:
            if self.count_active_neighbours(active_cube) in {2, 3}:
                to_be_active.add(active_cube)

            for neighbour_cube in iter_neighbours(active_cube):
                if self.is_active(neighbour_cube):
                    if self.count_active_neighbours(neighbour_cube) in {2, 3}:
                        to_be_active.add(neighbour_cube)
                else:
                    if self.count_active_neighbours(neighbour_cube) == 3:
                        to_be_active.add(neighbour_cube)

        return CubicGrid(to_be_active)

    @classmethod
    def from_lines(cls, lines: List[str], n_dims: Literal[3, 4]):
        active: Set[Tuple[int, ...]] = set()
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if symbol == "#":
                    if n_dims == 3:
                        active.add((x, y, 0))
                    else:
                        active.add((x, y, 0, 0))
        return cls(active)


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        # part 1
        grid = CubicGrid.from_lines(lines, n_dims=3)
        for _ in range(6):
            grid = next(grid)
        print(grid.count_active())

        # part 2
        grid = CubicGrid.from_lines(lines, n_dims=4)
        for _ in range(6):
            grid = next(grid)
        print(grid.count_active())


if __name__ == "__main__":
    run()
