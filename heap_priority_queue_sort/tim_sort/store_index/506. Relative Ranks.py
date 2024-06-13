"""
https://leetcode.com/problems/relative-ranks/
#store_index_before_sorting
"""

import unittest


class Solution:
    def findRelativeRanks(self, a: list[int]) -> list[str]:
        m = {}
        ac = sorted(a, reverse=True)
        for i in range(len(ac)):
            m[ac[i]] = i
        aa = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(a)):
            ord = m[a[i]]
            a[i] = aa[ord] if ord < 3 else str(ord + 1)
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.findRelativeRanks([5, 4, 3, 2, 1]),
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        )
        self.assertEqual(
            obj.findRelativeRanks([10, 3, 8, 9, 4]),
            ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
        )


if __name__ == "__main__":
    unittest.main()
