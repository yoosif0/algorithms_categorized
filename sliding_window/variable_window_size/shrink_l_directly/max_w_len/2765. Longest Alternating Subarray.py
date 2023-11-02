"""
https://leetcode.com/problems/longest-alternating-subarray/
"""
import unittest


class Solution:
    def alternatingSubarray(self, a: list[int]) -> int:
        l = 0
        bst = -1
        for r in range(1, len(a)):
            if (a[r] == a[r - 1] + 1 and r % 2 != l % 2) or (
                a[r] == a[r - 1] - 1 and r % 2 == l % 2
            ):
                # good and window is valid
                bst = max(bst, r - l + 1)
            elif a[r] == a[r - 1] + 1:
                # not good but we found a new pattern starting from r-1
                l = r - 1
            else:
                # reset window
                l = r
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.alternatingSubarray([2, 3, 4, 3, 4]), 4)
        self.assertEqual(t.alternatingSubarray([4, 5, 6]), 2)
        self.assertEqual(t.alternatingSubarray([21, 9, 5]), -1)


if __name__ == "__main__":
    unittest.main()
