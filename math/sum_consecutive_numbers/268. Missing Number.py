"""
https://leetcode.com/problems/missing-number/
the math trick here is to know how to compute sum of consecutive numbers
"""

import unittest


# O(1) space
# class Solution:
#     def missingNumber(self, a: list[int]) -> int:
#         i = 0
#         ans = len(a)
#         while i < len(a):
#             if a[i] == len(a):
#                 ans = i
#                 i += 1
#             elif a[i] == i:
#                 i += 1
#             else:
#                 a[a[i]], a[i] = a[i], a[a[i]]
#         return ans


class Solution:
    def missingNumber(self, a: list[int]) -> int:
        should = len(a) * (len(a) + 1) / 2
        return int(should - sum(a))


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.missingNumber([3, 0, 1]), 2)
        self.assertEqual(obj.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
        self.assertEqual(obj.missingNumber([0, 1]), 2)
        self.assertEqual(obj.missingNumber([1, 2]), 0)


if __name__ == "__main__":
    unittest.main()
