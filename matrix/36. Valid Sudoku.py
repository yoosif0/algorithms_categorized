"""
https://leetcode.com/problems/valid-sudoku/
The trick in this question is that you can save keys in hash map in form of tuple
#matrix
"""


import unittest


class Solution:
    def isValidSudoku(self, grid: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        clmns = [set() for _ in range(9)]
        blcks = {}
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == ".":
                    continue
                # b is the key for each set in blcks
                b = (i // 3, j // 3)
                if b not in blcks:
                    blcks[b] = set()
                if n in rows[i] or n in clmns[j] or n in blcks[b]:
                    return False
                rows[i].add(n)
                clmns[j].add(n)
                blcks[b].add(n)
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.isValidSudoku(
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
            True,
        )
        self.assertEqual(
            obj.isValidSudoku(
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
