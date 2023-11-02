"""
https://leetcode.com/problems/maximum-erasure-value/description/
#unique_set
"""

import unittest


class Solution:
    def maximumUniqueSubarray(self, a: list[int]) -> int:
        bst = 0
        w_s = set()
        w_v = 0
        l = 0
        for r in range(len(a)):
            while a[r] in w_s:
                # shift l to the right of the problematic num
                w_v -= a[l]
                w_s.remove(a[l])
                l += 1
            w_v += a[r]
            w_s.add(a[r])
            bst = max(w_v, bst)
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumUniqueSubarray([4, 2, 4, 5, 6]), 17)
        self.assertEqual(t.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]), 8)
        self.assertEqual(
            t.maximumUniqueSubarray(
                [
                    187,
                    470,
                    25,
                    436,
                    538,
                    809,
                    441,
                    167,
                    477,
                    110,
                    275,
                    133,
                    666,
                    345,
                    411,
                    459,
                    490,
                    266,
                    987,
                    965,
                    429,
                    166,
                    809,
                    340,
                    467,
                    318,
                    125,
                    165,
                    809,
                    610,
                    31,
                    585,
                    970,
                    306,
                    42,
                    189,
                    169,
                    743,
                    78,
                    810,
                    70,
                    382,
                    367,
                    490,
                    787,
                    670,
                    476,
                    278,
                    775,
                    673,
                    299,
                    19,
                    893,
                    817,
                    971,
                    458,
                    409,
                    886,
                    434,
                ]
            ),
            16911,
        )


if __name__ == "__main__":
    unittest.main()
