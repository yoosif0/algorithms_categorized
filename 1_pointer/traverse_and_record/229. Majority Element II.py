"""
https://leetcode.com/problems/majority-element-ii
"""

from collections import Counter
import unittest


class Solution:
    def majorityElement(self, a: list[int]) -> list[int]:
        m = Counter(a)
        return list(filter(lambda x: m[x] > len(a) / 3, m))


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.majorityElement([3, 2, 3]), [3])
        self.assertEqual(obj.majorityElement([1]), [1])
        self.assertEqual(obj.majorityElement([1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()
