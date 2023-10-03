"""
https://leetcode.com/problems/non-overlapping-intervals/
#overlapping_interval
#interval_scheduling

[[1,2],[2,3],[3,4],[1,4],[4,5],[1,2],[4,7],[1,8]]
[[1,2],[1,2],[2,3],[3,4],[1,4],[4,5],[4,7],[1,8]]
[[1,2],[2,3],[3,4],[4,5]]


[[1,2],[1,3],[3,4],[1,4],[4,5],[1,2],[4,7],[1,8]]
[[1,2],[1,2],[1,3],[3,4],[1,4],[4,5],[4,7],[1,8]]
[[1,2],[3,4],[4,5]]



[[1,8],[2,3],[3,4],[4,5],[4,7]]
[[2,3],[3,4],[4,5],[4,7],[1,8]]
[[2,3],[3,4],[4,5]]



[[1,8],[2,5],[3,4],[4,5],[1,5],[4,7]]
[[3,4],[2,5],[4,5],[1,5],[4,7],[1,8]]
[[3,4],[4,5]]
sort by by end interval but pick the one with lowest range if more than one has the same end interval



"""
import unittest


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_picked_end = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < last_picked_end:
                ans += 1
            else:
                last_picked_end = interval[1]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.eraseOverlapIntervals(
                [[1, 2], [2, 3], [3, 4], [1, 4], [4, 5], [1, 2], [4, 7], [1, 8]]
            ),
            4,
        )
        self.assertEqual(
            t.eraseOverlapIntervals(
                [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5], [1, 2], [4, 7], [1, 8]]
            ),
            5,
        )
        self.assertEqual(
            t.eraseOverlapIntervals([[1, 8], [2, 3], [3, 4], [4, 5], [4, 7]]),
            2,
        )
        self.assertEqual(
            t.eraseOverlapIntervals([[1, 8], [2, 5], [3, 4], [4, 5], [1, 5], [4, 7]]),
            4,
        )
        self.assertEqual(
            t.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]),
            2,
        )
        self.assertEqual(
            t.eraseOverlapIntervals([[1, 2], [2, 3]]),
            0,
        )


if __name__ == "__main__":
    unittest.main()
