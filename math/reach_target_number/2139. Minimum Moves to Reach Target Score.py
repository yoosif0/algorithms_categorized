"""
https://leetcode.com/problems/minimum-moves-to-reach-target-score/
#greedy
#reach_target_number
#move_backward
"""
import unittest


class Solution:
    def minMoves(self, n: int, maxDoubles: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 != 0:
                n -= 1
                ans += 1
            elif maxDoubles:
                n = n // 2
                maxDoubles -= 1
                ans += 1
            else:
                return ans + n - 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minMoves(19, 2), 7)
        self.assertEqual(t.minMoves(5, 0), 4)
        self.assertEqual(t.minMoves(10, 4), 4)
        self.assertEqual(t.minMoves(656101987, 1), 328050994)


if __name__ == "__main__":
    unittest.main()
