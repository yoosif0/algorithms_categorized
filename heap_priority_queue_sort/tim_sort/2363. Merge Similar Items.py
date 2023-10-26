"""
https://leetcode.com/problems/merge-similar-items
q:why not merge sort
a:because the 2 lists are not sorted
"""

import collections
import unittest


class Solution:
    def mergeSimilarItems(
        self, a: list[list[int]], a2: list[list[int]]
    ) -> list[list[int]]:
        m = collections.Counter()
        for [v, w] in a:
            m[v] += w
        for [v, w] in a2:
            m[v] += w
        ans = [[k, m[k]] for k in m]
        ans.sort(key=lambda x: x[0])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]),
            [[1, 6], [3, 9], [4, 5]],
        )


if __name__ == "__main__":
    unittest.main()
