"""
https://leetcode.com/problems/top-k-frequent-words/
#bucket_sort
"""


import collections
import unittest


class Solution:
    def topKFrequent(self, a: list[str], k: int) -> list[str]:
        # word counter
        m = collections.Counter(a)
        # buckets for frequences. each bucket hold words with certain freq
        bs = [[] for _ in range(len(a))]
        for word in m:
            bs[m[word] - 1].append(word)
        ans = []
        for i in range(len(bs) - 1, -1, -1):
            # sorting bucket since they need to be in lexicographic order
            bs[i].sort()
            for word in bs[i]:
                ans.append(word)
        return ans[:k]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2),
            ["i", "love"],
        )
        self.assertEqual(
            obj.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3),
            ["i", "love", "coding"],
        )


if __name__ == "__main__":
    unittest.main()
