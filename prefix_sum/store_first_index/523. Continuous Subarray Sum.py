"""
https://leetcode.com/problems/continuous-subarray-sum
#store_index
#store_first_index
The reason we store the first index and not the last is because if the only index that fullfills the 
condition is the index before the current index, it won't work

23 2 4 6 6    7
2  4 1 0           
"""

import unittest


class Solution:
    def checkSubarraySum(self, a: list[int], k: int) -> bool:
        cur = 0
        m = {0: -1}
        for i in range(len(a)):
            cur = (cur + a[i]) % k
            if cur in m:
                if i - m[cur] > 1:
                    return True
            else:
                m[cur % k] = i
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.checkSubarraySum([6, 6, 7], 6), True)
        self.assertEqual(t.checkSubarraySum([23, 2, 4, 6, 7], 6), True)
        self.assertEqual(t.checkSubarraySum([23, 2, 6, 4, 7], 6), True)
        self.assertEqual(t.checkSubarraySum([23, 2, 6, 4, 7], 13), False)
        self.assertEqual(t.checkSubarraySum([23, 2, 4, 6, 6], 7), True)
        self.assertEqual(t.checkSubarraySum([2, 4, 3], 6), True)
        self.assertEqual(t.checkSubarraySum([5, 0, 0, 0], 3), True)
        self.assertEqual(t.checkSubarraySum([6, 7], 6), False)
        self.assertEqual(t.checkSubarraySum([0], 1), False)
        self.assertEqual(t.checkSubarraySum([1, 0], 2), False)
        self.assertEqual(t.checkSubarraySum([1, 2, 12], 6), False)


if __name__ == "__main__":
    unittest.main()
