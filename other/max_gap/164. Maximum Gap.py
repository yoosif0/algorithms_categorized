"""
https://leetcode.com/problems/maximum-gap

If the bucket size is max-min/(N-1), this means that we can skip comparisons with numbers inside the bucket. We only compare the max of one bucket with the min of the other.

20 22 23 28 32 39

cap = 19/4 =4.75 


20-24           24-28       28-32         32-36       36-39
20,22,23         28          32                         39

"""

import unittest


class Solution:
    def maximumGap(self, a: list[int]) -> int:
        if len(a) < 2:
            return 0
        l, h = min(a), max(a)
        if l == h or len(a) == 2:
            return abs(a[1] - a[0])
        # number of buckets is one less than the length of arr just to ensure at least one bucket has 2 items
        bs = [[] for _ in range(len(a) - 1)]
        # len(bs) - 1 is the number of gaps between buckets. cp is the capactity of each bucket 
        cp = (h-l) / (len(bs) - 1)
        # put pigenos in holes (buckets)
        for x in a:
            i = int((x-l) // cp) 
            bs[i].append(x)
        del a
        # get max and min for each bucket (pigeon hole)
        bs = [(min(b), max(b)) for b in filter(lambda x: x, bs)]
        # find biggest difference between a min of bucket and the max of the bucket before
        ans = bs[0][1] - bs[0][0]
        for i in range(1, len(bs)):
            ans = max(ans, bs[i][0] - bs[i-1][1])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumGap([1,1,1,1]), 0)
        self.assertEqual(t.maximumGap([20, 22,23,28,32,39]), 7)
        self.assertEqual(t.maximumGap([3, 14, 15, 83, 6, 4, 19, 20, 40]), 43)
        self.assertEqual(t.maximumGap([10]), 0)
        self.assertEqual(t.maximumGap([1, 10000000]), 9999999)


if __name__ == "__main__":
    unittest.main()
