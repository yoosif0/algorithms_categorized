"""
@nested-tags:greedy,knapsack/unbounded
I can use greedy here because i can always fallback that there is a "1" coin change unlike the question here https://leetcode.com/problems/coin-change/
In the later, sometimes, I am able to full bigger coins but end up not able to continue since I don't have a coin of "1"
"""

import unittest


class Solution:
    def pickBest(self, n):
        a = [10, 5, 1]
        ans = []
        for n2 in a:
            if n >= n2:
                ans.extend(n // n2 * [n2])
                n = n % n2
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pickBest(27), [10, 10, 5, 1, 1])


if __name__ == "__main__":
    unittest.main()
