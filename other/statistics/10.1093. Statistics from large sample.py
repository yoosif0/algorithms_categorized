"""
https://leetcode.com/problems/statistics-from-a-large-sample/
"""

import sys
import unittest


class Solution:
    def sampleStats(self, a: list[int]) -> list[float]:
        ttl = 0
        cnt = 0
        mode = (0, 0)
        mn = -1
        mx = 0
        for i in range(len(a)):
            if a[i] == 0:
                continue
            if mn == -1:
                mn = i
            ttl += i * a[i]
            cnt += a[i]
            mx = i
            if a[i] > mode[1]:
                mode = (i, a[i])
        mean = ttl / cnt
        ans = [mn, mx, mean, -1, mode[0]]
        # get median
        if cnt % 2 == 1:
            cutof = cnt // 2 + 1
            for i in range(len(a)):
                if a[i] == 0:
                    continue
                cnt -= a[i]
                if cnt < cutof:
                    ans[3] = i
                    return ans
        else:
            cutof = cnt // 2
            for i in range(len(a)):
                if a[i] == 0:
                    continue
                cnt -= a[i]
                if cnt < cutof:
                    ans[3] = i
                    return ans
                elif cnt == cutof:
                    for j in range(i + 1, len(a)):
                        if a[j] == 0:
                            continue
                        ans[3] = (i + j) / 2
                        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.sampleStats([0, 1, 3, 5, 0, 0, 0]), [1, 3, 2.4444444444444446, 3, 3]
        )
        self.assertEqual(t.sampleStats([0, 1, 3, 4, 0, 0, 0]), [1, 3, 2.375, 2.5, 3])


if __name__ == "__main__":
    unittest.main()
