import pytest

from aoc.day_18_operation_order.operation_order import (
    interpret_left_to_right,
    interpret_swapped_add_and_mul,
)


@pytest.mark.parametrize(
    "expression,expected_result",
    (
        ("2 * 3 + (4 * 5)", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
    ),
)
def test_interpret_left_to_right(expression: str, expected_result: int) -> None:
    assert interpret_left_to_right(expression) == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    (
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    ),
)
def test_interpret_swapped_add_and_mul(expression: str, expected_result: int) -> None:
    assert interpret_swapped_add_and_mul(expression) == expected_result
