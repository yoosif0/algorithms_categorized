"""
https://leetcode.com/problems/subsets/description/
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

1, alone, with its next, with its next


[1,2,3,4]
[],[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]
"""
import unittest
from itertools import combinations
from bisect import bisect_left


def combi(arr: list[int], r: int):
    pool = tuple(arr)
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + len(arr) - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        for size in range(len(nums) + 1):
            for v in combi(nums, size):
                ans.append(list(v))
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.subsets([1, 2, 3, 4]), [[]])


if __name__ == "__main__":
    unittest.main()
