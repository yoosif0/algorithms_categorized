"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
#matrix
"""

import collections
import itertools
import unittest


class Solution:
    def kWeakestRows(self, grid: list[list[int]], k: int) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        # buckets: key is the frequency from 0 to n
        bs = [[] for _ in range(n + 1)]
        for i in range(m):
            bs[sum(grid[i])].append(i)
        return list(itertools.chain.from_iterable(bs))[:k]


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
