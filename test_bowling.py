import unittest
from bowling import bowling_score

class Testbowling_score(unittest.TestCase):
    def test_bowling_score(self):
        pins, ball, frames = bowling_score({})
        print (pins, ball, frames)

        self.assertEqual(pins, 0)
        self.assertEqual(ball, 0)
        self.assertEqual(frames, 0)

    def test_for_strike_on_first_ball(self):
        rolls = [10]
        total, ball, frames = bowling_score(rolls)

        self.assertEqual(ball, 1)
        self.assertEqual(frames, 1)
        self.assertEqual(total, 10)

if __name__ == "__main__":
    unittest.main()

