"""
@nested-tags:binary_search/remove_from_l,binary_search/store_index,store_index
https://leetcode.com/problems/find-right-interval
"""

import unittest


class Solution:
    def findRightInterval(self, a: list[list[int]]) -> list[int]:
        m = {}
        for i in range(len(a)):
            m[a[i][0]] = i
        # make a sorted copy of a
        ac = sorted(a, key=lambda x: x[0])
        for i in range(len(a)):
            l = 0
            r = len(ac)
            # find smallest start that is equal or greater to a[i][1]
            while l < r:
                mid = (l + r) // 2
                if ac[mid][0] < a[i][1]:
                    l = mid + 1
                else:
                    r = mid
            a[i] = -1 if l == len(a) else m[ac[l][0]]
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findRightInterval([[1, 2]]), [-1])
        self.assertEqual(t.findRightInterval([[3, 4], [2, 3], [1, 2]]), [-1, 0, 1])
        self.assertEqual(t.findRightInterval([[1, 4], [2, 3], [3, 4]]), [-1, 2, -1])
        self.assertEqual(t.findRightInterval([[1, 1], [3, 4]]), [0, -1])


"""
1,2  2,3  3,4
"""

if __name__ == "__main__":
    unittest.main()
