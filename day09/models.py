from lib.utils import file_to_lines
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


@dataclass(frozen=True)
class Motion:
    direction: Direction
    times: int

    @classmethod
    def from_str(cls, raw: str):
        direction_str, times_str = raw.split(' ')
        return cls(Direction(direction_str), int(times_str))


def motions_from_file(filename: str) -> list[Motion]:
    return [Motion.from_str(line) for line in file_to_lines(filename)]


class Head:
    def __init__(self):
        self._x = 0
        self._y = 0

    def coords(self) -> Tuple[int, int]:
        return self._x, self._y

    def move(self, direction: Direction) -> None:
        match direction:
            case Direction.RIGHT:
                self._x += 1
            case Direction.UP:
                self._y += 1
            case Direction.LEFT:
                self._x -= 1
            case Direction.DOWN:
                self._y -= 1


class TailSegment:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._positions = {self.coords()}

    def coords(self) -> Tuple[int, int]:
        return self._x, self._y

    def num_positions_visited(self) -> int:
        return len(self._positions)

    def follow_head(self, head: Head) -> None:
        head_x, head_y = head.coords()
        self._follow(head_x, head_y)

    def follow_tail(self, tail: 'TailSegment') -> None:
        tail_x, tail_y = tail.coords()
        self._follow(tail_x, tail_y)

    def _follow(self, x_to_follow: int, y_to_follow: int):
        delta_x = x_to_follow - self._x
        delta_y = y_to_follow - self._y

        self._x += self._calculate_x_movement(delta_x, delta_y)
        self._y += self._calculate_y_movement(delta_x, delta_y)

        self._positions.add(self.coords())

    def _calculate_x_movement(self, delta_x, delta_y) -> int:
        return self._calculate_movement(delta_x, delta_y)

    def _calculate_y_movement(self, delta_x, delta_y) -> int:
        return self._calculate_movement(delta_y, delta_x)

    @staticmethod
    def _calculate_movement(primary_delta, secondary_delta) -> int:
        if abs(primary_delta) % 2 == 0:
            return primary_delta / 2
        elif abs(primary_delta) == 1 and abs(secondary_delta) == 2:
            return primary_delta
        else:
            return 0


class Rope:

    def __init__(self, numer_of_knots: int = 2):
        self.head = Head()
        self.tail = [TailSegment() for _ in range(0, numer_of_knots - 1)]

    def move(self, motion: Motion) -> None:
        for _ in range(0, motion.times):
            self.head.move(motion.direction)
            self._move_tail()

    def _move_tail(self):
        first = self.tail[0]
        first.follow_head(self.head)
        prev = first
        for tail in self.tail[1:]:
            tail.follow_tail(prev)
            prev = tail

    def tip_of_the_tail(self):
        return self.tail[-1]
