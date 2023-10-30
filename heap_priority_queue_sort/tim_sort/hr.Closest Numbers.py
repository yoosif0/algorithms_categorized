"""
https://www.hackerrank.com/challenges/closest-numbers
5 2 3 4 1
1 2 3 4 5

"""

import collections
import unittest


def closestNumbers(a: list[int]) -> list[int]:
    a.sort()
    cur = a[1] - a[0]
    ans = [a[0], a[1]]
    for i in range(2, len(a)):
        df = a[i] - a[i - 1]
        if df < cur:
            ans = [a[i - 1], a[i]]
            cur = df
        elif df == cur:
            ans.append(a[i - 1])
            ans.append(a[i])
    return ans


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closestNumbers([5, 2, 3, 4, 1]), [1, 2, 2, 3, 3, 4, 4, 5])
        self.assertEqual(
            closestNumbers(
                [
                    -20,
                    -3916237,
                    -357920,
                    -3620601,
                    7374819,
                    -7330761,
                    30,
                    6246457,
                    -6461594,
                    266854,
                ]
            ),
            [-20, 30],
        )


if __name__ == "__main__":
    unittest.main()
