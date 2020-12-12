import re
from pathlib import Path

import typer

from aoc.scripts.create_day import create_day

cli = typer.Typer()


@cli.command()
def solve(day: int = typer.Option(...)):
    for path in Path(__file__).parent.iterdir():
        match = re.match("day_([0-9]{2})_([a-z_]+)", path.name)
        if match:
            matched_day, task_name = match.groups()
            if str(day).zfill(2) == matched_day:
                try:
                    exec(f"from aoc.day_{day:02}_{task_name}.{task_name} import run")
                except ImportError:
                    typer.echo(f"Could not import solution to day {day} task")
                else:
                    exec("run()")


@cli.command()
def create(day: int = typer.Option(...), name: str = typer.Option(...)):
    create_day(name, day)


if __name__ == "__main__":
    cli()
