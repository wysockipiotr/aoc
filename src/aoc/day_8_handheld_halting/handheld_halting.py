from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Set

from aoc.utils.io import open_input


@dataclass
class Instruction:
    opcode: str
    argument: int


@dataclass
class ProcessorState:
    accumulator: int = field(default=0)
    instruction_pointer: int = field(default=0)
    total_executions: int = field(default=0)
    executed_lines: Set[int] = field(default_factory=set)

    def execute(self, instruction: Instruction) -> ProcessorState:
        next_state = ProcessorState(
            self.accumulator,
            self.instruction_pointer,
            self.total_executions + 1,
            {*self.executed_lines, self.instruction_pointer},
        )
        if instruction.opcode == "jmp":
            next_state.instruction_pointer += instruction.argument
        elif instruction.opcode == "acc":
            next_state.accumulator += instruction.argument
            next_state.instruction_pointer += 1
        else:
            next_state.instruction_pointer += 1
        return next_state


def get_state_after_first_repeated_execution(
    instructions: List[Instruction],
) -> ProcessorState:
    state = ProcessorState()
    while state.instruction_pointer not in state.executed_lines:
        instruction = instructions[state.instruction_pointer]
        state = state.execute(instruction)
    return state


def get_state_after_termination(
    instructions: List[Instruction],
) -> Optional[ProcessorState]:
    state = ProcessorState()
    while state.instruction_pointer < len(instructions):
        instruction = instructions[state.instruction_pointer]
        state = state.execute(instruction)
        if state.total_executions > len(instructions):
            return None
    return state


def run() -> None:
    with open_input(__file__) as file:
        lines = file.read().splitlines()

        instructions = [
            Instruction(opcode, int(argument))
            for opcode, argument in map(str.split, lines)
        ]

        # part 1
        print(get_state_after_first_repeated_execution(instructions).accumulator)

        # part 2
        for opcode in {"nop", "jmp"}:
            for instruction_index, instruction in enumerate(instructions):
                if instruction.opcode == opcode:
                    modified_instructions = [*instructions]
                    modified_instructions[instruction_index] = Instruction(
                        "nop" if instruction.opcode == "jmp" else "jmp",
                        instruction.argument,
                    )
                    state = get_state_after_termination(modified_instructions)
                    if state:
                        print(state.accumulator)


if __name__ == "__main__":
    run()
