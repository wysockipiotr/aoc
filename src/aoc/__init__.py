from typing import Final

import typer

import aoc.day_01_report_repair.report_repair
import aoc.day_02_password_philosophy.password_philosophy
import aoc.day_03_toboggan_trajectory.toboggan_trajectory
import aoc.day_04_passport_processing.passport_processing
import aoc.day_05_binary_boarding.binary_boarding
import aoc.day_06_custom_customs.custom_customs
import aoc.day_07_handy_haversacks.handy_haversacks
import aoc.day_08_handheld_halting.handheld_halting
import aoc.day_09_encoding_error.encoding_error
import aoc.day_10_adapter_array.adapter_array
import aoc.day_11_seating_system.seating_system
import aoc.day_12_rain_risk.rain_risk

cli = typer.Typer()

TASKS: Final = [
    aoc.day_01_report_repair.report_repair,
    aoc.day_02_password_philosophy.password_philosophy,
    aoc.day_03_toboggan_trajectory.toboggan_trajectory,
    aoc.day_04_passport_processing.passport_processing,
    aoc.day_05_binary_boarding.binary_boarding,
    aoc.day_06_custom_customs.custom_customs,
    aoc.day_07_handy_haversacks.handy_haversacks,
    aoc.day_08_handheld_halting.handheld_halting,
    aoc.day_09_encoding_error.encoding_error,
    aoc.day_10_adapter_array.adapter_array,
    aoc.day_11_seating_system.seating_system,
    aoc.day_12_rain_risk.rain_risk,
]


@cli.command()
def run(day: int = typer.Option(..., min=1, max=len(TASKS))):
    TASKS[day - 1].run()  # type: ignore


if __name__ == "__main__":
    cli()
