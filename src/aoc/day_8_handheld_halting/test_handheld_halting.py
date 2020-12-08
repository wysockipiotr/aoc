from typing import List
from pytest import fixture

from aoc.day_8_handheld_halting.handheld_halting import (
    Instruction,
    get_state_after_first_repeated_execution,
    get_state_after_termination,
)


@fixture
def instructions() -> List[Instruction]:
    return [
        Instruction("nop", 0),
        Instruction("acc", 1),
        Instruction("jmp", 4),
        Instruction("acc", 3),
        Instruction("jmp", -3),
        Instruction("acc", -99),
        Instruction("acc", 1),
        Instruction("jmp", -4),
        Instruction("acc", 6),
    ]


def test_get_state_after_first_repeated_execution(
    instructions: List[Instruction],
) -> None:
    state = get_state_after_first_repeated_execution(instructions)
    assert state.accumulator == 5


def test_get_state_after_termination_returns_none_if_program_has_infinite_loop() -> None:
    infinite_program = [Instruction("nop"), Instruction("jmp", -1)]
    assert get_state_after_termination(infinite_program) is None


def test_get_state_after_termination() -> None:
    terminating_program = [
        Instruction("acc", 1),
        Instruction("jmp", 2),
        Instruction("nop"),
        Instruction("nop"),
    ]
    state = get_state_after_termination(terminating_program)
    assert state
    assert state.accumulator == 1
