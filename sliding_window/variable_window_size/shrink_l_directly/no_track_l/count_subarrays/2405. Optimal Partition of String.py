"""
https://leetcode.com/problems/optimal-partition-of-string/
#set
"""

import unittest


class Solution:
    def partitionString(self, s: str) -> int:
        w = set()
        cnt = 1
        for r in range(len(s)):
            if s[r] in w:
                w.clear()
                cnt += 1
            w.add(s[r])
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.partitionString("abacaba"), 4)
        self.assertEqual(t.partitionString("ssssss"), 6)


if __name__ == "__main__":
    unittest.main()
