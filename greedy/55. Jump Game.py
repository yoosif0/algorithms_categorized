"""
https://leetcode.com/problems/jump-game/
[3,2,1,0,4]

At the beginning, I thought that I need to be able to reach the index before but this example ruined it [2,0,0]
so here is a different approach
2,3,1,1,4,0,0,2,3,0,0,0,5,7,81,0,9
3: I can because max_force is 1
1: I can because max_force is 2
1: I can because max_force is 1
4: I can because max_force is 0
0: I can because max_force is 3
"""
import unittest


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_force = nums[0]
        for i in range(1, len(nums)):
            max_force = max_force - 1
            if max_force < 0:
                return False
            max_force = max(nums[i], max_force)
        return True


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.canJump([2, 3, 1, 1, 4]), True)
        self.assertEqual(t.canJump([3, 2, 1, 0, 4]), False)


if __name__ == "__main__":
    unittest.main()
