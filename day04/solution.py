from lib.utils import file_to_lines
from dataclasses import dataclass


@dataclass(frozen=True)
class SectionAssignment:
    start: int
    end: int

    @classmethod
    def from_string(cls, string: str) -> 'SectionAssignment':
        start, end = [int(entry) for entry in string.split('-')]
        return cls(start, end)

    def __contains__(self, other) -> bool:
        return (other.start >= self.start) and (other.end <= self.end)

    def is_overlapping(self, other) -> bool:
        return self.start <= other.end and self.end >= other.start


@dataclass(frozen=True)
class AssignmentPair:
    first: SectionAssignment
    second: SectionAssignment

    @classmethod
    def from_string(cls, string: str) -> 'AssignmentPair':
        first_raw, second_raw = string.split(',')
        return cls(
            SectionAssignment.from_string(first_raw),
            SectionAssignment.from_string(second_raw)
        )

    def is_one_containing_the_other(self) -> bool:
        return (self.first in self.second) or (self.second in self.first)

    def do_both_overlap(self) -> bool:
        return self.first.is_overlapping(self.second)


def part_one(lines: list[str]) -> int:
    return sum(
        [
            1
            for line
            in lines
            if AssignmentPair.from_string(line).is_one_containing_the_other()
        ]
    )


def part_two(lines: list[str]) -> int:
    return sum(
        [
            1
            for line
            in lines
            if AssignmentPair.from_string(line).do_both_overlap()
        ]
    )


def main():
    assert part_one(file_to_lines('test_input.txt')) == 2
    print(part_one(file_to_lines('puzzle_input.txt')))

    assert part_two(file_to_lines('test_input.txt')) == 4
    print(part_two(file_to_lines('puzzle_input.txt')))


if __name__ == '__main__':
    main()
