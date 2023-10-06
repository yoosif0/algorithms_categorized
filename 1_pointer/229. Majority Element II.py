"""
https://leetcode.com/problems/majority-element-ii
"""

import unittest


class Solution:
    def majorityElement(self, a: list[int]) -> list[int]:
        threshold = len(a) / 3
        counter = {}
        ans = set()
        for num in a:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > threshold:
                ans.add(num)
        return list(ans)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.majorityElement([3, 2, 3]), [3])
        self.assertEqual(obj.majorityElement([1]), [1])
        self.assertEqual(obj.majorityElement([1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()
