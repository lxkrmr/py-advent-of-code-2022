from lib.utils import file_to_str


def part_one(raw: str) -> int:
    return max(total_calories_per_elf(raw))


def part_two(raw: str) -> int:
    calories = total_calories_per_elf(raw)
    top_3_highest_calories = sorted(calories, reverse=True)[:3]
    return sum(top_3_highest_calories)


def total_calories_per_elf(raw):
    return [
        sum(
            [
                int(calories)
                for calories
                in calories_per_elf.split('\n')
                if calories.isdigit()
            ]
        )
        for calories_per_elf
        in (raw.split('\n\n'))
    ]


if __name__ == '__main__':
    # part 01
    assert part_one(file_to_str('test_input.txt')) == 24_000
    print(part_one(file_to_str('puzzle_input.txt')))

    # part 02
    assert part_two(file_to_str('test_input.txt')) == 45_000
    print(part_two(file_to_str('puzzle_input.txt')))

