import pytest

from aoc.day_5_binary_boarding.binary_boarding import (
    BoardingPass,
    get_free_seats,
    take_lower_half,
    take_upper_half,
)


@pytest.mark.parametrize(
    "rng,expected_lower_half",
    [
        (range(0, 128), range(0, 64)),
        (range(0, 1), range(0, 1)),
        (range(0, 2), range(0, 1)),
        (range(0, 3), range(0, 2)),
    ],
)
def test_take_lower_half(rng: range, expected_lower_half: range) -> None:
    assert take_lower_half(rng) == expected_lower_half


@pytest.mark.parametrize(
    "rng,expected_upper_half",
    [
        (range(0, 128), range(64, 128)),
        pytest.param(
            range(0, 1), range(0, 1), marks=pytest.mark.xfail(raises=ValueError)
        ),
        (range(0, 2), range(1, 2)),
        (range(0, 3), range(2, 3)),
    ],
)
def test_take_upper_half(rng: range, expected_upper_half: range) -> None:
    assert take_upper_half(rng) == expected_upper_half


@pytest.mark.parametrize(
    "sequence,expected_boarding_pass",
    [
        ("BFFFBBFRRR", BoardingPass(70, 7, 567)),
        ("FFFBBBFRRR", BoardingPass(14, 7, 119)),
        ("BBFFBBFRLL", BoardingPass(102, 4, 820)),
    ],
)
def test_boarding_pass_can_be_decoded_from_binary_search_sequence(
    sequence: str, expected_boarding_pass: BoardingPass
) -> None:
    assert BoardingPass.decode(sequence) == expected_boarding_pass


def test_get_free_seats() -> None:
    seats = [1, 2, 3, 4, 5]
    free_seat = seats.pop(2)
    assert get_free_seats(seats) == {free_seat}
