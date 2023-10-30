"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array/
#triplets
#subsequence
when we are asked for a subsequence, we can't use a set. the constraints are small (n is max 100) so we can use a triple loop

not_my_solution
"""


import collections
import unittest


class Solution:
    # def unequalTriplets(self, a: list[int]) -> int:
    #     ans = 0
    #     for i in range(len(a)):
    #         for j in range(i + 1, len(a)):
    #             for k in range(j + 1, len(a)):
    #                 if a[i] != a[j] and a[j] != a[k] and a[i] != a[k]:
    #                     ans += 1
    #     return ans

    def unequalTriplets(self, a: list[int]) -> int:
        ans = 0
        prs = 0
        m = collections.Counter()
        for i, k in enumerate(a):
            print(k)
            ans += prs - m[k] * (i - m[k])
            prs += i - m[k]
            m[k] += 1
            print(ans, prs, m[k])
        return ans


"""
4,2
4,2
2,4

prs - m[k]
"""


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.unequalTriplets([4, 4, 2, 4, 3]), 3)


if __name__ == "__main__":
    unittest.main()
