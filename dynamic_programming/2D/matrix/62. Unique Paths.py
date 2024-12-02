"""
https://leetcode.com/problems/unique-paths/
#count_combinations

Logic: Solve subproblems from smallest to biggest grid. Start by 1x1 grid.
Which have 1 unique paths. Also any point in the right most or bottom most
has 1 unique path. 

Control: Fill rightmost and bottommost lines as shown below. Then fill the rest
from bottom-right to top-left. Fill m-2 row, then m-3, m-4, etc

..1
..1
..1
..1
..1
..1
111

"""
import unittest


def f(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    # fill right-most column. c is that column
    c = n - 1
    for r in range(m - 1, -1, -1):
        dp[r][c] = 1
    # fill bottom-most row. r is that row
    r = m - 1
    for c in range(n - 1, -1, -1):
        dp[r][c] = 1
    for r in range(m - 2, -1, -1):
        for c in range(n - 2, -1, -1):
            down = dp[r + 1][c]
            right = dp[r][c + 1]
            dp[r][c] = down + right
    return dp[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return f(m,n)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.uniquePaths(3, 7), 28)
        self.assertEqual(t.uniquePaths(4, 7), 84)


if __name__ == "__main__":
    unittest.main()
