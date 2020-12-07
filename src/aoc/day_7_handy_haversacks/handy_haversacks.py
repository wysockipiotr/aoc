from collections import defaultdict
from typing import DefaultDict, Dict

from aoc.utils.io import open_input


def can_contain_bag_of_color(
    container_color: str,
    bag_color: str,
    allowed_colors: DefaultDict[str, Dict[str, int]],
) -> bool:
    if container_color not in allowed_colors:
        return False

    inner_bags_colors = allowed_colors[container_color]

    if bag_color in inner_bags_colors:
        return True

    return any(
        can_contain_bag_of_color(inner_bag_color, bag_color, allowed_colors)
        for inner_bag_color in inner_bags_colors
    )


def count_bags(color: str, allowed_colors: DefaultDict[str, Dict[str, int]]) -> int:
    if color not in allowed_colors:
        return 0

    inner_bags_colors_counts = allowed_colors[color]

    return sum(inner_bags_colors_counts.values()) + sum(
        qty * count_bags(inner_bag_color, allowed_colors)
        for inner_bag_color, qty in inner_bags_colors_counts.items()
    )



def run():
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        lookup = defaultdict(dict)

        for line in lines:
            container, contents = map(str.strip, line.split("bags contain"))

            for content in map(str.strip, contents[:-1].split(",")):
                qty, *name, _ = content.split()
                name = " ".join(name).strip()
                if qty != "no":
                    lookup[container][name] = int(qty)

        # part 1
        print(
            sum(
                can_contain_bag_of_color(bag, "shiny gold", lookup)
                for bag in lookup
            )
        )
        
        # part 2
        print(count_bags("shiny gold", lookup))


if __name__ == "__main__":
    run()
