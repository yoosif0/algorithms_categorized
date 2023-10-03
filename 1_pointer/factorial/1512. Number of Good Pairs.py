"""
https://leetcode.com/problems/number-of-good-pairs
The trick here is to know how to calculat combinations which is n * (n - 1) // 2
"""

import unittest


class Solution:
    def numIdenticalPairs(self, a: list[int]) -> int:
        ans = 0
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            n = freq[num]
            ans += n * (n - 1) // 2
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numIdenticalPairs([1, 1, 1, 1]), 6)
        self.assertEqual(t.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)


if __name__ == "__main__":
    unittest.main()
