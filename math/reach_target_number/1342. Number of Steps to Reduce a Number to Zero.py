"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
#greedy
#reach_target_number
"""
import unittest


class Solution:
    def numberOfSteps(self, n: int) -> int:
        ans = 0
        while n:
            if n % 2 == 0:
                n /= 2
            else:
                n -= 1
            ans += 1
        return ans


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.numberOfSteps(14), 6)


if __name__ == "__main__":
    unittest.main()
