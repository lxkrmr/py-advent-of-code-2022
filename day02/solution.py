from lib.utils import file_to_lines


def part_one(lines: list[str]) -> int:
    return sum([scores_part_one[match] for match in lines])


scores_part_one = {
    'A X': 4,  # opponent: Rock        vs    you: Rock     -> draw -> 3 + 1
    'B X': 1,  # opponent: Paper       vs    you: Rock     -> lost -> 0 + 1
    'C X': 7,  # opponent: Scissors    vs    you: Rock     -> won  -> 6 + 1
    'A Y': 8,  # opponent: Rock        vs    you: Paper    -> won  -> 6 + 2
    'B Y': 5,  # opponent: Paper       vs    you: Paper    -> draw -> 3 + 2
    'C Y': 2,  # opponent: Scissors    vs    you: Paper    -> lost -> 0 + 2
    'A Z': 3,  # opponent: Rock        vs    you: Scissors -> lost -> 0 + 3
    'B Z': 9,  # opponent: Paper       vs    you: Scissors ->  won -> 6 + 3
    'C Z': 6,  # opponent: Scissors    vs    you: Scissors -> draw -> 3 + 3
}


def part_two(lines: list[str]) -> int:
    return sum([scores_part_two[match] for match in lines])


scores_part_two = {
    'A X': 3,  # opponent: Rock     -> you: lose -> Scissors -> 0 + 3
    'B X': 1,  # opponent: Paper    -> you: lose -> Rock     -> 0 + 1
    'C X': 2,  # opponent: Scissors -> you: lose -> Paper    -> 0 + 2
    'A Y': 4,  # opponent: Rock     -> you: draw -> Rock     -> 3 + 1
    'B Y': 5,  # opponent: Paper    -> you: draw -> Paper    -> 3 + 2
    'C Y': 6,  # opponent: Scissors -> you: draw -> Scissors -> 3 + 3
    'A Z': 8,  # opponent: Rock     -> you: win  -> Paper    -> 6 + 2
    'B Z': 9,  # opponent: Paper    -> you: win  -> Scissors -> 6 + 3
    'C Z': 7,  # op
    # ponent: Scissors -> you: win  -> Rock     -> 6 + 1
}

if __name__ == '__main__':
    assert part_one(file_to_lines('test_input.txt')) == 15
    print(part_one(file_to_lines('puzzle_input.txt')))

    assert part_two(file_to_lines('test_input.txt')) == 12
    print(part_two(file_to_lines('puzzle_input.txt')))
