"""
https://leetcode.com/problems/find-all-groups-of-farmland/
traverse each island in for loop. while traversing, pass by coordinates
"""
import unittest


class Solution:
    def findFarmland(self, grid: list[list[int]]) -> list[list[int]]:
        g_len = len(grid)
        r_len = len(grid[0])
        cur: list[int] = []
        ans: list[list[int]] = []

        def dfs(r: int, c: int):
            if not 0 <= r < g_len or not 0 <= c < r_len or grid[r][c] != 1:
                return

            grid[r][c] = "visited"
            cur[0] = min(cur[0], r)
            cur[1] = min(cur[1], c)
            cur[2] = max(cur[2], r)
            cur[3] = max(cur[3], c)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1:
                    cur = [i, j, i, j]
                    dfs(i, j)
                    ans.append(cur)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]),
            [[0, 0, 0, 0], [1, 1, 2, 2]],
        )


if __name__ == "__main__":
    unittest.main()
