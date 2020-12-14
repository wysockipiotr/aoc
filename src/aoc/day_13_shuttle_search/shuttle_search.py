from operator import itemgetter

from sympy.ntheory.modular import crt

from aoc.utils.io import open_input


def round_up(num, divisor):
    return num - (num % divisor) + divisor


def run() -> None:
    with open_input(__file__) as file:
        lines = list(file.read().splitlines())
        earliest_depart_t, buses = int(lines[0]), lines[1]

        # part 1
        active_buses = [int(bus_id) for bus_id in buses.split(",") if bus_id != "x"]
        earliest_bus_id, earliest_bus_departure_t = min(
            ((bus_id, round_up(earliest_depart_t, bus_id)) for bus_id in active_buses),
            key=itemgetter(1),
        )
        print(earliest_bus_id * (earliest_bus_departure_t - earliest_depart_t))

        # part 2
        buses = [
            (offset, int(bus_id))
            for offset, bus_id in enumerate(bus for bus in buses.split(","))
            if bus_id != "x"
        ]
        print(
            crt(
                [bus_id for _, bus_id in buses],
                [bus_id - offset for offset, bus_id in buses],
            )[0]
        )


if __name__ == "__main__":
    run()
