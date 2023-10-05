"""
https://leetcode.com/problems/house-robber/

[2,7,9,3,1,20,5,22,60]
2: incl:2 excl:0
7: incl:7 excl:2
9: incl:11 excl:7    incl = num + prev_excl; excl = prev_incl
3: incl:10 excl:11   incl = num + prev_excl; excl = prev_incl
1: incl:12 excl:11   incl = num + prev_excl; excl = max(prev_incl, prev_excl)
20:incl:31 excl:12 
5: incl:17 excl:31
22:incl:53 excl:31
60:incl:91 excl:53
#optimization
"""

import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        incl, excl = 0, 0
        for _, num in enumerate(nums):
            incl, excl = num + excl, max(incl, excl)
        return max(excl, incl)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rob([2, 7, 9, 3, 1, 20, 5, 22, 60]), 91)


if __name__ == "__main__":
    unittest.main()
