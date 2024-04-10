"""
https://leetcode.com/problems/random-pick-with-blacklist
#bisect_post_process
"""

import bisect
import random
import unittest


class Solution:
    def __init__(self, n: int, a: list[int]):
        a.sort()
        a.append(n)
        a2 = []
        l = 0
        pre = [0]
        for n in a:
            if l < n:
                a2.append((l, n - 1))
                pre.append(pre[-1] + n - l)
            l = n + 1
        self.a2 = a2
        self.pre = pre

    def pick(self) -> int:
        rnd = random.uniform(0, self.pre[-1])
        i = bisect.bisect_left(self.pre, rnd) - 1
        ans = self.a2[i]
        return random.randint(ans[0], ans[1])


class Test(unittest.TestCase):
    def test(self):
        # t = Solution(7, [2, 3, 5])
        # N = 10
        # for _ in range(N):
        #     i = t.pick()
        #     print(i)
        t = Solution(4, [2, 1])
        N = 10
        for _ in range(N):
            i = t.pick()
            print(i)


if __name__ == "__main__":
    unittest.main()
