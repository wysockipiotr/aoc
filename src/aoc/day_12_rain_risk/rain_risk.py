from dataclasses import dataclass

import numpy as np

from aoc.utils.io import open_input

DIRECTIONS = {
    "N": np.array([0, 1]),
    "E": np.array([1, 0]),
    "S": np.array([0, -1]),
    "W": np.array([-1, 0]),
}


@dataclass(frozen=True)
class ShipState:
    position: np.ndarray = np.array([0, 0])
    orientation: np.ndarray = np.array(DIRECTIONS["E"])


def manhattan_distance(position: np.ndarray) -> float:
    return sum(map(abs, position))


def rotation_2d(degrees: int) -> np.ndarray:
    angle = np.deg2rad(degrees)
    return np.array(
        [
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)],
        ]
    )


def advance(state: ShipState, instruction: str, use_waypoints: bool) -> ShipState:
    instruction, argument = instruction[0], int(instruction[1:])

    if instruction in {"L", "R"}:
        angle = argument * (1 if instruction == "L" else -1)
        state = ShipState(
            state.position, np.round(rotation_2d(angle) @ state.orientation)
        )
    elif instruction in DIRECTIONS:
        if use_waypoints:
            state = ShipState(
                state.position, state.orientation + argument * DIRECTIONS[instruction]
            )
        else:
            state = ShipState(
                state.position + argument * DIRECTIONS[instruction], state.orientation
            )
    else:
        state = ShipState(
            state.position + argument * state.orientation, state.orientation
        )
    return state


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

    # part 1
    state = ShipState()
    for line in lines:
        state = advance(state, line, use_waypoints=False)
    print(manhattan_distance(state.position))

    # part 2
    state = ShipState(orientation=10 * DIRECTIONS["E"] + 1 * DIRECTIONS["N"])
    for line in lines:
        state = advance(state, line, use_waypoints=True)
    print(manhattan_distance(state.position))


if __name__ == "__main__":
    run()
