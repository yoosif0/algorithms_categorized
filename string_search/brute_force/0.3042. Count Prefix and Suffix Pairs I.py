"""
@nested-tags:string/easy/brute_force,string_prefix_search
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
"""

import unittest


class Solution:
    def countPrefixSuffixPairs(self, a: list[str]) -> int:
        ans = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if len(a[i]) > len(a[j]):
                    continue
                if a[j][: len(a[i])] == a[i] and a[j][len(a[j]) - len(a[i]) :] == a[i]:
                    ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]), 4)
        self.assertEqual(t.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]), 2)
        self.assertEqual(t.countPrefixSuffixPairs(["abab", "ab"]), 0)


if __name__ == "__main__":
    unittest.main()
