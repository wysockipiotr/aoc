from pathlib import Path
import clipboard

template = """from aoc.utils.io import open_input


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()


if __name__ == "__main__":
    run()

"""


def create_day(task_name: str, day_number: int) -> None:
    days_path = Path(__file__).parents[1]
    if any(f"{day_number:02}" in path.name for path in days_path.iterdir()):
        raise ValueError

    created_day_dir = days_path / f"day_{day_number:02}_{task_name}"
    created_day_dir.mkdir()

    with (created_day_dir / "input").open("w") as file:
        file.write(clipboard.paste())
    (created_day_dir / f"test_{task_name}.py").touch()
    with (created_day_dir / f"{task_name}.py").open("w") as file:
        file.write(template)
