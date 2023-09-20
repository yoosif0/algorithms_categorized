"""
https://leetcode.com/problems/longest-consecutive-sequence/
[100, 4, 200, 1, 3, 2]

1 2 3 4                 100                 200

You want to measure the length of each consequence. The trick here is to find the beginning or end of each
consequence and measure the length moving forward or backward respectively. Even though there is a while loop 
inside the for loop, this is still O(n)
"""
import unittest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            # only pick numbers that are the beginning of a consequence
            if (num - 1) in num_set:
                continue
            length = 1
            while num + length in num_set:
                length += 1
            ans = max(ans, length)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
        self.assertEqual(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]), 7)
        self.assertEqual(
            obj.longestConsecutive(
                [0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999]
            ),
            10,
        )


if __name__ == "__main__":
    unittest.main()
