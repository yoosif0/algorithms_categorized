"""
https://leetcode.com/problems/sort-an-array
"""

import unittest


class Solution:
    def merge(self, a: list[int], a2: list[int]) -> None:
        ans = [None for _ in range(len(a) + len(a2))]
        p, p2 = 0, 0
        for i in range(len(ans)):
            if p2 >= len(a2):
                ans[i] = a[p]
                p += 1
            elif p >= len(a) or a2[p2] < a[p]:
                ans[i] = a2[p2]
                p2 += 1
            else:
                ans[i] = a[p]
                p += 1
        return ans

    def sortArray(self, a: list[int]) -> list[int]:
        if len(a) == 1:
            return a
        return self.merge(
            self.sortArray(a[: len(a) // 2]), self.sortArray(a[len(a) // 2 :])
        )


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(t.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])
        self.assertEqual(t.sortArray([5, 1, 1, 2, 0, 0, 3]), [0, 0, 1, 1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
