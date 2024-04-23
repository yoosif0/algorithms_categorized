"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
You can not add "l" because sometimes what's before "l" makes the subarry invalid
"""

import unittest


class Solution:
    def numberOfSubarrays(self, a: list[int], k: int) -> int:
        a = [0 if n % 2 == 0 else 1 for n in a]
        m = {0: 1}
        cnt = 0
        acc = 0
        for i in range(len(a)):
            acc += a[i]
            if acc - k in m:
                cnt += m[acc - k]
            if acc not in m:
                m[acc] = 0
            m[acc] += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numberOfSubarrays([1, 1, 2, 1, 1], 3), 2)
        self.assertEqual(t.numberOfSubarrays([2, 4, 6], 1), 0)
        self.assertEqual(t.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2), 16)


if __name__ == "__main__":
    unittest.main()
