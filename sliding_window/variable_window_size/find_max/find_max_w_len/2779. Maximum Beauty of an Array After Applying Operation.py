"""
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation
[4,6,1,2], k = 2
[1,2,4,6], k = 2
   l   r    
w=[-1,3] ans=2
w=[0,4] ans=3
#sorting_helps
#intervals
#no_need_valid_w
#find_max_w_len
"""

import unittest


class Solution:
    def maximumBeauty(self, a: list[int], k: int) -> int:
        a.sort()
        ans = 1
        l = 0
        for r in range(1, len(a)):
            if a[r] - a[l] > 2 * k:
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumBeauty([4, 6, 1, 2], 2), 3)
        self.assertEqual(t.maximumBeauty([1, 1, 1, 1], 10), 4)


if __name__ == "__main__":
    unittest.main()
