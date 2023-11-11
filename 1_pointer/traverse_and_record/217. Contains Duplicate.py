"""
https://leetcode.com/problems/contains-duplicate/
"""

import unittest


class Solution:
    def containsDuplicate(self, a: list[int]) -> bool:
        m = {}
        for k in a:
            m[k] = m.get(k, 0) + 1
            if m[k] > 1:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
