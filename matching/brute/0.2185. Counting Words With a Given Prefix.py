"""
@nested-tags:matching/brute_force
https://leetcode.com/problems/counting-words-with-a-given-prefix
"""

import unittest


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word[: len(pref)] == pref:
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.prefixCount(["pay", "attention", "practice", "attend"], "at"), 2
        )


if __name__ == "__main__":
    unittest.main()
