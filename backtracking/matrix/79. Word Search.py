"""
https://leetcode.com/problems/word-search/
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

             A
  S                    B
                     C  F
                    C E
                 F S E
                    D E


[["A", "B", "C", "E"]
["S", "F", "E", "S"]
["A", "D", "E", "E"]]
                
                "ABCESEEEFS"
#matrix
#cleanup_after_dfs
#decision
"""

import unittest


class Solution:
    def exist(self, grid: list[list[str]], s: str) -> bool:
        m = len(grid)
        n = len(grid[0])
        fl = False

        def dfs(r: int, c: int, ch: int):
            nonlocal fl
            if not 0 <= r < m or not 0 <= c < n or fl or grid[r][c] != s[ch]:
                return
            if ch == len(s) - 1:
                fl = True
                return

            # mark that the character has been fl on board (only for the dfs functions below)
            grid[r][c] = "#"
            dfs(r - 1, c, ch + 1)
            dfs(r + 1, c, ch + 1)
            dfs(r, c - 1, ch + 1)
            dfs(r, c + 1, ch + 1)
            # cleanup
            grid[r][c] = s[ch]

        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == s[0]:
                    dfs(i, j, 0)

        return fl


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.exist(
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
            ),
            True,
        )
        self.assertEqual(
            obj.exist(
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
            ),
            False,
        )
        self.assertEqual(
            obj.exist(
                [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
                "ABCESEEEFS",
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
