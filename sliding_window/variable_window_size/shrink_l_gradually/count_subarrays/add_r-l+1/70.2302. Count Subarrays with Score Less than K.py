"""
https://leetcode.com/problems/count-subarrays-with-score-less-than-k
2 tricks that enable sliding window.


"""

import unittest


class Solution:
    def countSubarrays(self, a: list[int], k: int) -> list[int]:
        l = 0
        w = 0
        cnt = 0
        for r in range(len(a)):
            w += a[r]
            while w * (r - l + 1) >= k:
                w -= a[l]
                l += 1
            cnt += r - l + 1
        return cnt

    # def countSubarrays(self, a: list[int], k: int) -> list[int]:
    #     a = list(accumulate(a, initial=0))
    #     cnt = 0
    #     mn_l = 1
    #     for r in range(1, len(a)):
    #         mx_l = r + 1
    #         while True:
    #             l = (mn_l + mx_l) // 2
    #             if mx_l <= mn_l:
    #                 break
    #             if (a[r] - a[l - 1]) * (r - l + 1) < k:
    #                 mx_l = l
    #             else:
    #                 mn_l = l + 1
    #         cnt += r - l + 1
    #     return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countSubarrays([2, 1, 4, 3, 5], 30), 11)
        self.assertEqual(t.countSubarrays([2, 1, 4, 3, 11], 10), 5)


if __name__ == "__main__":
    unittest.main()
