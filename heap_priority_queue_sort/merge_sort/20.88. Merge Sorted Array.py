"""
https://leetcode.com/problems/merge-sorted-array

This is like "simplest_merge_sort.py" but here you need to do it in place.

We fill "ans" from right to left because the empty space we have is on the right of one of the arrays

1 2 2 3 6 6          2 5 6
  i,m             n     
"""

import unittest


class Solution:
    def merge(self, a: list[int], m: int, a2: list[int], n: int) -> None:
        n -= 1
        m -= 1
        for i in range(len(a) - 1, -1, -1):
            if n < 0:
                break
            if m >= 0 and a[m] > a2[n]:
                a[i] = a[m]
                m -= 1
            else:
                a[i] = a2[n]
                n -= 1
        return a

class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6]
        )
        self.assertEqual(t.merge([1, 2, 4, 5, 6, 0], 5, [3], 1), [1, 2, 3, 4, 5, 6])
        self.assertEqual(t.merge([1], 1, [], 0), [1])
        self.assertEqual(t.merge([0], 0, [1], 1), [1])
        self.assertEqual(
            t.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), [1, 2, 3, 4, 5, 6]
        )
        self.assertEqual(
            t.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5), [1, 2, 3, 4, 5, 6]
        )


if __name__ == "__main__":
    unittest.main()
