"""
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered
"""

import unittest


class Solution:
    def isCovered(self, a: list[list[int]], l: int, r: int) -> bool:
        aa = [False for _ in range(50)]
        for ia in a:
            for i in range(ia[0], ia[1] + 1):
                aa[i - 1] = True
        # check that all numbers from l to r are truthy
        for i in range(l, r + 1):
            if i > len(aa) or aa[i - 1] == False:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5), True)
        self.assertEqual(obj.isCovered([[1, 10], [10, 20]], 21, 21), False)
        self.assertEqual(obj.isCovered([[37, 49], [5, 17], [8, 32]], 29, 49), False)


if __name__ == "__main__":
    unittest.main()
