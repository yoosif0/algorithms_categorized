"""
@nested-tags:greedy
https://leetcode.com/problems/find-the-highest-altitude/
"""

import unittest


class Solution:
    def largestAltitude(self, a: list[int]) -> int:
        cur = 0
        ans = 0
        for n in a:
            cur += n
            ans = max(cur, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.largestAltitude([-5, 1, 5, 0, -7]), 1)


if __name__ == "__main__":
    unittest.main()
