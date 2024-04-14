"""
https://leetcode.com/problems/count-complete-subarrays-in-an-array/
[1,3,1,2,2]
once it reaches the required length, any other extra value coming next can give us an addtional subarray.

1,3,1,2,2,5,7,8,1,2,3,7,1,1,2,7,8
1,3,1,2,2,5,7,8: cnt=1 can't reduce l 10
1,3,1,2,2,5,7,8,1: reduce l till as long we're good needed 3,1,2,2,5,7,8,1 cnt=11 + len-r = 20
3,1,2,2,5,7,8,1,2: try to reduce l but can't. 
3,1,2,2,5,7,8,1,2,3: try to reduce l. can. cnt=30. 1,2,2,5,7,8,1,2,3. I can reduce again to 2,2,5,7,8,1,2,3 cnt =38 
I can reduce again to 2,5,7,8,1,2,3 cnt = 48
#extend_r_in_w
#extend_r_then_shrink_l
#set
"""

import unittest


class Solution:
    def countCompleteSubarrays(self, a: list[int]) -> int:
        k = len(set(a))
        cnt = 0
        l = 0
        m = {}
        for r in range(len(a)):
            if a[r] not in m:
                m[a[r]] = 0
            m[a[r]] += 1
            while len(m) == k:
                cnt += len(a) - r
                m[a[l]] -= 1
                if m[a[l]] == 0:
                    del m[a[l]]
                l += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countCompleteSubarrays([1, 3, 1, 2, 2]), 4)
        self.assertEqual(t.countCompleteSubarrays([5, 5, 5, 5]), 10)
        self.assertEqual(
            t.countCompleteSubarrays(
                [1, 3, 1, 2, 2, 5, 7, 8, 1, 2, 3, 7, 1, 1, 2, 7, 8]
            ),
            48,
        )


if __name__ == "__main__":
    unittest.main()
