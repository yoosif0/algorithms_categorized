"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

import collections
import unittest


class Solution:
    def frequencySort(self, a: str) -> str:
        # ch counter
        cnt = collections.Counter(a)
        bs = [[] for _ in range(len(a))]
        for ch in cnt:
            bs[cnt[ch] - 1].append(ch)
        ans = []
        for i in range(len(bs) - 1, -1, -1):
            for ch in bs[i]:
                ans.extend([ch for _ in range(i+1)])
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.frequencySort("tree"), "eetr")


if __name__ == "__main__":
    unittest.main()
