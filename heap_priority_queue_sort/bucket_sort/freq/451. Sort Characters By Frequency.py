"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

import collections
import unittest


class Solution:
    def frequencySort(self, a: str) -> str:
        # ch counter
        m = collections.Counter(a)
        bs = [[] for _ in range(len(a))]
        for ch in m:
            bs[m[ch] - 1].append(ch)
        ans = []
        for i in range(len(bs) - 1, -1, -1):
            for ch in bs[i]:
                for _ in range(i + 1):
                    ans.append(ch)
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.frequencySort("tree"), "eetr")


if __name__ == "__main__":
    unittest.main()
