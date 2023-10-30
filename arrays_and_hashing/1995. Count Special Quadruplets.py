"""
https://leetcode.com/problems/count-special-quadruplets
#subsequence
#triplets
#store_indecis
"""

import collections
import unittest


class Solution:
    def countQuadruplets(self, a: list[int]) -> int:
        m = collections.defaultdict(list)
        for i, n in enumerate(a):
            m[n].append(i)
        ans = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                for k in range(j + 1, len(a)):
                    ans += len(list(filter(lambda x: x > k, m[a[i] + a[j] + a[k]])))
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countQuadruplets([1, 2, 3, 6]), 1)
        self.assertEqual(t.countQuadruplets([3, 3, 6, 4, 5]), 0)
        self.assertEqual(t.countQuadruplets([1, 1, 1, 3, 5]), 4)
        self.assertEqual(t.countQuadruplets([9, 6, 8, 23, 39, 23]), 2)
        self.assertEqual(t.countQuadruplets([28, 8, 49, 85, 37, 90, 20, 8]), 1)


if __name__ == "__main__":
    unittest.main()
