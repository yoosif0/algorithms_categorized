"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

import collections
import unittest


class Solution:
    def intersect(self, a: list[int], a2: list[int]) -> list[int]:
        m = collections.Counter(a)
        m2 = collections.Counter(a2)
        ans = []
        for n in m:
            if n in m2:
                for _ in range(min(m[n], m2[n])):
                    ans.append(n)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.intersection([1, 2, 2, 1], [2, 2]), [2, 2])


if __name__ == "__main__":
    unittest.main()
