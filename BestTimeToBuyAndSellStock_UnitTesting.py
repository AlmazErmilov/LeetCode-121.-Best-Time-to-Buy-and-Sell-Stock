import unittest
from BestTimeToBuyAndSellStock_final import bestTimeToBuyAndSellStock

test_cases = [
    ([22,1,5], 4),
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0), 
    ([5,10,1,3,2,1,2], 5),
    ([21,22,1,5,7,2], 6),
    ([21,22,10,15,1,3], 5)
]

class TestValidClockTimes(unittest.TestCase):
    def test_all(self):
        for stock, expected in test_cases:
            with self.subTest(case=stock, expected=expected):
                result = bestTimeToBuyAndSellStock(stock)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
