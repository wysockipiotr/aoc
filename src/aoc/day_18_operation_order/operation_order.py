import re
from operator import add, mul
from typing import List, Optional, Tuple

from more_itertools import first, last

from aoc.utils.io import open_input

OPERATORS = {"+": add, "*": mul}


def find_outermost_right_operator(expression: str) -> Optional[Tuple[int, str]]:
    level = 0
    for index, token in enumerate(reversed(expression)):
        if token == ")":
            level += 1
        if token == "(":
            level -= 1
        if level == 0:
            if token in OPERATORS:
                return len(expression) - index - 1, token
    return None


def interpret_left_to_right(expression: str) -> int:
    expression = expression.replace(" ", "")
    outermost_right = find_outermost_right_operator(expression)
    if outermost_right is None:
        if first(expression) == "(" and last(expression) == ")":
            return interpret_left_to_right(expression[1:-1])
        return int(expression)
    index, operator = outermost_right
    return OPERATORS[operator](
        interpret_left_to_right(expression[:index]),
        interpret_left_to_right(expression[index + 1 :]),
    )


def interpret_swapped_add_and_mul(expression: str) -> int:
    class SwappedInt:
        def __init__(self, value: int, /) -> None:
            self._value = value

        def __int__(self) -> int:
            return self._value

        def __add__(self, other):
            return SwappedInt(self._value * other._value)

        def __mul__(self, other):
            return SwappedInt(self._value + other._value)

    expression = expression.translate(str.maketrans({"+": "*", "*": "+"}))  # type: ignore
    expression = re.sub("([0-9]+)", r"SwappedInt(\1)", expression)
    return int(eval(expression))


def run() -> None:
    with open_input(__file__) as file:
        lines: List[str] = file.read().splitlines()

        # part 1
        print(sum(interpret_left_to_right(line) for line in lines))

        # part 2
        print(sum(interpret_swapped_add_and_mul(line) for line in lines))


if __name__ == "__main__":
    run()
