"""
https://leetcode.com/problems/product-of-array-except-self/

Each num in nums should have a before product and after product saved in an array or hash map and the result
is before * after
"""


import unittest


class Solution:
    def productExceptSelf(self, a: list[int]) -> list[int]:
        # fill before product
        l = []
        cur = 1
        for i in a:
            l.append(cur)
            cur *= i

        # fill after product
        r = [1 for _ in range(len(a))]
        cur = 1
        for i in range(len(a) - 1, -1, -1):
            r[i] = cur
            cur *= a[i]

        # fill ans
        ans = []
        for i in range(len(a)):
            ans.append(l[i] * r[i])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == "__main__":
    unittest.main()
