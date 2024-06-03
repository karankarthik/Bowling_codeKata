import unittest
from bowling import bowling_score

class Testbowling_score(unittest.TestCase):
    def test_bowling_score(self):
        pins, ball, frames = bowling_score([])
        print (pins, ball, frames)

        self.assertEqual(pins, 0)
        self.assertEqual(ball, 0)
        self.assertEqual(frames, 0)

    def test_for_strike_on_first_ball(self):
        rolls = [0,10]
        total, ball, frames = bowling_score(rolls)
        print ("total strike:", total)

        self.assertEqual(ball, 0)
        self.assertEqual(frames, 1)
        self.assertEqual(total, 10)

    def test_for_complete_miss(self):
        rolls = [0,0]
        total, ball, frames = bowling_score(rolls)
        print ("total miss:", total)

        self.assertEqual(ball, 0)
        self.assertEqual(frames, 1)
        self.assertEqual(total, 0)
    
    def test_for_regular_throw(self):
        rolls = [6,2]
        total, ball, frames = bowling_score(rolls)
        print("total_for_regular_throw", total)

        self.assertEqual(ball, 0)
        self.assertEqual(frames, 1)
        self.assertEqual(total, 8)

    def test_for_strike_with_bonus(self):
        rolls = [10, 4, 3]
        total, ball, frames = bowling_score(rolls)
        print("total for strike with bonus", total)

        self.assertEqual(ball, 0)
        self.assertEqual(frames, 2)
        self.assertEqual(total, 24)

    def test_for_spare_with_bonus(self):
        rolls = [5, 5, 4, 2]
        total, ball, frames = bowling_score(rolls)
        print("total for spare with bonus", total)

        self.assertEqual(ball, 0)
        self.assertEqual(frames, 2)
        self.assertEqual(total, 20)

    def test_for_full_game(self):
        rolls = [5, 5, 4, 2, 10, 4, 6, 3, 4, 10, 2, 8, 2, 1, 4, 5, 2, 3]
        total, ball, frames = bowling_score(rolls)
        print("total for full game", total)

        self.assertEqual(ball, 2)
        self.assertEqual(frames, 1)
        self.assertEqual(total, 109)

    def test_for_full_game_with_strike_at_end(self):
        rolls = [5, 5, 4, 2, 10, 4, 6, 3, 4, 10, 2, 8, 2, 1, 4, 5, 10, 10, 3]
        total, ball, frames = bowling_score(rolls)
        print("total for full game with strike at the end", total)

        self.assertEqual(ball, 3)
        self.assertEqual(frames, 9)
        self.assertEqual(total, 127)

if __name__ == "__main__":
    unittest.main()


