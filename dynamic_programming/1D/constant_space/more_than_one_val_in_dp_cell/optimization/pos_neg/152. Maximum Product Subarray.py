import unittest

"""
https://leetcode.com/problems/maximum-product-subarray
[2,3,-2,4]
2:2
3:6
-2:-12,6
4:-48,24

[[2,2],[6,6],[-12,6],[-12,24]]
#optimization
#more_than_one_val_in_dp_cell
"""


class Solution:
    def maxProduct(self, a: list[int]) -> int:
        neg = pos = ans = a[0]
        for i in range(1, len(a)):
            num = a[i]
            neg, pos = min(pos * num, neg * num, num), max(pos * num, neg * num, num)
            ans = max(pos, ans, neg)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxProduct([2, 3, -2, 4]), 6)
        self.assertEqual(t.maxProduct([2, 3, -2, 4, -5]), 240)
        self.assertEqual(t.maxProduct([-2, 0, -1]), 0)
        self.assertEqual(t.maxProduct([2, -5, -2, -4, 3]), 24)


if __name__ == "__main__":
    unittest.main()
