from day09.models import motions_from_file, Motion, Rope, Direction


def main():
    test_input = motions_from_file('test_input.txt')
    puzzle_input = motions_from_file('puzzle_input.txt')

    assert part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(test_input) == 13
    print(part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(puzzle_input))


def part_one_how_many_positions_does_the_tail_rope_visit_at_least_once(test_input):
    rope = Rope()
    for motion in test_input:
        rope.move(motion)
    return rope.tail.num_positions_visited()


if __name__ == '__main__':
    main()
