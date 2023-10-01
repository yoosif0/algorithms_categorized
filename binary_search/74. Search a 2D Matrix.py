"""
https://leetcode.com/problems/search-a-2d-matrix/
3/col1 = 3/4 = 0r3
4/4 = 1r0 = [1][0]
5/4 = 1r2 
#matrix

"""

import unittest


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        def one_d_to_two_d_value(index: int):
            x, y = index // col_count, index % col_count
            return matrix[x][y]

        l = 0
        r = col_count * row_count
        while l < r:
            m = (r + l) // 2
            mid_num = one_d_to_two_d_value(m)
            if mid_num == target:
                return True
            elif mid_num < target:
                l = m + 1
            else:
                r = m
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(
        #     t.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True
        # )
        # self.assertEqual(
        #     t.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        #     False,
        # )
        self.assertEqual(
            t.searchMatrix([[1]], 1),
            True,
        )


if __name__ == "__main__":
    unittest.main()
