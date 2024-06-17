"""
@nested-tags:greedy/ptn
https://leetcode.com/problems/jump-game-ii/

[2,3,1,1,4,0,2,3,0,0,1,5]
0:2r2 j++ je:2
1:3r4(i+1) 
2:1 j++ je:4
3:1
4:4r8 j++ je:8
5:0
6:2 if 2+i > r, update reach and increase jump
7:3r10
8:0r10 je:10 j++
9:0r
10:1r11 je:11 j++

The greedy strategy lies in that when i < last_jump_index, there is no need to jump, since you must find a better point to jump from forward
When you increase jumps, it does not mean that you just jumped from here. You don't need to know whether you're going to
jump from this node or not

#improve_on_dp
"""

import unittest

# # dp but slow
# class Solution:
#     def jump(self, a: list[int]) -> int:
#         dp = [sys.maxsize for _ in range(len(a))]
#         dp[0] = 0
#         for i, num in enumerate(a):
#             # Do not jump till after len(nums)
#             for j in range(i + 1, min(len(a), i + num + 1)):
#                 dp[j] = min(dp[j], dp[i] + 1)
#         return dp[-1]


class Solution:
    def jump(self, a: list[int]) -> int:
        if len(a) <= 1:
            return 0
        ans = 1
        cur = a[0]
        for i in range(1, len(a) - 1):
            cur = max(i + a[i], cur)
            if i == a[0]:
                ans += 1
                a[0] = cur
            if a[0] >= len(a) - 1:
                break
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.jump([2, 3, 1, 1, 4, 0, 2, 3, 0, 0, 1, 5]), 5)
        self.assertEqual(t.jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(t.jump([0]), 0)


if __name__ == "__main__":
    unittest.main()
