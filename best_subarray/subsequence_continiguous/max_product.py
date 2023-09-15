import unittest

"""
[2,3,-2,4]
    meh:2  min:2   msf:2
3:  meh:6  min:6   msf:6
-2: meh:-2 min:-12 msf:6
4:  meh:4  min:-48 msf:6

[2,3,-2,4,-5]
   meh:2   min:2   msf:2
3: meh:6   min:3   msf:6
-2:meh:-2  min:-12 msf:6    min = prev_meh * num
4: meh:4   min:-48 msf:6    min = prev_min * num
-5:meh:-5  min:240 msf:240  min = prev_min * num

[-2,0,-1]
    meh:-2, min:-2, msf:-2
0:  meh:0,  min:0,  msf:0   min = (prev_min or prev_meh) * num
-1: meh:0,  min:0,  msf:0


[2,-5,-2,-4,3]
   meh:2,  min:2,   msf:2
-5:meh:-5, min:-10, msf:2
-2:meh:20, min:-2,  msf:20    meh=prev_min * num    min=num 
-4:meh:8,  min:-80, msf:20    meh=prev_min * num    min=prev_meh*num
3 :meh:24, min:-240,msf:22    meh=prev_meh * num    min=prev_min*num

"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        neg = pos = global_max = nums[0]
        for _, num in enumerate(nums[1:]):
            neg, pos = min(pos * num, neg * num, num), max(pos * num, neg * num, num)
            global_max = max(pos, global_max, neg)
        return global_max


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxProduct([2, 3, -2, 4]), 6)
        self.assertEqual(t.maxProduct([2, 3, -2, 4, -5]), 240)
        self.assertEqual(t.maxProduct([-2, 0, -1]), 0)
        self.assertEqual(t.maxProduct([2, -5, -2, -4, 3]), 24)


if __name__ == "__main__":
    unittest.main()
