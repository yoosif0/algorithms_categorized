"""
https://leetcode.com/problems/find-the-middle-index-in-array/
if what's on the right of the pivot equals to what's on the right
same as 724
"""
import unittest


class Solution:
    def findMiddleIndex(self, a: list[int]) -> int:
        dp = [0 for _ in range(len(a) + 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + a[i - 1]
        for i in range(1, len(dp)):
            if dp[-1] - dp[i] == dp[i - 1]:
                return i - 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pivotIndex([2, 3, -1, 8, 4]), 3)


if __name__ == "__main__":
    unittest.main()
