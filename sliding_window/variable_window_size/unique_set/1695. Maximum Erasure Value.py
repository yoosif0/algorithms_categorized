"""
https://leetcode.com/problems/maximum-erasure-value/description/
#unique
"""

import unittest
import dataclasses


@dataclasses.dataclass
class WindowState:
    total: int
    nums: set[int]


class Solution:
    def maximumUniqueSubarray(self, a: list[int]) -> int:
        ans = 0
        w = WindowState(0, set())
        l = 0
        for r in range(len(a)):
            if a[r] in w.nums:
                # shift l to the right of the problematic num
                while True:
                    w.total -= a[l]
                    w.nums.remove(a[l])
                    if a[l] == a[r]:
                        l += 1
                        break
                    l += 1
            w.total += a[r]
            w.nums.add(a[r])
            ans = max(w.total, ans)
        return ans


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
