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
"""

import unittest


class Solution:
    def exist(self, grid: list[list[str]], word: str) -> bool:
        m = len(grid)
        n = len(grid[0])
        found = False

        def dfs(r: int, c: int, char_to_search: int):
            nonlocal found
            if (
                not 0 <= r < m
                or not 0 <= c < n
                or found
                or grid[r][c] != word[char_to_search]
            ):
                return
            if char_to_search == len(word) - 1:
                found = True
                return

            # mark that the character has been found on board (only for the dfs functions below)
            grid[r][c] = "#"
            dfs(r - 1, c, char_to_search + 1)
            dfs(r + 1, c, char_to_search + 1)
            dfs(r, c - 1, char_to_search + 1)
            dfs(r, c + 1, char_to_search + 1)
            # cleanup
            grid[r][c] = word[char_to_search]

        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == word[0]:
                    dfs(i, j, 0)

        return found


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
