"""
https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/
#optimization

1 2 3 4 5
0 1    2    3     4      5 6 7 8 9
f 1    
not_solved
0/1 knapsack
"""
import sys
import unittest


class Solution:
    def lengthOfLongestSubsequence(self, cs: list[int], t: int) -> int:
        pass


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9), 3)
        self.assertEqual(t.lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7), 4)
        self.assertEqual(t.lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3), -1)


if __name__ == "__main__":
    unittest.main()
