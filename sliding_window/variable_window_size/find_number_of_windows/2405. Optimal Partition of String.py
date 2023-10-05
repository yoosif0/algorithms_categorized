"""
https://leetcode.com/problems/optimal-partition-of-string/
#set
"""

import unittest


class Solution:
    def partitionString(self, s: str) -> int:
        w = {s[0]}
        ans = 1
        r = 0
        while True:
            r += 1
            if r == len(s):
                break
            if s[r] in w:
                w.clear()
                ans += 1
            w.add(s[r])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.partitionString("abacaba"), 4)
        self.assertEqual(t.partitionString("ssssss"), 6)


if __name__ == "__main__":
    unittest.main()
