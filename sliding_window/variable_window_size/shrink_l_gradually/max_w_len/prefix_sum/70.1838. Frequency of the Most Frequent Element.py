"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element
#no_need_valid_w
#find_max_w_len
#sorting_helps

"""

import unittest


class Solution:
    def maxFrequency(self, a: list[int], k: int) -> int:
        a.sort()
        ans = 0
        l = 0
        w = 0
        for r in range(len(a)):
            w += a[r]
            worst = (r - l) * a[r]
            if worst - (w - a[r]) > k:
                w -= a[l]
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxFrequency([1, 2, 4], 5), 3)
        self.assertEqual(t.maxFrequency([1, 4, 8, 13], 5), 2)
        self.assertEqual(t.maxFrequency([3, 9, 6], 2), 1)
        self.assertEqual(
            t.maxFrequency(
                [
                    9940,
                    9995,
                    9944,
                    9937,
                    9941,
                    9952,
                    9907,
                    9952,
                    9987,
                    9964,
                    9940,
                    9914,
                    9941,
                    9933,
                    9912,
                    9934,
                    9980,
                    9907,
                    9980,
                    9944,
                    9910,
                    9997,
                ],
                7925,
            ),
            22,
        )

        self.assertEqual(
            t.maxFrequency(
                [
                    9930,
                    9923,
                    9983,
                    9997,
                    9934,
                    9952,
                    9945,
                    9914,
                    9985,
                    9982,
                    9970,
                    9932,
                    9985,
                    9902,
                    9975,
                    9990,
                    9922,
                    9990,
                    9994,
                    9937,
                    9996,
                    9964,
                    9943,
                    9963,
                    9911,
                    9925,
                    9935,
                    9945,
                    9933,
                    9916,
                    9930,
                    9938,
                    10000,
                    9916,
                    9911,
                    9959,
                    9957,
                    9907,
                    9913,
                    9916,
                    9993,
                    9930,
                    9975,
                    9924,
                    9988,
                    9923,
                    9910,
                    9925,
                    9977,
                    9981,
                    9927,
                    9930,
                    9927,
                    9925,
                    9923,
                    9904,
                    9928,
                    9928,
                    9986,
                    9903,
                    9985,
                    9954,
                    9938,
                    9911,
                    9952,
                    9974,
                    9926,
                    9920,
                    9972,
                    9983,
                    9973,
                    9917,
                    9995,
                    9973,
                    9977,
                    9947,
                    9936,
                    9975,
                    9954,
                    9932,
                    9964,
                    9972,
                    9935,
                    9946,
                    9966,
                ],
                3056,
            ),
            73,
        )


if __name__ == "__main__":
    unittest.main()
