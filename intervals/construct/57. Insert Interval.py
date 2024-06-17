"""
@nested-tags:intervals/construct
https://leetcode.com/problems/insert-interval/
[[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

import unittest


class Solution:
    def insert(self, a: list[list[int]], n: list[int]) -> list[list[int]]:
        if not a:
            return [n]

        ans = []
        # fill initial portion of ans (before new interval)
        i = 0
        while i < len(a) and a[i][1] < n[0]:
            ans.append(a[i])
            i += 1

        # fill problematic portion
        start = min(a[i][0], n[0]) if len(a) > i else n[0]
        end = n[1]
        while i < len(a) and a[i][0] <= end:
            end = max(a[i][1], n[1])
            i += 1
        ans.append([start, end])

        # fill rest of unproblematic array
        for i in range(i, len(a)):
            ans.append(a[i])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.insert([[6, 9], [12, 15]], [10, 11]),
            [[6, 9], [10, 11], [12, 15]],
        )
        self.assertEqual(t.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(
            t.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )
        self.assertEqual(t.insert([], [2, 5]), [[2, 5]])
        self.assertEqual(t.insert([[1, 5]], [6, 8]), [[1, 5], [6, 8]])


if __name__ == "__main__":
    unittest.main()
