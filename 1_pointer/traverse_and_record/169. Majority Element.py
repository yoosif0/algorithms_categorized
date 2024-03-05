"""
https://leetcode.com/problems/majority-element
"""

import unittest


class Solution:
    def majorityElement(self, a: list[int]) -> list[int]:
        m = {}
        ans = None
        cnt = 0
        for i in a:
            m[i] = m.get(i, 0) + 1
            if m[i] > cnt:
                ans = i
                cnt = m[i]
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.majorityElement([3, 2, 3]), 3)
        self.assertEqual(obj.majorityElement([1]), 1)


if __name__ == "__main__":
    unittest.main()
