from __future__ import annotations

from dataclasses import astuple, dataclass
from functools import reduce
from itertools import count, takewhile
from operator import mul
from pathlib import Path
from typing import Final

import numpy as np

TREE_SYMBOL: Final = "#"


@dataclass
class Vec2i:
    x: int
    y: int


Slope = Vec2i
Position = Vec2i
Size = Vec2i


class Geology:
    def __init__(self, tree_mask: np.ndarray) -> None:
        self._tree_mask = tree_mask

    @classmethod
    def from_file(cls, path: Path) -> Geology:
        with path.open("r") as file:
            tree_mask = [
                [character == TREE_SYMBOL for character in line]
                for line in file.read().splitlines()
            ]
            tree_mask = np.array(tree_mask)
            return cls(tree_mask)

    @property
    def tile_size(self) -> Size:
        y, x = self._tree_mask.shape
        return Size(x, y)

    def tree_at(self, x: int, y: int) -> bool:
        return self._tree_mask[y, x % self.tile_size.x]


def count_tree_encounters(
    geology: Geology, slope: Slope, start: Position = Position(0, 0)
) -> int:
    start_x, start_y = astuple(start)
    return sum(
        geology.tree_at(x, y)
        for x, y in zip(
            count(start=start_x, step=slope.x),
            takewhile(
                lambda y: y < geology.tile_size.y, count(start=start_y, step=slope.y)
            ),
        )
    )


def run() -> None:
    geology = Geology.from_file(Path(__file__).parent / "input")

    # part 1
    slope = Slope(3, 1)
    encountered_trees = count_tree_encounters(geology, slope)
    print(encountered_trees)

    # part 2
    slopes = (
        Slope(1, 1),
        Slope(3, 1),
        Slope(5, 1),
        Slope(7, 1),
        Slope(1, 2),
    )
    encountered_trees_per_slope = (
        count_tree_encounters(geology, slope) for slope in slopes
    )
    result = reduce(mul, encountered_trees_per_slope, 1)
    print(result)


if __name__ == "__main__":
    run()
