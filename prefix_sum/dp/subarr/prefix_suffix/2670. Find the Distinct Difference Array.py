"""
https://leetcode.com/problems/find-the-distinct-difference-array
#prefix_suffix
3 2 3 4 2  suf={3:1, 2:2, 4:1} pre={3:1}

"""
from collections import Counter, defaultdict
import unittest


class Solution:
    def distinctDifferenceArray(self, a: list[int]) -> list[int]:
        pre = defaultdict(int)
        suf = Counter(a)
        for i in range(len(a)):
            pre[a[i]] += 1
            suf[a[i]] -= 1
            if suf[a[i]] == 0:
                suf.pop(a[i])
            a[i] = len(pre) - len(suf)
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.distinctDifferenceArray([1, 2, 3, 4, 5]), [-3, -1, 1, 3, 5])


if __name__ == "__main__":
    unittest.main()
