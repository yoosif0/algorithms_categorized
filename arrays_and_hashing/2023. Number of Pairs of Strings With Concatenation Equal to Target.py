"""
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target
777 7 77 77
#prefix_suffix_str

O(n2) time since substring take O(n) time
"""

from collections import Counter
import unittest


class Solution:
    def numOfPairs(self, a: list[str], t: str) -> int:
        m = Counter(a)
        ans = 0
        for i in range(len(a)):
            if a[i] == t[: len(a[i])]:
                suf = t[len(a[i]) :]
                ans += m[suf]
                # that's a special i can't equal j (prefix can't be the same as suffix)
                if suf == a[i]:
                    ans -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numOfPairs(["777", "7", "77", "77"], "7777"), 4)
        self.assertEqual(t.numOfPairs(["1", "1", "1"], "11"), 6)


if __name__ == "__main__":
    unittest.main()
