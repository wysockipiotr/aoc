from pathlib import Path
from typing import IO


def open_input(file: str) -> IO:
    return (Path(file).parent / "input").open("r")
