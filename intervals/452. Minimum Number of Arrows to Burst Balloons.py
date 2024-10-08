"""
@nested-tags:intervals/cur_end,greedy
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

[[1,2],[2,3],[3,4],[4,5]]
0: max for first = 2, shot and last_shot 2, finished=1
1: if last_shot >= b[i][0], then finished=2
2: b[i][1] = 4, shot++; finished++; last_shot 4
3: if last_shot >= b[i][0]; finished++
return finished
"""

import unittest


class Solution:
    def findMinArrowShots(self, a: list[list[int]]) -> int:
        a.sort(key=lambda x: x[1])
        ans = 1
        cur_end = a[0][1]
        for i in range(1, len(a)):
            if a[i][0] > cur_end:
                cur_end = a[i][1]
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)
        self.assertEqual(t.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
        self.assertEqual(t.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
        self.assertEqual(
            t.findMinArrowShots(
                [
                    [3, 9],
                    [7, 12],
                    [3, 8],
                    [6, 8],
                    [9, 10],
                    [2, 9],
                    [0, 9],
                    [3, 9],
                    [0, 6],
                    [2, 8],
                ]
            ),
            2,
        )


if __name__ == "__main__":
    unittest.main()
