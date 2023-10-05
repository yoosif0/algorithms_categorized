"""
https://leetcode.com/problems/plus-one/
"""

import unittest


class Solution:
    def plusOne(self, a: list[int]) -> list[int]:
        r = len(a) - 1
        while True:
            if r == -1:
                return [1] + a
            if a[r] != 9:
                a[r] += 1
                return a
            else:
                a[r] = 0
                r -= 1


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(obj.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(obj.plusOne([9]), [1, 0])


if __name__ == "__main__":
    unittest.main()
