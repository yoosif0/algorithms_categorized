"""
https://leetcode.com/problems/3sum-closest
#triplets
#n3_to_n2_time
"""


import unittest


class Solution:
    def threeSumClosest(self, a: list[int], t: int) -> int:
        ans = a[0] + a[1] + a[2]
        a.sort()
        for i in range(len(a)):
            l = i + 1
            r = len(a) - 1
            while l < r:
                x = a[l] + a[r] + a[i]
                if x == t:
                    return t
                if abs(t - ans) > abs(t - x):
                    ans = x
                if x < t:
                    l += 1
                else:
                    r -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(t.threeSumClosest([0, 0, 0], 1), 0)


if __name__ == "__main__":
    unittest.main()
