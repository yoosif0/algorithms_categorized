"""
https://leetcode.com/problems/left-and-right-sum-differences/
#prefix_suffix
10 4 8 3
15 
"""
import unittest


class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        pre = 0
        suf = sum(a)
        ans = [0 for _ in range(len(a))]
        for i in range(len(a)):
            suf -= a[i]
            ans[i] = abs(suf - pre)
            pre += a[i]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.leftRightDifference([10, 4, 8, 3]), [15, 1, 11, 22])


if __name__ == "__main__":
    unittest.main()
