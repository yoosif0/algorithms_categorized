"""
https://leetcode.com/problems/max-consecutive-ones/
#cur_bst
"""
import unittest


class Solution:
    def findMaxConsecutiveOnes(self, a: list[int]) -> int:
        cur = 0
        bst = cur
        for i in a:
            if i == 1:
                cur += 1
                bst = max(bst, cur)
            else:
                cur = 0
        return bst


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
