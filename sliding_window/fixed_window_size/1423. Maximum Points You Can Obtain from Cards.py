"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
[100,40,17,9,73,75]
We either pick the first k from front or back or by combining them in circular connected way. The window can't go 
the pass to the rest of the array. Time is O(k) and O(n)
#circular
"""


import unittest


class Solution:
    def maxScore(self, a: list[int], k: int) -> int:
        w = 0
        # initial window (right side)
        for i in range(len(a) - k, len(a)):
            w += a[i]
        ans = w
        # slide window to the right to comeback to index 0 in circular fashion
        i = 0
        while i != k:
            w += a[i] - a[i - k]
            ans = max(ans, w)
            i += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12)
        self.assertEqual(t.maxScore([2, 2, 2], 2), 4)
        self.assertEqual(t.maxScore([9, 7, 7, 9, 7, 7, 9], 7), 55)
        self.assertEqual(t.maxScore([100, 40, 17, 9, 73, 75], 3), 248)
        self.assertEqual(t.maxScore([1, 1000, 1], 1), 1)


if __name__ == "__main__":
    unittest.main()
