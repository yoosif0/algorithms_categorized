"""
@nested-tags:binary_search/no_arr,binary_search/remove_from_l
https://leetcode.com/problems/first-bad-version/
"""

import unittest

bad = None


def isBadVersion(n: int):
    return n >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
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
