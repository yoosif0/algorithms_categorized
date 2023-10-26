"""
https://leetcode.com/problems/maximum-gap

"""

import math
import unittest


# 25 -3 = 22 / 8 =

1001 * 7 / 1001


class Solution:
    def maximumGap(self, a: list[int]) -> int:
        if len(a) < 2:
            return 0
        # number of buckets is one less than the length of arr just to ensure at least 2 items are in the same bucket (pigeon hole)
        bs = [[] for _ in range(len(a) - 1)]
        # put pigenos in holes (buckets)
        r = max(a)
        for i in a:
            bs[i * (len(bs) - 1) // r].append(i)
        # get max and min for each bucket (pigeon hole)
        a = []
        for b in bs:
            if not b:
                continue
            a.append((min(b), max(b)))
        # find biggest difference between a min of bucket and the max of the bucket before
        ans = a[0][1] - a[0][0]
        cur = a[0][1]
        for i in range(1, len(a)):
            ans = max(ans, a[i][0] - cur)
            cur = a[i][1]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumGap([3, 14, 15, 83, 6, 4, 19, 20, 40]), 43)
        self.assertEqual(t.maximumGap([10]), 0)
        self.assertEqual(t.maximumGap([1, 10000000]), 9999999)


if __name__ == "__main__":
    unittest.main()
