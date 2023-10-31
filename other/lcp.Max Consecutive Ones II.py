"""
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.

    
0011011101001011011100011101001
6
"""
import unittest


class Solution:
    def findMaxConsecutiveOnes(self, a: list[int]) -> int:
        cnt = 0
        ans = cnt
        for i in a:
            if i == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
