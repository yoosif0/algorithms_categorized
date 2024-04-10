"""
https://www.lintcode.com/problem/883/
ans = 0
0     0      1    1       0     111      0 1001011011100011101001
(1,t) (1,t) (2,t) (3,t)  (1,t)    4t    1t
"""

import unittest


class Solution:
    def find_max_consecutive_ones(self, a):
        cur = (0, False)
        bst = 0
        for i in range(len(a)):
            if a[i] == 1:
                cur = (cur[0] + 1, cur[1])
                bst = max(cur[0], bst)
            elif a[i] == 0 and cur[1] == False:
                cur = (cur[0] + 1, True)
                bst = max(cur[0], bst)
            else:
                cur = (1, True)
        return bst


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.find_max_consecutive_ones([1, 0, 1, 1, 0]), 4)
        self.assertEqual(obj.find_max_consecutive_ones([1, 0, 1, 0, 1]), 3)


if __name__ == "__main__":
    unittest.main()
