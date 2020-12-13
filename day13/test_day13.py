import unittest
from day13 import *

class TestChineseRemainderTheorem(unittest.TestCase):

    def test_part2(self):
        # list of ({bus1: offset1, ...}, solution) pairs
        test_cases = [
            ({4: 0, 5:1, 7:6}, 64)
        ]

        for buses, expected in test_cases:
            actual = part2(buses)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
