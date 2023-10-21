"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
#sorting_helps
#sorted_copy
"""
import unittest
import bisect


class Solution:
    def smallerNumbersThanCurrent(self, a: list[int]) -> list[int]:
        # make a sorted copy of a
        ac = a.copy()
        ac.sort()
        for i in range(len(a)):
            a[i] = bisect.bisect_left(ac, a[i])
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.smallerNumbersThanCurrent([8,1,2,2,3]), [4,0,1,1,3])


if __name__ == "__main__":
    unittest.main()