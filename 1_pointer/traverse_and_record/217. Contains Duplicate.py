"""
https://leetcode.com/problems/contains-duplicate/
"""

import unittest


class Solution:
    def containsDuplicate(self, a: list[int]) -> bool:
        m = {}
        for i in a:
            m[i] = m.get(i, 0) + 1
            if m[i] > 1:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
