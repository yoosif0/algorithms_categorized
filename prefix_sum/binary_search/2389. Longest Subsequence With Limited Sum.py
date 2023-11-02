"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
#prefix_sum
#binary_search
#sorting_helps
"""
from itertools import accumulate
import unittest
import bisect


class Solution:
    def answerQueries(self, a: list[int], req: list[int]) -> list[int]:
        a.sort()
        a = list(accumulate(a))
        # binary search
        for i in range(len(req)):
            req[i] = bisect.bisect_right(a, req[i])
        return req


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.answerQueries([4, 5, 2, 1], [3, 10, 21]), [2, 3, 4])
        self.assertEqual(t.answerQueries([2, 3, 4, 5], [1]), [0])


if __name__ == "__main__":
    unittest.main()