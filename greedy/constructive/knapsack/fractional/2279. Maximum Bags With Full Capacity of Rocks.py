"""
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
the trick here is to sort by how much rocks left for each bag to reach full capacity
"""
import unittest


class Solution:
    def maximumBags(self, a: list[int], a2: list[int], x: int) -> int:
        # get differece between full capacity and current capacity. this is the only arr we need
        for i in range(len(a)):
            a[i] = a[i] - a2[i]
        a.sort()
        ans = 0
        for i in range(len(a)):
            if a[i] > x:
                break
            x -= a[i]
            ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2), 3)


if __name__ == "__main__":
    unittest.main()
