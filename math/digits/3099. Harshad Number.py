"""
https://leetcode.com/problems/harshad-number
"""

import unittest


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, n: int) -> int:
        sum = 0
        cur = n
        while cur:
            sum += cur % 10
            cur //= 10
        return -1 if n % sum != 0 else sum


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sumOfTheDigitsOfHarshadNumber(18), 9)
        self.assertEqual(t.sumOfTheDigitsOfHarshadNumber(23), -1)


if __name__ == "__main__":
    unittest.main()
