from itertools import count

import typer

cli = typer.Typer()


@cli.command()
def run(day: int = typer.Option(..., min=1)):
    from aoc.day_1_report_repair import report_repair
    from aoc.day_2_password_philosophy import password_philosophy
    from aoc.day_3_toboggan_trajectory import toboggan_trajectory
    from aoc.day_4_passport_processing import passport_processing
    from aoc.day_5_binary_boarding import binary_boarding

    puzzle_per_day = {
        day: puzzle
        for day, puzzle in zip(
            count(1),
            [
                report_repair,
                password_philosophy,
                toboggan_trajectory,
                passport_processing,
                binary_boarding,
            ],
        )
    }

    puzzle_per_day[day].run()  # type: ignore


if __name__ == "__main__":
    cli()
