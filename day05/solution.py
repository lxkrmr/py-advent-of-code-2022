from utils.utils import file_to_str
from dataclasses import dataclass


def part_one(file: str) -> str:
    raw_supply_stacks, raw_instructions = file.split('\n\n')

    supply_stacks = to_supply_stacks(raw_supply_stacks)
    instructions = to_instructions(raw_instructions)

    crate_mover_9000(instructions, supply_stacks)

    return top_crates(supply_stacks)


def part_two(file: str) -> str:
    raw_supply_stacks, raw_instructions = file.split('\n\n')

    supply_stacks = to_supply_stacks(raw_supply_stacks)
    instructions = to_instructions(raw_instructions)

    crate_mover_9001(instructions, supply_stacks)

    return top_crates(supply_stacks)


def to_supply_stacks(string: str) -> list[list[str]]:
    raw_without_labels = string.split('\n')[:-1]
    rows = [[*to_row_generator(row)] for row in reversed(raw_without_labels)]
    return rows_to_columns(rows)


def to_row_generator(raw_row: str):
    stack_size = 3
    space_between = 1
    for index in range(0, len(raw_row), stack_size + space_between):
        crate = raw_row[index:(index + stack_size)]
        yield index, crate


def rows_to_columns(rows):
    helper_dict = {}
    for row in rows:
        for index, crate in row:
            if crate.strip():
                helper_dict.setdefault(index, []).append(crate)

    return [helper_dict[key] for key in helper_dict.keys()]


@dataclass(frozen=True)
class Instruction:
    move: int
    from_position: int
    to_position: int

    def from_as_index(self):
        return self.from_position - 1

    def to_as_index(self):
        return self.to_position - 1


def to_instructions(string: str) -> list[Instruction]:
    only_numbers = [[int(entry) for entry in row.split(' ') if entry.isdigit()] for row in (string.split('\n'))]
    return [Instruction(m, f, t) for m, f, t in only_numbers]


def crate_mover_9000(instructions: list[Instruction], supply_stacks: list[list[str]]) -> None:
    for instruction in instructions:
        for times in range(0, instruction.move):
            crate = supply_stacks[instruction.from_as_index()].pop()
            supply_stacks[instruction.to_as_index()].append(crate)


def crate_mover_9001(instructions: list[Instruction], supply_stacks: list[list[str]]) -> None:
    for instruction in instructions:
        last_x_crates = -1 * instruction.move
        crates = supply_stacks[instruction.from_as_index()][last_x_crates:]
        supply_stacks[instruction.from_as_index()] = supply_stacks[instruction.from_as_index()][:last_x_crates]
        supply_stacks[instruction.to_as_index()].extend(crates)


def top_crates(supply_stacks: list[list[str]]) -> str:
    top = [to_pretty_crate(stack[-1]) for stack in supply_stacks]
    return "".join(top)


def to_pretty_crate(crate: str) -> str:
    return crate.replace('[', '').replace(']', '').strip()


def main():
    assert part_one(file_to_str('test_input.txt')) == 'CMZ'
    print(part_one(file_to_str('puzzle_input.txt')))

    assert part_two(file_to_str('test_input.txt')) == 'MCD'
    print(part_two(file_to_str('puzzle_input.txt')))


if __name__ == '__main__':
    main()
