from lib.utils import file_to_lines
from functools import reduce


def part_one(lines: list[str]) -> int:
    priorities = [
        to_priority(
            items_to_rearranged(rucksack)
        )
        for rucksack
        in lines
    ]
    return sum(priorities)


def items_to_rearranged(rucksack: str) -> set[str]:
    middle = int(len(rucksack) / 2)
    first_compartment = set(rucksack[:middle])
    second_compartment = set(rucksack[middle:])
    return first_compartment.intersection(second_compartment)


def to_priority(items: set[str]) -> int:
    return sum([to_prio(item) for item in items])


def to_prio(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38
    else:
        raise ValueError(f'Expected single digit item in lower or uppercase, but got: {item}')


def part_two(lines: list[str]) -> int:
    window_size = 3
    badges = [
        to_badge(lines[window:window + window_size])
        for window
        in range(0, len(lines), window_size)
    ]
    return sum([to_prio(badge) for badge in badges])


def to_badge(group: list[str]) -> str:
    badges = [*reduce(set.intersection, [set(rucksack) for rucksack in group])]
    if len(badges) != 1:
        raise ValueError(f'Expected one badge for group: {group} but found: {badges}')

    return badges.pop()


if __name__ == '__main__':
    assert part_one(file_to_lines('test_input.txt')) == 157
    print(part_one(file_to_lines('puzzle_input.txt')))

    assert part_two(file_to_lines('test_input.txt')) == 70
    print(part_two(file_to_lines('puzzle_input.txt')))
