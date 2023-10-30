"""
https://leetcode.com/problems/count-good-triplets
#triplets
#subsequence

can't use binary search because array is not sorted and I can't sort the arr because it requires a subsequence
"""


import unittest

"""
3,0,1,1,9,7

"""


class Solution:
    def countGoodTriplets(self, a: list[int], x: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if abs(a[i] - a[j]) <= x:
                    for k in range(j + 1, len(a)):
                        if abs(a[j] - a[k]) <= b and abs(a[i] - a[k]) <= c:
                            ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3), 4)


if __name__ == "__main__":
    unittest.main()
