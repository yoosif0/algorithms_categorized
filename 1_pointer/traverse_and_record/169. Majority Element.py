"""
https://leetcode.com/problems/majority-element
"""

import unittest


class Solution:
    def majorityElement(self, a: list[int]) -> list[int]:
        m = {}
        ans_el = None
        ans_cnt = 0
        for i in a:
            m[i] = m.get(i, 0) + 1
            if m[i] > ans_cnt:
                ans_el = i
                ans_cnt = m[i]
        return ans_el


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.majorityElement([3, 2, 3]), 3)
        self.assertEqual(obj.majorityElement([1]), 1)


if __name__ == "__main__":
    unittest.main()
