"""
https://leetcode.com/problems/plus-one/
"""

import unittest


class Solution:
    def plusOne(self, a: list[int]) -> list[int]:
        i = len(a) - 1
        while True:
            if i == -1:
                return [1] + a
            if a[i] != 9:
                a[i] += 1
                return a
            else:
                a[i] = 0
                i -= 1


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(obj.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(obj.plusOne([9]), [1, 0])


if __name__ == "__main__":
    unittest.main()
