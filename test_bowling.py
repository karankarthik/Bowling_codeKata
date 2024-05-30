import unittest
from bowling import bowling_score

class Testbowling_score(unittest.TestCase):
    def test_bowling_score(self):
        score, frame_index, frames = bowling_score({})

        self.assertEqual(score, 2)
        self.assertEqual(frame_index, 3)
        self.assertEqual(frames, 4)

if __name__ == "__main__":
    unittest.main()