from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import Final

from aoc.utils.io import open_input


class PasswordValidator(ABC):
    policy_password_regex: Final = re.compile(
        # first number
        "([0-9]+)"
        # separator
        "-"
        # second number
        "([0-9]+)"
        # separator
        " "
        # letter
        "([a-zA-Z])"
        # separator
        ": "
        # password
        "([a-zA-Z]+)"
    )

    def __init__(self, line: str) -> None:
        match = next(self.policy_password_regex.finditer(line))
        (
            first_number,
            second_number,
            self.letter,
            self.password,
        ) = match.groups()
        self.first_number = int(first_number)
        self.second_number = int(second_number)

    @abstractmethod
    def validate(self) -> bool:
        pass


class LetterRepeatsPasswordValidator(PasswordValidator):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.min_repeats = self.first_number
        self.max_repeats = self.second_number

    def validate(self) -> bool:
        letter_occurences = sum(letter == self.letter for letter in self.password)
        return self.min_repeats <= letter_occurences <= self.max_repeats


class LetterAtPositionsPasswordValidator(PasswordValidator):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.positions = (self.first_number - 1, self.second_number - 1)

    def validate(self) -> bool:
        return (
            sum(
                letter == self.letter
                for position in self.positions
                for letter in self.password[position]
            )
            == 1
        )


def run() -> None:
    with open_input(__file__) as file:
        lines = list(file.readlines())
        for validator in (
            LetterRepeatsPasswordValidator,
            LetterAtPositionsPasswordValidator,
        ):
            n_valid_passwords = sum(validator(line).validate() for line in lines)
            print(n_valid_passwords)


if __name__ == "__main__":
    run()
