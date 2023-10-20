"""
https://leetcode.com/problems/left-and-right-sum-differences/
"""
import unittest


class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        dp1 = [0 for _ in range(len(a))]
        for i in range(1, len(a)):
            dp1[i] = a[i - 1] + dp1[i - 1]

        dp2 = [0 for _ in range(len(a))]
        for i in range(len(a) - 2, -1, -1):
            dp2[i] = a[i + 1] + dp2[i + 1]

        ans = [0 for _ in range(len(a))]
        for i in range(len(dp1)):
            ans[i] = abs(dp1[i] - dp2[i])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.leftRightDifference([10, 4, 8, 3]), [15, 1, 11, 22])


if __name__ == "__main__":
    unittest.main()
