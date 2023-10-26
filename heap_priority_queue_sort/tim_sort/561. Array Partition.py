"""
https://leetcode.com/problems/array-partition
"""

import unittest


class Solution:
    def arrayPairSum(self, a: list[int]) -> int:
        a.sort()
        ans = 0
        for i in range(0, len(a), 2):
            ans += a[i]
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.arrayPairSum([1, 4, 3, 2]), 4)


if __name__ == "__main__":
    unittest.main()
