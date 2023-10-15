"""
https://leetcode.com/problems/maximum-width-ramp/
 0 1 2 3 4 5 6 7 9 0101112 1314151617 18192021 
[9,8,1,0,1,9,4,0,4,1,2,3,9,2,1,3,8,10,11,3,4,5]
left to right[0,1,2,3]

"""

import unittest


class Solution:
    def maxWidthRamp(self, a: list[int]) -> int:
        st = [0]
        for i in range(len(a)):
            if a[i] < a[st[-1]]:
                st.append(i)
        ans = 0
        for i in range(len(a) - 1, -1, -1):
            while st and a[i] >= a[st[-1]]:
                ans = max(ans, i - st.pop())
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.maxWidthRamp([6, 0, 8, 2, 1, 5]), 4)
        self.assertEqual(obj.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]), 7)


if __name__ == "__main__":
    unittest.main()
