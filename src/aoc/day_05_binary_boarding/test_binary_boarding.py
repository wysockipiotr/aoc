import pytest

from aoc.day_05_binary_boarding.binary_boarding import BoardingPass, get_free_seats


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
    assert BoardingPass.decode_from(sequence) == expected_boarding_pass


def test_get_free_seats() -> None:
    seats = [1, 2, 3, 4, 5]
    free_seat = seats.pop(2)
    assert get_free_seats(seats) == {free_seat}
