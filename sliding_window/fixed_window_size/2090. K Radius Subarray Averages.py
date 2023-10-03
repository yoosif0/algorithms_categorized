"""
https://leetcode.com/problems/k-radius-subarray-averages/
"""
import unittest


class Solution:
    def getAverages(self, a: list[int], z: int) -> list[int]:
        w = 0
        ans = [-1] * len(a)
        k = 2 * z + 1
        if k > len(a):
            return ans
        # initial w
        for i in range(k):
            w += a[i]
        # slide
        i = k - 1
        while True:
            avg = w // k
            ans[i - z] = avg
            i += 1
            if i == len(a):
                break
            w += a[i] - a[i - k]
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
