"""
https://leetcode.com/problems/longest-well-performing-interval
sliding window technique does not work here because the condition of the window is not monotonic.
monotonic means that the condition keeps satisfied as the window expands if it was satisfied once
#subarr
"""

import unittest


class Solution:
    def longestWPI(self, a: list[int]) -> int:
        l = 0
        w = 1 if a[0] > 8 else 0
        ans = w
        for r in range(1, len(a)):
            w = w + 1 if a[r] > 8 else w
            print(f"w is {w}")
            if w / (r - l + 1) <= 0.5:
                print(f"not valid")
                w = w - 1 if a[l] > 8 else w
                l += 1
            else:
                print(f"valid. len is {r - l + 1} because r is {r} and l is {l}")
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.longestWPI([9, 9, 6, 0, 6, 6, 9]), 3)
        # self.assertEqual(t.longestWPI([6, 6, 6]), 0)
        # self.assertEqual(t.longestWPI([6, 6, 9]), 1)
        self.assertEqual(t.longestWPI([6, 9, 9]), 3)


"""
can't use sliding window and can't use 2 pointers
0, 1, 9, 9, 6, 0, 6, 6, 9, 2
-1, -1, 1, 1, -1, -1, -1, -1, 1, -1
-1,-2, -1, 0,-1, -2,  -3, -4, -3,-4


"""

if __name__ == "__main__":
    unittest.main()
