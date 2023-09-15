"""
https://leetcode.com/problems/merge-intervals/

[[1,3],[2,6],[8,10],[15,18],[1,20]]
[[1,3],[1,20],[2,6],[8,10],[15,18]]


"""

import unittest


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            last_picked = ans[-1]
            if interval[0] <= last_picked[1]:
                ans[-1][1] = max(last_picked[1], interval[1])
            else:
                ans.append(interval)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(
            t.merge([[1, 4], [4, 5]]),
            [[1, 5]],
        )
        self.assertEqual(
            t.merge([[1, 3], [2, 6], [8, 10], [15, 18], [3, 17], [1, 17], [2, 17]]),
            [[1, 18]],
        )


if __name__ == "__main__":
    unittest.main()
