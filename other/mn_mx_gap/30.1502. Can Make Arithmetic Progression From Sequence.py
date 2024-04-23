"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""

import sys
import unittest


class Solution:
    def canMakeArithmeticProgression(self, a: list[int]) -> bool:
        mn = sys.maxsize
        mx = -sys.maxsize
        st = set()
        for i in range(len(a)):
            mn = min(a[i], mn)
            mx = max(a[i], mx)
            st.add(a[i])
        # for cases like [0,0,0]
        if mn == mx:
            return True
        # for cases like [0,0,1]
        if (mx - mn) % (len(a) - 1) != 0:
            return False
        d = (mx - mn) // (len(a) - 1)
        for n in range(mn, mx + 1, int(d)):
            if n not in st:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.canMakeArithmeticProgression([1, 3, 5]), True)


if __name__ == "__main__":
    unittest.main()
