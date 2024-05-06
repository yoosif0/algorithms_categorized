"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
#prefix_sum
#binary_search
#sorting_helps
"""

from itertools import accumulate
import unittest


class Solution:
    def answerQueries(self, a: list[int], req: list[int]) -> list[int]:
        a.sort()
        a = list(accumulate(a, initial=0))
        # binary search
        for i in range(len(req)):
            t = req[i]
            l = 0
            r = len(a) - 1
            while l < r:
                m = (l + r + 1) // 2
                if a[m] > t:
                    r = m - 1
                elif a[m] < t:
                    l = m
                else:
                    l = m
                    break
            req[i] = l
        return req


"""
0 1 3 7 12
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.answerQueries([4, 5, 2, 1], [3, 10, 21]), [2, 3, 4])
        self.assertEqual(t.answerQueries([2, 3, 4, 5], [1]), [0])


if __name__ == "__main__":
    unittest.main()
