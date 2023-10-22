"""
https://leetcode.com/problems/find-pivot-index/

[1,7,3, 6, 5, 6]
0  1  2 3  4  5
[1,8,11,17,22,28]

[4,-3,5,-7,8]
0  1  2  3  4
[4,1, 6, -1,7]


[2, 1, -1]
prefix: [2,3,2]

if what's on the right of the pivot equals to what's on the right

"""
import unittest


class Solution:
    def pivotIndex(self, a: list[int]) -> int:
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
        self.assertEqual(t.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(t.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(t.pivotIndex([4, -3, 5, -7, 8]), 2)
        self.assertEqual(t.pivotIndex([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()