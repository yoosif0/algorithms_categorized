"""
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
#store_index
#store_last_index
#unique
#find_min_w_len
"""

import unittest
import sys


class Solution:
    def minimumCardPickup(self, a: list[int]) -> int:
        ans = sys.maxsize
        m = {}
        for r in range(len(a)):
            if a[r] in m:
                # w_size is the min window size that accompany the same number
                w_size = r - m[a[r]] + 1
                ans = min(w_size, ans)
            m[a[r]] = r
        return -1 if ans == sys.maxsize else ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minimumCardPickup([3, 4, 2, 3, 4, 7]), 4)
        self.assertEqual(t.minimumCardPickup([1, 0, 5, 3]), -1)
        self.assertEqual(
            t.minimumCardPickup(
                [
                    95,
                    11,
                    8,
                    65,
                    5,
                    86,
                    30,
                    27,
                    30,
                    73,
                    15,
                    91,
                    30,
                    7,
                    37,
                    26,
                    55,
                    76,
                    60,
                    43,
                    36,
                    85,
                    47,
                    96,
                    6,
                ]
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
