"""
https://leetcode.com/problems/sort-array-by-parity
[3,1,2,4]
[4,1,2,3]
   l r 
"""


import unittest


class Solution:
    def sortArrayByParity(self, a: list[int]) -> list[int]:
        l = 0
        r = len(a) - 1
        while l < r:
            if a[l] % 2 != 0:
                a[l], a[r] = a[r], a[l]
                r -= 1
            else:
                l += 1
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortArrayByParity([3, 1, 2, 4]), [4, 2, 1, 3])


if __name__ == "__main__":
    unittest.main()
