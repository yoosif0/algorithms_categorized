"""
https://leetcode.com/problems/game-of-life/
#tricky_o_1_space
#new_code

The trick for O(1) space is to have new codes that identify previous and new states
"""

import unittest


class Solution:
    def gameOfLife(self, grid: list[list[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        NEWLY_DEAD = 2
        NEWLY_ALIVE = 3

        for i in range(m):
            for j in range(n):
                neighbors = [
                    [i - 1, j],
                    [i + 1, j],
                    [i, j + 1],
                    [i, j - 1],
                    [i - 1, j - 1],
                    [i + 1, j + 1],
                    [i + 1, j - 1],
                    [i - 1, j + 1],
                ]
                live_count = 0
                for nb in neighbors:
                    if not 0 <= nb[0] < m or not 0 <= nb[1] < n:
                        continue
                    if grid[nb[0]][nb[1]] == 1 or grid[nb[0]][nb[1]] == NEWLY_DEAD:
                        live_count += 1
                if grid[i][j] == 1 or grid[i][j] == NEWLY_DEAD:
                    if live_count < 2:
                        # die due to underpopulation
                        grid[i][j] = NEWLY_DEAD
                    elif live_count > 3:
                        # die overpopulation
                        grid[i][j] = NEWLY_DEAD
                else:
                    if live_count == 3:
                        # wake up from die state
                        grid[i][j] = NEWLY_ALIVE
        # replace new code by required code
        for i in range(m):
            for j in range(n):
                if grid[i][j] == NEWLY_ALIVE:
                    grid[i][j] = 1
                elif grid[i][j] == NEWLY_DEAD:
                    grid[i][j] = 0
        return grid


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        res = t.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
        self.assertEqual(res, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
        res = t.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
        self.assertEqual(res, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])


if __name__ == "__main__":
    unittest.main()
