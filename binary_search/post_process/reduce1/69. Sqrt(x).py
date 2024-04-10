"""
https://leetcode.com/problems/sqrtx/description/
#bisect_post_process
#bisect_left
#bisect_post_process
here we reduce 1 from the answer
"""

import unittest


# like bisect left
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        r = x
        l = 1
        while l < r:
            mid = (l + r) // 2
            m = mid * mid
            if m < x:
                l = mid + 1
            else:
                r = mid
        return l if l**2 == x else l - 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.mySqrt(8), 2)
        self.assertEqual(t.mySqrt(4), 2)


if __name__ == "__main__":
    unittest.main()
