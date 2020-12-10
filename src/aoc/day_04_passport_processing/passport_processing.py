import re
from typing import Dict, Final, Literal

from more_itertools import split_at
from pydantic import BaseModel, Field, validator
from pydantic.error_wrappers import ValidationError

from aoc.utils.io import open_input

FIELD_REGEX: Final = re.compile(
    # field name
    "([a-z]{3})"
    # separator
    ":"
    # field value
    "([a-zA-Z0-9#]+)"
)
REQUIRED_FIELDS: Final = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


class Passport(BaseModel):
    byr: int = Field(..., ge=1920, le=2002)
    iyr: int = Field(..., ge=2010, le=2020)
    eyr: int = Field(..., ge=2020, le=2030)
    hgt: str = Field(..., min_length=3)
    ecl: Literal["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    hcl: str = Field(..., max_length=7, regex="#[0-9a-f]{6}")
    pid: str = Field(..., max_length=9, regex="[0-9]{9}")

    @validator("hgt")
    def validate_height(cls, hgt: str) -> str:
        value, unit = int(hgt[:-2]), hgt[-2:]
        if any(
            (
                (unit == "cm" and 150 <= value <= 193),
                (unit == "in" and 59 <= value <= 76),
            )
        ):
            return hgt
        raise ValueError

    @classmethod
    def is_valid(cls, fields: Dict) -> bool:
        try:
            cls(**fields)
        except ValidationError:
            return False
        else:
            return True


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()
        raw_passports_data = [
            " ".join(fields) for fields in split_at(lines, lambda line: len(line) == 0)
        ]
        passports = [
            {name: value for name, value in FIELD_REGEX.findall(passport_data)}
            for passport_data in raw_passports_data
        ]

        # part 1
        valid_passports = [
            passport for passport in passports if REQUIRED_FIELDS <= passport.keys()
        ]
        print(len(valid_passports))

        # part 2
        valid_passports = [
            passport for passport in valid_passports if Passport.is_valid(passport)
        ]
        print(len(valid_passports))


if __name__ == "__main__":
    run()
