"""
https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i
#triplet
#subsequence
#prefix_suffix

8 6 1 5 3
1 5 3

  [5,4,8, 7, 10, 2]
[0,5,9,17,24,34,36]
5 8 7
5 7 2
4 8 7 
4 7 2
4 10 2
8 10 2
7 10 2
"""

import unittest


class Solution:
    def minimumSum(self, a: list[int]) -> int:
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.getDistances([2, 1, 3, 1, 2, 3, 3]), [4, 2, 7, 2, 4, 4, 5])


# 2:[0,4]

if __name__ == "__main__":
    unittest.main()
