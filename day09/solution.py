from day09.models import motions_from_file, Motion, Rope


def main():
    test_input_part_one = motions_from_file('test_input_part_one.txt')
    test_input_part_two = motions_from_file('test_input_part_two.txt')
    puzzle_input = motions_from_file('puzzle_input.txt')

    assert part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(test_input_part_one) == 13
    print(part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(puzzle_input))

    assert part_two_rope_with_ten_knots(test_input_part_two) == 36
    print(part_two_rope_with_ten_knots(puzzle_input))


def part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(motions: list[Motion]):
    rope = Rope()
    for motion in motions:
        rope.move(motion)
    return rope.tip_of_the_tail().num_positions_visited()


def part_two_rope_with_ten_knots(motions: list[Motion]) -> int:
    rope = Rope(numer_of_knots=10)
    for motion in motions:
        rope.move(motion)
    return rope.tip_of_the_tail().num_positions_visited()


if __name__ == '__main__':
    main()
