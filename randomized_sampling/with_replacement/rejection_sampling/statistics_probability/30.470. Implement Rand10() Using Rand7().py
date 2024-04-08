"""
"""

import random
import unittest


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self) -> int:
        while True:
            # uniform distribution of integers between 0 to 48 (1 to 49)
            r49 = 7 * (rand7() - 1) + rand7() - 1
            if r49 < 40:
                # limit urself to values from 0 to 39 to get something from 0 to 9 (and then add 1 to it)
                return r49 % 10 + 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        N = 100
        for _ in range(N):
            p = t.rand10()
            print(p)


if __name__ == "__main__":
    unittest.main()
