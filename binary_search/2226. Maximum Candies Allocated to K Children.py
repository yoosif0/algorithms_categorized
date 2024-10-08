"""
@nested-tags:binary_search/no_arr/consumption,binary_search/remove_from_r
https://leetcode.com/problems/maximum-candies-allocated-to-k-children
[5,8,6,7,6,7,20] 30
59 / 30
5 5 5 5 5 5 5 5 5 5 5 5

mid = (left + right) / 2 and l=mid+1 to find first element valid
mid = (left + right + 1) / 2 r=mid-1 to find last element valid
"""

import unittest


class Solution:
    def maximumCandies(self, a: list[int], k: int) -> int:
        l = 0
        r = sum(a) // k
        while l < r:
            mid = (r + l + 1) // 2
            if sum(n // mid for n in a) < k:
                r = mid - 1
            else:
                l = mid
        return r


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumCandies([5, 8, 6], 3), 5)
        self.assertEqual(t.maximumCandies([2, 5], 11), 0)
        self.assertEqual(t.maximumCandies([5, 8, 6, 7, 6, 7, 20], 30), 1)
        self.assertEqual(t.maximumCandies([4, 7, 5], 4), 3)
        self.assertEqual(t.maximumCandies([1, 2, 3, 4, 10], 5), 3)


if __name__ == "__main__":
    unittest.main()
