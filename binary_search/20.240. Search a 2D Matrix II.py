"""
@nested-tags:binary_search/remove_from_both,binary_search/matrix
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

import unittest


class Solution:
    def searchMatrix(self, g: list[list[int]], t: int) -> bool:
        m = len(g)
        n = len(g[0])
        for i in range(m):
            l = 0
            r = n - 1
            while l <= r:
                mid = (r + l) // 2
                mv = g[i][mid % n]
                if mv < t:
                    l = mid + 1
                elif mv > t:
                    r = mid - 1
                else:
                    return True
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.searchMatrix(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                5,
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
