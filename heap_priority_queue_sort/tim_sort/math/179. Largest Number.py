"""
https://leetcode.com/problems/largest-number/

#math
if they are equal compare with the next digit. for example, 3 and 30 are equal in the first  digit, therefore we compare 3 to 0 and this mean we favor 3. The whole trick here is the compare function where when we compare which of 2 stringified numbers should come first, we compare

35/3  11r2
34/3  11r1
3/3   1 r0
32/3  10r2
30/3  10r0

"""


import functools
import unittest


def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


class Solution:
    def largestNumber(self, a: list[int]) -> str:
        # convert to string to be able to sort and compare x + y to y + x
        a = map(str, a)
        a = sorted(a, key=functools.cmp_to_key(compare))
        # if it starts with 0, it means that everything else is 0. we don't want repeated 0s so we just return a 0
        if a[0] == "0":
            return "0"
        a = "".join(a)
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.largestNumber([10, 2]), "210")
        self.assertEqual(t.largestNumber([0, 0]), "0")


if __name__ == "__main__":
    unittest.main()
