"""
https://leetcode.com/problems/reorganize-string
aaabbbccdd
abababcdcd

aaaaaaabbbccdd
abababacad
"""

import collections
import heapq
import unittest


class Solution:
    def reorganizeString(self, s: str) -> str:
        m = collections.Counter(s)
        h = [(-m[ch], ch) for ch in m]
        heapq.heapify(h)
        ans = []
        while h:
            ppd = heapq.heappop(h)
            if h and ans and ans[-1] == ppd[1]:
                ppd, _ = heapq.heappop(h), heapq.heappush(h, ppd)
            ans.append(ppd[1])
            if ppd[0] != -1:
                heapq.heappush(h, (ppd[0] + 1, ppd[1]))
        for i in range(1, len(ans)):
            if ans[i] == ans[i - 1]:
                return ""
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reorganizeString("aab"), "aba")


if __name__ == "__main__":
    unittest.main()
