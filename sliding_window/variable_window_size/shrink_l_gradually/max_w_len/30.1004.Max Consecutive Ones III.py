"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""

import unittest


class Solution:
    def longestOnes(self, a: list[int], k: int) -> int:
        l = 0
        w = 0
        ans = 0
        for r in range(len(a)):
            if a[r] == 0:
                w += 1
            if w > k:
                if a[l] == 0:
                    w -= 1
                l += 1
            else:
                ans = max(r - l + 1, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)
        self.assertEqual(
            obj.longestOnes(
                [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
            ),
            10,
        )


if __name__ == "__main__":
    unittest.main()
