"""
https://leetcode.com/problems/count-complete-subarrays-in-an-array/
[1,3,1,2,2]
once it reaches the required length, any other extra value coming next can give us an addtional subarray.

1,3,1,2,2,5,7,8,1,2,3,7,1,1,2,7,8
1,3,1,2,2,5,7,8: ans=1 can't reduce l 10
1,3,1,2,2,5,7,8,1: reduce l till as long we're good needed 3,1,2,2,5,7,8,1 ans=11 + len-r = 20
3,1,2,2,5,7,8,1,2: try to reduce l but can't. 
3,1,2,2,5,7,8,1,2,3: try to reduce l. can. ans=30. 1,2,2,5,7,8,1,2,3. I can reduce again to 2,2,5,7,8,1,2,3 ans =38 
I can reduce again to 2,5,7,8,1,2,3 ans = 48
#extend_r_in_w
#extend_r_then_shrink_l
#set
"""

import unittest


class Solution:
    def countCompleteSubarrays(self, a: list[int]) -> int:
        s = set({})
        for n in a:
            s.add(n)
        k = len(s)
        cnt = 0
        w = {}
        l = 0
        r = 0
        # extend r till you reach required len then break
        while True:
            if r == len(a):
                break
            w[a[r]] = w.get(a[r], 0) + 1
            if len(w) == k:
                cnt += len(a) - r
                break
            else:
                r += 1

        # shrink l
        while True:
            if l > r or l == len(a):
                break
            if w[a[l]] >= 2:
                w[a[l]] -= 1
                l += 1
                cnt += len(a) - r
            else:
                # extend r
                r += 1
                if r == len(a):
                    break
                w[a[r]] = w.get(a[r], 0) + 1
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
