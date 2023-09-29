"""
https://leetcode.com/problems/3sum-closest
"""


import unittest


class Solution:
    def threeSumClosest(self, a: list[int], target: int) -> int:
        ans = a[0] + a[1] + a[2]
        a.sort()
        for i in range(len(a)):
            l = i + 1
            r = len(a) - 1
            while l < r:
                sum = a[l] + a[r] + a[i]
                if sum == target:
                    return target
                if abs(target - ans) > abs(target - sum):
                    ans = sum
                if sum < target:
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
