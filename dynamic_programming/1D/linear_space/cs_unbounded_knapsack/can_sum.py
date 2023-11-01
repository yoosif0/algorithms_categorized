"""
https://www.youtube.com/watch?v=oBt53YbR9Kk at 3:52:42
#decision
2 5
0 1 2 3 4 5 6 7
    t   t t t t
"""
import functools
import unittest


class Solution:
    # def canSum(self, t: int, cs: list[int]) -> bool:
    #     dp = [False for _ in range(t + 1)]
    #     cs = list(filter(lambda x: x <= t, cs))
    #     for c in cs:
    #         dp[c] = True
    #         for i in range(c + 1, len(dp)):
    #             if dp[i - c]:
    #                 dp[i] = True
    #     return dp[-1]

    def canSum(self, t: int, cs: list[int]) -> bool:
        found = False

        @functools.cache
        def rcrs(t: int):
            nonlocal found
            nonlocal cs
            for c in cs:
                if c > t:
                    continue
                suf = t - c
                if suf == 0:
                    found = True
                    return
                rcrs(suf)

        rcrs(t)
        return found


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.canSum(7, [2, 3]), True)
        self.assertEqual(t.canSum(7, [5, 3, 4, 7]), True)
        self.assertEqual(t.canSum(7, [2, 4]), False)
        self.assertEqual(t.canSum(8, [2, 3, 5]), True)
        self.assertEqual(t.canSum(300, [7, 14]), False)


if __name__ == "__main__":
    unittest.main()
