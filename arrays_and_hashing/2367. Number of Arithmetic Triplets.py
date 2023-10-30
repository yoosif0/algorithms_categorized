"""
https://leetcode.com/problems/number-of-arithmetic-triplets
#triplets
because of a fixed "x", you don't need 3 pointers, unilike other triplet questions like 3sum. You can just check if 2 other values are in the set
"""


import unittest


class Solution:
    def arithmeticTriplets(self, a: list[int], x: int) -> int:
        s = set(a)
        ans = 0
        for i in a:
            if i + x in s and i + 2 * x in s:
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3), 2)


if __name__ == "__main__":
    unittest.main()
