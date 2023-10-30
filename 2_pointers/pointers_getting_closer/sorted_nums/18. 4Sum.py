"""
https://leetcode.com/problems/4sum/
#triplets
#n4_to_n3_time
"""


import unittest


class Solution:
    def fourSum(self, a: list[int], t: int) -> list[list[int]]:
        ans = []
        a.sort()
        for i in range(len(a) - 3):
            if i >= 1 and a[i] == a[i - 1]:
                continue
            for j in range(i + 1, len(a) - 2):
                if j > i + 1 and a[j] == a[j - 1]:
                    continue
                l = j + 1
                r = len(a) - 1
                while l < r:
                    if l != j + 1 and a[l] == a[l - 1]:
                        l += 1
                        continue
                    x = a[i] + a[j] + a[l] + a[r]
                    if x == t:
                        ans.append([a[i], a[j], a[l], a[r]])
                        l += 1
                    elif x < t:
                        l += 1
                    else:
                        r -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.fourSum([1, 0, -1, 0, -2, 2], 0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        )
        self.assertEqual(t.fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])


if __name__ == "__main__":
    unittest.main()
