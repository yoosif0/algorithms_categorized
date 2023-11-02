"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
13,10,7,6,5,4,1 z=5
13
10 use 3
7 nothing would help here. shift l to be 10 and calculate new z
#no_need_valid_w
#find_max_w_len
#sorting_helps
"""

import unittest


class Solution:
    def maxFrequency(self, a: list[int], k: int) -> int:
        a.sort(reverse=True)
        ans = 1
        l = 0
        w = k
        for r in range(1, len(a)):
            w = w - (a[l] - a[r])
            if w < 0:
                diff = a[l] - a[l + 1]
                w = w + diff * (r - l)
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxFrequency([1, 2, 4], 5), 3)
        self.assertEqual(t.maxFrequency([1, 4, 8, 13], 5), 2)
        self.assertEqual(t.maxFrequency([3, 9, 6], 2), 1)
        self.assertEqual(
            t.maxFrequency(
                [
                    9940,
                    9995,
                    9944,
                    9937,
                    9941,
                    9952,
                    9907,
                    9952,
                    9987,
                    9964,
                    9940,
                    9914,
                    9941,
                    9933,
                    9912,
                    9934,
                    9980,
                    9907,
                    9980,
                    9944,
                    9910,
                    9997,
                ],
                7925,
            ),
            22,
        )


if __name__ == "__main__":
    unittest.main()
