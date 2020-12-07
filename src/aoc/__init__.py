import typer

import aoc.day_1_report_repair.report_repair
import aoc.day_2_password_philosophy.password_philosophy
import aoc.day_3_toboggan_trajectory.toboggan_trajectory
import aoc.day_4_passport_processing.passport_processing
import aoc.day_5_binary_boarding.binary_boarding
import aoc.day_6_custom_customs.custom_customs
import aoc.day_7_handy_haversacks.handy_haversacks

cli = typer.Typer()


@cli.command()
def run(day: int = typer.Option(..., min=1)):
    [
        aoc.day_1_report_repair.report_repair,
        aoc.day_2_password_philosophy.password_philosophy,
        aoc.day_3_toboggan_trajectory.toboggan_trajectory,
        aoc.day_4_passport_processing.passport_processing,
        aoc.day_5_binary_boarding.binary_boarding,
        aoc.day_6_custom_customs.custom_customs,
        aoc.day_7_handy_haversacks.handy_haversacks,
    ][
        day - 1
    ].run()  # type: ignore


if __name__ == "__main__":
    cli()
