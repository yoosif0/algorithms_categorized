"""
https://leetcode.com/problems/first-bad-version/
#bisect_left
"""

import unittest

bad = None


def target(n: int):
    return n >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if not target(m):
                l = m + 1
            else:
                r = m
        return l


class Test(unittest.TestCase):
    def test(self):
        global bad
        t = Solution()
        bad = 4
        self.assertEqual(t.firstBadVersion(5), 4)
        bad = 1
        self.assertEqual(t.firstBadVersion(1), 1)
        bad = 1
        self.assertEqual(t.firstBadVersion(2), 1)


if __name__ == "__main__":
    unittest.main()
