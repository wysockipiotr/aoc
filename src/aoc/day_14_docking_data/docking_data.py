import re
from collections import defaultdict
from itertools import product
from typing import Callable, DefaultDict, List, Optional

from more_itertools import first

from aoc.utils.io import open_input

Memory = DefaultDict[int, int]

# part 1
def value_masking(memory: Memory, mask: str, address: int, value: int) -> Memory:
    for mask_bit_index, mask_bit in enumerate(reversed(mask)):
        if mask_bit in {"0", "1"}:
            value ^= (-int(mask_bit) ^ value) & (1 << mask_bit_index)
    memory[address] = value
    return memory


# part 2
def address_masking(memory: Memory, mask: str, address: int, value: int) -> Memory:
    address_bits = "".join(
        "X" if mask_bit == "X" else ("1" if mask_bit == "1" else address_bit)
        for mask_bit, address_bit in zip(mask, bin(address)[2:].zfill(36))
    )
    n_floating = sum(bit == "X" for bit in address_bits)
    for bits in product({"0", "1"}, repeat=n_floating):
        effective_address = address_bits
        floating_indices = [
            index for index, bit in enumerate(address_bits) if bit == "X"
        ]
        for floating_index, bit in zip(floating_indices, bits):
            effective_address = (
                effective_address[:floating_index]
                + bit
                + effective_address[floating_index + 1 :]
            )
        memory[int(effective_address)] = int(value)
    return memory


def mutate_memory(lines: List[str], method: Callable) -> Memory:
    mask: Optional[str] = None
    memory: Memory = defaultdict(lambda: 0)

    for line in lines:
        mask_definition_match = re.match("mask = ([01X]{36})", line)
        assignment_match = re.match("mem\[([0-9]+)\] = ([0-9]+)", line)
        if mask_definition_match:
            mask = first(mask_definition_match.groups())
        if assignment_match:
            if not mask:
                raise RuntimeError
            address, value = map(int, assignment_match.groups())

            memory = method(memory, mask, address, value)

    return memory


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        for method in (value_masking, address_masking):
            memory = mutate_memory(lines, method)
            print(sum(memory.values()))


if __name__ == "__main__":
    run()
