"""
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
"""
import unittest


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        cur_sum = 0
        ans = 0

        def add_to_cur_sum(index: int):
            nonlocal cur_sum
            cur_sum += arr[index]

        def remove_from_cur_sum(index: int):
            nonlocal cur_sum
            cur_sum -= arr[index]

        def check_avg():
            nonlocal ans
            avg = cur_sum / k
            if avg >= threshold:
                ans += 1

        # initial window
        for i in range(k):
            add_to_cur_sum(i)
        check_avg()

        # Slide window
        for i in range(k, len(arr)):
            add_to_cur_sum(i)
            remove_from_cur_sum(i - k)
            check_avg()
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4),
            3,
        )
        self.assertEqual(
            t.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5),
            6,
        )


if __name__ == "__main__":
    unittest.main()
