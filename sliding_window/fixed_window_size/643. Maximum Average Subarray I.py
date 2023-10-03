"""
https://leetcode.com/problems/maximum-average-subarray-i/
"""
import unittest


class Solution:
    def findMaxAverage(self, a: list[int], k: int) -> float:
        w = 0
        for i in range(k):
            w += a[i]
        max_sum = w
        # Slide window
        i = k - 1
        while True:
            max_sum = max(w, max_sum)
            i += 1
            if i == len(a):
                break
            w += a[i] - a[i - k]
        return max_sum / k


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
