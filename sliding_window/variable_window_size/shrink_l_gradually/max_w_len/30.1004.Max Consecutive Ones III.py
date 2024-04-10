"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""

import unittest


class Solution:
    def longestOnes(self, a: list[int], k: int) -> int:
        w_l = 0
        w_k = 0
        ans = 0
        for r in range(len(a)):
            if a[r] == 1:
                ans = max(r - w_l + 1, ans)
            elif a[r] == 0 and w_k < k:
                w_k += 1
                ans = max(r - w_l + 1, ans)
            else:
                while a[w_l] == 1:
                    w_l += 1
                w_l += 1
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
