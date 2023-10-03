"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

"""
import unittest


class Solution:
    def numOfSubarrays(self, a: list[int], k: int, threshold: int) -> int:
        w = 0
        ans = 0
        for i in range(k):
            w += a[i]
        # slide
        target = threshold * k
        i = k - 1
        while True:
            if w >= target:
                ans += 1
            i += 1
            if i >= len(a):
                break
            w += a[i] - a[i - k]
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
