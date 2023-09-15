"""
https://leetcode.com/problems/k-radius-subarray-averages/description/
"""
import unittest


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        cur_sum = 0
        ans = [-1] * len(nums)
        window_size = 2 * k + 1

        if window_size > len(nums):
            return ans

        def add_to_cur_sum(index: int):
            nonlocal cur_sum
            cur_sum += nums[index]

        def remove_from_cur_sum(index: int):
            nonlocal cur_sum
            cur_sum -= nums[index]

        def save_avg(index: int):
            avg = cur_sum // window_size
            ans[index] = avg

        # initial window
        for i in range(window_size):
            add_to_cur_sum(i)
        save_avg(k)

        # Slide window
        for i in range(window_size, len(nums)):
            add_to_cur_sum(i)
            remove_from_cur_sum(i - window_size)
            save_avg(i - k)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3),
            [-1, -1, -1, 5, 4, 4, -1, -1, -1],
        )
        self.assertEqual(
            t.getAverages([100000], 0),
            [100000],
        )
        self.assertEqual(
            t.getAverages([8], 100000),
            [-1],
        )


if __name__ == "__main__":
    unittest.main()
