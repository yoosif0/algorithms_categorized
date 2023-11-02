"""
https://leetcode.com/problems/longest-turbulent-subarray/
keep window unless the trend changes, then reset it
"""


import unittest


class Solution:
    def maxTurbulenceSize(self, a: list[int]) -> int:
        l = 0
        bst = 1
        # window flag that describes the status of the window of whether odd indecis hold higher numbers or the other way around
        w = True
        for r in range(1, len(a)):
            if a[r] == a[r - 1]:
                # shrink l to be the same as r because the one does not work
                l = r
                continue
            fl = (a[r] < a[r - 1]) if r % 2 != 0 else (a[r] > a[r - 1])
            # shrink l to the one before if the trend is different
            if w != fl:
                l = r - 1
                w = not w
            bst = max(bst, r - l + 1)
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
        self.assertEqual(t.maxTurbulenceSize([4, 8, 12, 16]), 2)
        self.assertEqual(t.maxTurbulenceSize([100]), 1)
        self.assertEqual(t.maxTurbulenceSize([9, 9]), 1)


if __name__ == "__main__":
    unittest.main()
