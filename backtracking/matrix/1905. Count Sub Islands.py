"""
https://leetcode.com/problems/count-sub-islands/

The dfs function does 2 things. 
1. It mark cells as visited so that the for loop does not assume a cell
with 1 a new island althoug it belongs to a previously visited island.
2. Whenever a cell in an island is not in grid1, we mark it as so
"""
import unittest


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        g_len = len(grid2)
        r_len = len(grid2[0])
        cur = True
        ans = 0

        def dfs(r: int, c: int):
            nonlocal cur
            if not 0 <= r < g_len or not 0 <= c < r_len or grid2[r][c] != 1:
                return
            grid2[r][c] = "v"
            if grid1[r][c] != 1:
                cur = False
                # we do not return here because we want to visit all cells in this island

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i, row in enumerate(grid2):
            for j, c in enumerate(row):
                if c == 1:
                    cur = True
                    dfs(i, j)
                    if cur:
                        ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.countSubIslands(
                [
                    [1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 1, 1],
                ],
                [
                    [1, 1, 1, 0, 0],
                    [0, 0, 1, 1, 1],
                    [0, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                ],
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
