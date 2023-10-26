"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
#matrix
"""

import unittest


class Solution:
    def kWeakestRows(self, grid: list[list[int]], k: int) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        # buckets
        bs = [[] for _ in range(n + 1)]
        for i in range(m):
            bs[sum(grid[i])].append(i)
        ans = []
        for bc in bs:
            for i in bc:
                ans.append(i)
        return ans[:k]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.kWeakestRows(
                [
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                ],
                3,
            ),
            [2, 0, 3],
        )


if __name__ == "__main__":
    unittest.main()
