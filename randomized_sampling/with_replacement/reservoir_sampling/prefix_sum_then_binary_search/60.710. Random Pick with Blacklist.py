"""
https://leetcode.com/problems/random-pick-with-blacklist
#intervals
"""

import random
import unittest


class Solution:
    def __init__(self, n: int, a: list[int]):
        a.sort()
        a.append(n)
        ivls = []
        l = 0
        for n in a:
            if l < n:
                ivls.append((l, n - 1))
            l = n + 1
        wps = []
        cur = 0
        for i in range(len(ivls)):
            cur += ivls[i][1] - ivls[i][0] + 1
            wps.append(cur)
        self.a = ivls
        self.wps = wps

    def pick(self) -> int:
        t = random.uniform(0, self.wps[-1])
        # find index of first item greater than t
        l = 0
        r = len(self.wps) - 1
        while l < r:
            m = (l + r) // 2
            if self.wps[m] < t:
                l = m + 1
            else:
                r = m
        ans = self.a[l]
        return random.randint(ans[0], ans[1])


class Test(unittest.TestCase):
    def test(self):
        t = Solution(7, [2, 3, 5])
        N = 10
        for _ in range(N):
            i = t.pick()
            print(i)
        t = Solution(4, [2, 1])
        N = 10
        for _ in range(N):
            i = t.pick()
            print(i)


if __name__ == "__main__":
    unittest.main()
