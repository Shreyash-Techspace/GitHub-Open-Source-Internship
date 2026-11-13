import unittest
from agent.stats import median

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([2, 4, 6]), 4)

    def test_even_length(self):
        self.assertEqual(median([2, 4, 6, 8]), 5)

    def test_even_length_another_example(self):
        self.assertEqual(median([1, 3, 5, 7]), 4)

if __name__ == "__main__":
    unittest.main()