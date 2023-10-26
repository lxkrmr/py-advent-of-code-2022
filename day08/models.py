from dataclasses import dataclass


@dataclass(frozen=True)
class TreeInfo:
    x: int
    y: int
    height: int


@dataclass(frozen=True)
class SurroundingTrees:
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
