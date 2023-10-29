import unittest

from day09.models import Rope, Motion, Direction


class TestRopeMovement(unittest.TestCase):

    def test_rope_moves_right(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.RIGHT, 3))

        self.assertEqual((3, 0), rope.head.coords())
        self.assertEqual((1, 0), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_left(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.LEFT, 3))

        self.assertEqual((-3, 0), rope.head.coords())
        self.assertEqual((-1, 0), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_up(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.UP, 3))

        self.assertEqual((0, 3), rope.head.coords())
        self.assertEqual((0, 1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_down(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.DOWN, 3))

        self.assertEqual((0, -3), rope.head.coords())
        self.assertEqual((0, -1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_right_up(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.RIGHT, 1))
        rope.move(Motion(Direction.UP, 3))

        self.assertEqual((1, 3), rope.head.coords())
        self.assertEqual((1, 1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_up_right(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.UP, 1))
        rope.move(Motion(Direction.RIGHT, 3))

        self.assertEqual((3, 1), rope.head.coords())
        self.assertEqual((1, 1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_right_down(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.RIGHT, 1))
        rope.move(Motion(Direction.DOWN, 3))

        self.assertEqual((1, -3), rope.head.coords())
        self.assertEqual((1, -1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_down_right(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.DOWN, 1))
        rope.move(Motion(Direction.RIGHT, 3))

        self.assertEqual((3, -1), rope.head.coords())
        self.assertEqual((1, -1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_left_down(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.LEFT, 1))
        rope.move(Motion(Direction.DOWN, 3))

        self.assertEqual((-1, -3), rope.head.coords())
        self.assertEqual((-1, -1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_down_left(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.DOWN, 1))
        rope.move(Motion(Direction.LEFT, 3))

        self.assertEqual((-3, -1), rope.head.coords())
        self.assertEqual((-1, -1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_left_up(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.LEFT, 1))
        rope.move(Motion(Direction.UP, 3))

        self.assertEqual((-1, 3), rope.head.coords())
        self.assertEqual((-1, 1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())

    def test_rope_moves_up_left(self):
        rope = Rope(numer_of_knots=3)

        rope.move(Motion(Direction.UP, 1))
        rope.move(Motion(Direction.LEFT, 3))

        self.assertEqual((-3, 1), rope.head.coords())
        self.assertEqual((-1, 1), rope.tip_of_the_tail().coords())
        self.assertEqual(2, rope.tip_of_the_tail().num_positions_visited())


if __name__ == '__main__':
    unittest.main()
