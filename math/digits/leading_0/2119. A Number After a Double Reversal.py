"""
https://leetcode.com/problems/a-number-after-a-double-reversal
as long as the reversed number has no leading zeroes, reversing it again should lead to the original number

"Reversed number has leading 0" == "original number ends with 0"

The only exception is if the original number is 0
"""

import unittest


class Solution:
    def isSameAfterReversals(self, n: int) -> bool:
        if n == 0:
            return True
        return not n % 10 == 0


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.isSameAfterReversals(1800), False)
        self.assertEqual(t.isSameAfterReversals(625), True)
        self.assertEqual(t.isSameAfterReversals(0), True)


if __name__ == "__main__":
    unittest.main()
