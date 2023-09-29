"""
https://leetcode.com/problems/find-the-duplicate-number/

3, 1, 3, 4, 2
            sf  
not_solved

0  1  2  3  4  5  6  7  8  9
2, 5, 9, 6, 9, 3, 8, 9, 7, 1
   f              s           

not_solved
"""


import unittest


class Solution:
    def findDuplicate(self, a: list[int]) -> int:
        s = 0
        f = 0
        while True:
            f = a[a[f]]
            s = a[s]
            if s == f:
                return a[s]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findDuplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(obj.findDuplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(
            obj.findDuplicate(
                [4, 4, 17, 15, 2, 1, 19, 11, 12, 13, 3, 18, 4, 4, 5, 9, 7, 14, 4, 16]
            ),
            4,
        )
        self.assertEqual(obj.findDuplicate([9, 4, 9, 5, 7, 2, 8, 9, 3, 9]), 9)
        self.assertEqual(obj.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]), 9)


if __name__ == "__main__":
    unittest.main()
