"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""

import unittest


class Solution:
    def intersection(self, a: list[int], a2: list[int]) -> list[int]:
        s = set(a)
        s2 = set(a2)
        ans = set()
        for n in s:
            if n in s2:
                ans.add(n)
        return list(ans)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.intersection([1, 2, 2, 1], [2, 2]), [2])


if __name__ == "__main__":
    unittest.main()
