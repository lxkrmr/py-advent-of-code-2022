from dataclasses import dataclass
from typing import Generator

from utils.utils import file_to_lines


@dataclass(frozen=True)
class SignalSequence:
    start: int
    end: int
    sequence: str

    def is_start_sequence(self) -> bool:
        """ True if all chars in sequence are different """
        unique_chars_in_sequence = set(self.sequence)
        expected_length_for_marker = self.end - self.start
        return len(unique_chars_in_sequence) == expected_length_for_marker


def solve(lines: list[str], window_size: int) -> list[int]:
    result = [seq.end for seq in [find_first_start_sequence(line, window_size) for line in lines] if seq]
    return result


def find_first_start_sequence(line: str, window_size: int) -> SignalSequence | None:
    for sequence in signal_sequence_generator(line, window_size):
        if sequence.is_start_sequence():
            return sequence

    return None


def signal_sequence_generator(line: str, window_size: int) -> Generator[SignalSequence, None, None]:
    for start in range(0, len(line)):
        stop = start + window_size
        sequence = line[start:stop]
        yield SignalSequence(start, stop, sequence)


def main():
    assert solve(file_to_lines('test_input.txt'), 4) == [7, 5, 6, 10, 11]
    print(solve(file_to_lines('puzzle_input.txt'), 4))

    assert solve(file_to_lines('test_input.txt'), 14) == [19, 23, 23, 29, 26]
    print(solve(file_to_lines('puzzle_input.txt'), 14))


if __name__ == '__main__':
    main()
