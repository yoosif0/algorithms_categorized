"""
#counter
https://leetcode.com/problems/sort-colors/
"""

import collections
import unittest


class Solution:
    def sortColors(self, a: list[int]) -> None:
        cnt = collections.Counter(a)
        j = 0
        for i in range(0, 3):
            for _ in range(cnt[i]):
                a[j] = i
                j += 1

class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        a = [2, 0, 2, 1, 1, 0]
        t.sortColors(a)
        self.assertEqual(a, [0, 0, 1, 1, 2, 2])


if __name__ == "__main__":
    unittest.main()
