"""
https://leetcode.com/problems/max-chunks-to-make-sorted/
"""
import sys
import unittest


class Solution:
    def maxChunksToSorted(self, a: list[int]) -> int:
        max_val = -sys.maxsize
        ans = 0
        for i in range(len(a)):
            max_val = max(a[i], max_val)
            # if number is in the ideal place, increase ans
            if max_val == i:
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.maxChunksToSorted([4, 3, 2, 1, 0]), 1)
        self.assertEqual(obj.maxChunksToSorted([4, 3, 2, 1, 2]), 1)
        self.assertEqual(obj.maxChunksToSorted([1, 0, 2, 3, 4]), 4)
        self.assertEqual(obj.maxChunksToSorted([2, 0, 1]), 1)


if __name__ == "__main__":
    unittest.main()
