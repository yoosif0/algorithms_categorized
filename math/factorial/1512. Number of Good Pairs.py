"""
https://leetcode.com/problems/number-of-good-pairs
The trick here is to know how to calculat combinations which is n * (n - 1) // 2
"""

import unittest


class Solution:
    def numIdenticalPairs(self, a: list[int]) -> int:
        ans = 0
        m = {}
        for i in a:
            m[i] = m.get(i, 0) + 1
        for i in m:
            ans += m[i] * (m[i] - 1) // 2
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numIdenticalPairs([1, 1, 1, 1]), 6)
        self.assertEqual(t.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)


if __name__ == "__main__":
    unittest.main()
