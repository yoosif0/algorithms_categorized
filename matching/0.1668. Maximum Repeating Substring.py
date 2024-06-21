"""
@nested-tags:matching/brute_force
https://leetcode.com/problems/maximum-repeating-substring

it's ok to brute force here since the input is small
"""

import unittest


class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        ans = 0
        for i in range(len(s) - len(word) + 1):
            j = i
            cur = 0
            while s[j : j + len(word)] == word:
                j += len(word)
                cur += 1
            ans = max(cur, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxRepeating("ababc", "ab"), 2)
        self.assertEqual(t.maxRepeating("ababc", "ac"), 0)
        self.assertEqual(t.maxRepeating("a", "a"), 1)


if __name__ == "__main__":
    unittest.main()
