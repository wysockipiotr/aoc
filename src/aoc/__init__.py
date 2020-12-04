from itertools import count

import typer

cli = typer.Typer()


@cli.command()
def run(day: int = typer.Option(..., min=1)):
    from aoc.day_1_report_repair import day_1_report_repair
    from aoc.day_2_password_philosophy import day_2_password_philosophy
    from aoc.day_3_toboggan_trajectory import day_3_toboggan_trajectory
    from aoc.day_4_passport_processing import passport_processing

    puzzle_per_day = {
        day: puzzle
        for day, puzzle in zip(
            count(1),
            [
                day_1_report_repair,
                day_2_password_philosophy,
                day_3_toboggan_trajectory,
                passport_processing,
            ],
        )
    }

    puzzle_per_day[day].run()  # type: ignore


if __name__ == "__main__":
    cli()