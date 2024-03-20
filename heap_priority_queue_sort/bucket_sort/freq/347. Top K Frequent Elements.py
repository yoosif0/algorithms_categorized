"""
https://leetcode.com/problems/top-k-frequent-elements/
To have O(n) time, you don't sort. Instead you bucket sort

#bucket_sort
"""


import collections
import unittest


class Solution:
    def topKFrequent(self, a: list[int], k: int) -> list[int]:
        # num counter
        cnt = collections.Counter(a)
        # buckets
        bs = [[] for _ in range(len(a) + 1)]
        for num in cnt:
            bs[cnt[num]].append(num)
        ans = []
        for i in range(len(bs) - 1, -1, -1):
            for j in bs[i]:
                ans.append(j)
        return ans[:k]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(obj.topKFrequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
