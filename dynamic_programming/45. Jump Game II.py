"""
https://leetcode.com/problems/jump-game-ii/
[2,3,1,1,4,0,2,3,0,0,1,5]
[.,1,1,2,2,3,3,3,3,4,4]
send 1,2
1: reached by 1: send 2,3,4
2:1reached by 1: send 3
3:1reached by 2: send 4
4:4reached by 2: send 5,6,7,8 (3)
5:0reached by 3
6:2reached by 3: send 7,8 (4)
7:3reached by 3: send 8,9,10 (4)
8:0reached by 3: 
9:0
10:1reachedby4: send 11 (5)
also in #greedy
"""
import unittest
import sys


class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [sys.maxsize for _ in range(len(nums))]
        dp[0] = 0
        for i, num in enumerate(nums):
            # Do not jump till after len(nums)
            for j in range(i + 1, min(len(nums), i + num + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.jump([2, 3, 1, 1, 4, 0, 2, 3, 0, 0, 1, 5]), 5)
        self.assertEqual(t.jump([2, 3, 1, 1, 4]), 2)


if __name__ == "__main__":
    unittest.main()
