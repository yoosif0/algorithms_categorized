"""
https://leetcode.com/problems/maximum-average-subarray-i/description/
"""
import unittest


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        ans = -float("inf")
        cur_sum = 0

        def add_num(index: int):
            nonlocal cur_sum
            num = nums[index]
            cur_sum += num

        def remove_num(index: int):
            nonlocal cur_sum
            num = nums[index]
            cur_sum -= num

        def update_ans_applicable():
            nonlocal ans
            cur_avg = cur_sum / k
            ans = max(cur_avg, ans)

        # initial window
        for i in range(k):
            add_num(i)
        update_ans_applicable()

        # Slide window
        for i in range(k, len(nums)):
            add_num(i)
            remove_num(i - k)
            update_ans_applicable()
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findMaxAverage([1, 12, -5, -6, 50, 3], 4),
            12.75000,
        )
        self.assertEqual(
            t.findMaxAverage([5], 1),
            5.000,
        )
        self.assertEqual(
            t.findMaxAverage([-5], 1),
            -5.000,
        )


if __name__ == "__main__":
    unittest.main()
