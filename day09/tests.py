import unittest

from day09.models import Rope, Motion, Direction


class TestRopeMovement(unittest.TestCase):

    def test_rope_moves_right(self):
        rope = Rope()

        rope.move(Motion(Direction.RIGHT, 2))

        self.assertEqual((2, 0), rope.head.coords())
        self.assertEqual((1, 0), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_left(self):
        rope = Rope()

        rope.move(Motion(Direction.LEFT, 2))

        self.assertEqual((-2, 0), rope.head.coords())
        self.assertEqual((-1, 0), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_up(self):
        rope = Rope()

        rope.move(Motion(Direction.UP, 2))

        self.assertEqual((0, 2), rope.head.coords())
        self.assertEqual((0, 1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_down(self):
        rope = Rope()

        rope.move(Motion(Direction.DOWN, 2))

        self.assertEqual((0, -2), rope.head.coords())
        self.assertEqual((0, -1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_right_up(self):
        rope = Rope()

        rope.move(Motion(Direction.RIGHT, 1))
        rope.move(Motion(Direction.UP, 2))

        self.assertEqual((1, 2), rope.head.coords())
        self.assertEqual((1, 1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_up_right(self):
        rope = Rope()

        rope.move(Motion(Direction.UP, 1))
        rope.move(Motion(Direction.RIGHT, 2))

        self.assertEqual((2, 1), rope.head.coords())
        self.assertEqual((1, 1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_right_down(self):
        rope = Rope()

        rope.move(Motion(Direction.RIGHT, 1))
        rope.move(Motion(Direction.DOWN, 2))

        self.assertEqual((1, -2), rope.head.coords())
        self.assertEqual((1, -1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_down_right(self):
        rope = Rope()

        rope.move(Motion(Direction.DOWN, 1))
        rope.move(Motion(Direction.RIGHT, 2))

        self.assertEqual((2, -1), rope.head.coords())
        self.assertEqual((1, -1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_left_down(self):
        rope = Rope()

        rope.move(Motion(Direction.LEFT, 1))
        rope.move(Motion(Direction.DOWN, 2))

        self.assertEqual((-1, -2), rope.head.coords())
        self.assertEqual((-1, -1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_down_left(self):
        rope = Rope()

        rope.move(Motion(Direction.DOWN, 1))
        rope.move(Motion(Direction.LEFT, 2))

        self.assertEqual((-2, -1), rope.head.coords())
        self.assertEqual((-1, -1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_left_up(self):
        rope = Rope()

        rope.move(Motion(Direction.LEFT, 1))
        rope.move(Motion(Direction.UP, 2))

        self.assertEqual((-1, 2), rope.head.coords())
        self.assertEqual((-1, 1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())

    def test_rope_moves_up_left(self):
        rope = Rope()

        rope.move(Motion(Direction.UP, 1))
        rope.move(Motion(Direction.LEFT, 2))

        self.assertEqual((-2, 1), rope.head.coords())
        self.assertEqual((-1, 1), rope.tail.coords())
        self.assertEqual(2, rope.tail.num_positions_visited())


if __name__ == '__main__':
    unittest.main()
