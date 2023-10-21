"""
https://leetcode.com/problems/points-that-intersect-with-cars/
"""

import unittest


class Solution:
    def numberOfPoints(self, a: list[list[int]]) -> int:
        ans = 0
        s = set()
        for ia in a:
            for i in range(ia[0], ia[1] + 1):
                if i not in s:
                    ans += 1
                    s.add(i)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.numberOfPoints([[3, 6], [1, 5], [4, 7]]), 7)
        self.assertEqual(obj.numberOfPoints([[1, 3], [5, 8]]), 7)


if __name__ == "__main__":
    unittest.main()
