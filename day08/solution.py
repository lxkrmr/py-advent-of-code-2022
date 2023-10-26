import numpy as np
from dataclasses import dataclass


def load_numpy_array(filename: str):
    return np.array(
        [
            [
                digit
                for
                digit
                in row
            ]
            for row
            in (np.loadtxt(filename, dtype=str))],
        dtype=np.int8
    )


@dataclass(frozen=True)
class TreeInfo:
    x: int
    y: int
    height: int


@dataclass(frozen=True)
class NearbyTreeHeights:
    left: list[int]
    right: list[int]
    up: list[int]
    down: list[int]

    def all_directions(self) -> list[list[int]]:
        return [
            self.left,
            self.right,
            self.up,
            self.down,
        ]


def nearby_tree_heights(tree_info: TreeInfo, all_tree_heights) -> NearbyTreeHeights:
    row = all_tree_heights[tree_info.x]
    column = all_tree_heights[:, tree_info.y]

    left = row[:tree_info.y]
    right = row[tree_info.y + 1:]
    up = column[:tree_info.x]
    down = column[tree_info.x + 1:]

    return NearbyTreeHeights(left=left, right=right, up=up, down=down)


def is_tree_visible(tree_info: TreeInfo, nearby_trees: NearbyTreeHeights) -> bool:
    result = [
        is_tree_visible_from_direction(tree_info.height, direction)
        for direction
        in nearby_trees.all_directions()
    ]
    print(tree_info, result)
    return any(result)


def is_tree_visible_from_direction(tree_height: int, direction: list[int]) -> bool:
    return len(direction) == 0 or max(direction) < tree_height


def part_one(all_trees: np.ndarray) -> int:
    total = 0
    for (x, y), height in np.ndenumerate(all_trees):
        tree_info = TreeInfo(x=x, y=y, height=height)
        nearby_trees = nearby_tree_heights(tree_info, all_trees)
        if is_tree_visible(tree_info, nearby_trees):
            total += 1

    return total


def main():
    test_input = load_numpy_array('test_input.txt')
    puzzle_input = load_numpy_array('puzzle_input.txt')

    assert part_one(test_input) == 21
    print(part_one(puzzle_input))


if __name__ == '__main__':
    main()
