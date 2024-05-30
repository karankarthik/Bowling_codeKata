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


    # Spare bonus
    # Strike bonus
    

if __name__ == "__main__":
    unittest.main()

