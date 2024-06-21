"""
@nested-tags:matching/brute_force
https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
it's ok to brute force here since the input is small
"""

import unittest


class Solution:
    def containsPattern(self, a: list[int], m: int, k: int) -> bool:
        for i in range(len(a) - m + 1):
            pat = tuple(a[i : i + m])
            cur = 1
            for j in range(i + m, len(a) - m + 1):
                if tuple(a[j : j + m]) == pat:
                    cur += 1
                    if cur >= k:
                        return True
                else:
                    break
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.containsPattern([1, 2, 4, 4, 4, 4], 1, 3), True)
        self.assertEqual(t.containsPattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2), True)
        self.assertEqual(t.containsPattern([1, 2, 3, 1, 2], 2, 2), False)


if __name__ == "__main__":
    unittest.main()
