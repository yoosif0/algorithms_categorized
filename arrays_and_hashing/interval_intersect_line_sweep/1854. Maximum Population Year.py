"""
https://leetcode.com/problems/maximum-population-year
"""

import unittest


class Solution:
    def maximumPopulation(self, a: list[list[int]]) -> int:
        aa = [0 for _ in range(100)]
        for ia in a:
            for i in range(ia[0], ia[1]):
                aa[i - 1950] += 1
        ans = (0, 0)
        for i in range(len(aa)):
            if aa[i] > ans[1]:
                ans = (i, aa[i])
        return ans[0] + 1950


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.maximumPopulation([[1993, 1999], [2000, 2010]]), 1993)
        self.assertEqual(
            obj.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]), 1960
        )
        self.assertEqual(
            obj.maximumPopulation(
                [
                    [2033, 2034],
                    [2039, 2047],
                    [1998, 2042],
                    [2047, 2048],
                    [2025, 2029],
                    [2005, 2044],
                    [1990, 1992],
                    [1952, 1956],
                    [1984, 2014],
                ]
            ),
            2005,
        )


if __name__ == "__main__":
    unittest.main()
