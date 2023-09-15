"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/
sort from least to most max then skip any overlap


[[1,3],[2,6],[8,10],[15,18],[1,20]]
[[1,3],[2,6],[8,10],[15,18],[1,20]]
[[1,3],[8,10],[15,18]]


[[1,2],[1,8],[2,3],[3,41],[4,5],[4,7]]
[[1,2],[2,3],[4,5],[4,7],[1,8],[3,41]]
[[1,2],[4,5]]



[[1,5],[2,3],[3,41],[4,5],[4,7]]
[[2,3],[1,5],[4,5],[4,7],[3,41]]
[[2,3],[4,5]]



[[1,2],[3,5],[4,8],[6,8],[7,10]]
[[1,2],[3,5],[6,8],[4,8],[7,10]]

"""

import unittest


class Solution:
    def findLongestChain(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_picked_end = intervals[0][1]
        ans = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > last_picked_end:
                last_picked_end = interval[1]
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findLongestChain([[1, 2], [2, 3], [3, 4]]), 2)
        self.assertEqual(t.findLongestChain([[1, 2], [7, 8], [4, 5]]), 3)


if __name__ == "__main__":
    unittest.main()
