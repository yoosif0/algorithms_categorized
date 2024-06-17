"""
@nested-tags:prefix_suffix
https://leetcode.com/problems/find-the-distinct-difference-array
3 2 3 4 2  suf={3:1, 2:2, 4:1} pre={3:1}

"""

import unittest


class Solution:
    def distinctDifferenceArray(self, a: list[int]) -> list[int]:
        # prefix array
        pre = [0 for _ in range(len(a))]
        fnd = set()
        cur = 0
        for i in range(len(pre)):
            if a[i] not in fnd:
                fnd.add(a[i])
                cur += 1
            pre[i] = cur
        # suffix array
        suf = [0 for _ in range(len(a))]
        fnd = set()
        cur = 0
        for i in range(len(suf) - 1, -1, -1):
            suf[i] = cur
            if a[i] not in fnd:
                fnd.add(a[i])
                cur += 1
        # ans from both arrays
        a = [0 for _ in range(len(a))]
        for i in range(0, len(a)):
            a[i] = pre[i] - suf[i]
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.distinctDifferenceArray([1, 2, 3, 4, 5]), [-3, -1, 1, 3, 5])


if __name__ == "__main__":
    unittest.main()
