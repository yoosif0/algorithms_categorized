"""
[10,5,2,6]
10: add 10 to cache since it's less than 100 and add 1 to total  [10]
5:  set cache to 15 (5*10), total = 3  [5], [10,5]
2:  cache * num <100  set cache to 10 (5*2) total=5  [2], [5,2]
6:  cache * num <100  set cache to cache * num total=8  [6], [5,2,6], [2,6]


"""
import unittest
from collections import deque


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        cache = deque([])
        cache_value = 1
        total = 0
        for num in nums:
            if num >= k:
                cache = deque([])
                cache_value = 1
                continue
            total = total + 1
            cache_value = cache_value * num
            cache.append(num)
            # keep removing first elements in cache till it fits num inside.
            while cache_value >= k:
                firstNum = cache.popleft()
                cache_value = cache_value / firstNum
            total = total + len(cache) - 1
        return total


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)
        self.assertEqual(t.numSubarrayProductLessThanK([1, 1, 1], 1), 0)


if __name__ == "__main__":
    unittest.main()
