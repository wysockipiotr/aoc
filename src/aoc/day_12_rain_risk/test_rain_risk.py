from typing import List

from pytest import fixture

from aoc.day_12_rain_risk.rain_risk import (
    DIRECTIONS,
    ShipState,
    advance,
    manhattan_distance,
)


@fixture
def instructions() -> List[str]:
    return ["F10", "N3", "F7", "R90", "F11"]


def test_advance_ship_without_waypoints(instructions: List[str]) -> None:
    state = ShipState(orientation=DIRECTIONS["E"])
    for instruction in instructions:
        state = advance(state, instruction, use_waypoints=False)
    assert manhattan_distance(state.position) == 25


def test_advance_ship_using_waypoints(instructions: List[str]) -> None:
    state = ShipState(orientation=10 * DIRECTIONS["E"] + 1 * DIRECTIONS["N"])
    for instruction in instructions:
        state = advance(state, instruction, use_waypoints=True)
    assert manhattan_distance(state.position) == 286
