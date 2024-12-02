"""
https://leetcode.com/problems/unique-paths-ii/
[0, 0, 0],
[0, 1, 0],
[0, 0, 0]

211
101
111

Control: Fill bottommost and rightmost lines with either 0 or 1. If blocked:0.
If not blocked: 1. It can be blocked by either the point itself is blocked or
the value leading to it is blocked.

#count_combinations
"""
import unittest
from algoutils.twod_array import p2dnl

def f(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-1] = 1 if grid[-1][-1] == 0 else 0
    # fill right-most column buttom to up. c is that column
    c = n - 1 
    for r in range(m - 2, -1, -1):
        blocked = grid[r][c] == 1 or dp[r+1][c] == 0
        dp[r][c] = int(not blocked)
    # fill bottom-most row right to left. r is that row
    r = m - 1
    for c in range(n - 2, -1, -1):
        blocked = grid[r][c] == 1 or dp[r][c+1] == 0
        dp[r][c] = int(not blocked)
    p2dnl(dp, width=2)
    for r in range(m - 2, -1, -1):
        for c in range(n - 2, -1, -1):
            blocked = grid[r][c] == 1
            if blocked:
                dp[r][c] = 0
            else:
                down = dp[r+1][c]
                right = dp[r][c+1]
                dp[r][c] = right + down
    return dp[0][0]



class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        return f(grid)

a = [
    [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        2
    ],
    [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        2
    ],
    [
        [
            [0, 1],
            [0, 0],
        ],
        1
    ],
    [
        [
            [0, 0],
            [0, 1],
        ],
        0
    ]
]
class Test(unittest.TestCase):
    def test(self):
        for x in a:
            self.assertEqual(f(x[0]), x[1])


if __name__ == "__main__":
    unittest.main()
