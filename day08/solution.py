import numpy as np

from models import TreeInfo, SurroundingTrees
from utils import load_numpy_array


def part_one_how_many_trees_are_visible_from_outside_the_grid(all_trees: np.ndarray) -> int:
    number_of_visible_trees = 0
    for (x, y), height in np.ndenumerate(all_trees):
        tree_info = TreeInfo(x, y, height)
        surrounding_trees = get_surrounding_trees(tree_info, all_trees)
        if is_tree_visible(tree_info, surrounding_trees):
            number_of_visible_trees += 1

    return number_of_visible_trees


def get_surrounding_trees(tree_info: TreeInfo, all_tree_heights) -> SurroundingTrees:
    row = all_tree_heights[tree_info.x]
    left = row[:tree_info.y]
    right = row[tree_info.y + 1:]

    column = all_tree_heights[:, tree_info.y]
    up = column[:tree_info.x]
    down = column[tree_info.x + 1:]

    return SurroundingTrees(left, right, up, down)


def is_tree_visible(tree_info: TreeInfo, nearby_trees: SurroundingTrees) -> bool:
    return any(
        [
            is_tree_visible_from_direction(tree_info.height, direction)
            for direction
            in nearby_trees.all_directions()
        ]
    )


def is_tree_visible_from_direction(tree_height: int, direction: list[int]) -> bool:
    return len(direction) == 0 or max(direction) < tree_height


def part_two_what_is_the_highest_scenic_score_possible(all_trees: np.ndarray) -> int:
    result = [
        calc_scenic_score(TreeInfo(x, y, height), all_trees)
        for (x, y), height
        in np.ndenumerate(all_trees)
    ]
    return max(result)


def calc_scenic_score(tree_info: TreeInfo, all_trees: np.ndarray) -> int:
    surrounding_trees = get_surrounding_trees(tree_info, all_trees)

    left_from_inside_out = surrounding_trees.left[::-1]
    up_from_inside_out = surrounding_trees.up[::-1]

    score_left = scenic_score_for_direction(tree_info.height, left_from_inside_out)
    score_right = scenic_score_for_direction(tree_info.height, surrounding_trees.right)
    score_up = scenic_score_for_direction(tree_info.height, up_from_inside_out)
    score_down = scenic_score_for_direction(tree_info.height, surrounding_trees.down)

    return score_left * score_right * score_up * score_down


def scenic_score_for_direction(tree_height: int, direction: list[int]) -> int:
    scenic_score = 0
    for height in direction:
        scenic_score += 1
        if height >= tree_height:
            break

    return scenic_score


def main():
    test_input = load_numpy_array('test_input.txt')
    puzzle_input = load_numpy_array('puzzle_input.txt')

    assert part_one_how_many_trees_are_visible_from_outside_the_grid(test_input) == 21
    print(part_one_how_many_trees_are_visible_from_outside_the_grid(puzzle_input))

    assert part_two_what_is_the_highest_scenic_score_possible(test_input) == 8
    print(part_two_what_is_the_highest_scenic_score_possible(puzzle_input))


if __name__ == '__main__':
    main()
