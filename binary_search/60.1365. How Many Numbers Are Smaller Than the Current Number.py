"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
#first_occurrence
"""

import unittest


class Solution:
    def smallerNumbersThanCurrent(self, a: list[int]) -> list[int]:
        # make a sorted copy of a
        ac = a.copy()
        ac.sort()
        for i in range(len(a)):
            l = 0
            r = len(ac) - 1
            t = a[i]
            # find index of first occurence
            while l < r:
                m = (l + r) // 2
                if ac[m] < t:
                    l = m + 1
                elif ac[m] > t:
                    r = m - 1
                else:
                    r -= 1
            a[i] = l
        return a


"""
1 2 2 3 8
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.smallerNumbersThanCurrent([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])


if __name__ == "__main__":
    unittest.main()
