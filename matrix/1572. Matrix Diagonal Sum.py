"""
https://leetcode.com/problems/matrix-diagonal-sum/
#traversal 
"""

import unittest


class Solution:
    def diagonalSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        ans = 0
        for i in range(m):
            ans += grid[i][i]
            # mark so that it's not counted twice
            grid[i][i] = 0
        for i in range(m):
            ans += grid[i][-i - 1]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 8
        )


if __name__ == "__main__":
    unittest.main()
