"""
https://leetcode.com/problems/find-pivot-index/
Input: nums = [1,7,3,6,5,6]
1: 1
7: 8
3: 11
6: 17
5: 22
6: 28

[4,-3,5,-7,8]
prefix: [4,1,6,-1,7]


[2, 1, -1]
prefix: [2,3,2]


"""
import unittest


def getPrefixSums(nums: list[int]) -> list[int]:
    prefix_sums = []
    prefix_sum = 0
    for num in nums:
        prefix_sum += num
        prefix_sums.append(prefix_sum)
    return prefix_sums


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sums = getPrefixSums(nums)
        if prefix_sums[-1] == prefix_sums[0]:
            return 0
        last_prefix_sum = prefix_sums[-1]
        for i in range(len(prefix_sums) - 1):
            if last_prefix_sum - prefix_sums[i + 1] == prefix_sums[i]:
                return i + 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(t.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(t.pivotIndex([4, -3, 5, -7, 8]), 2)
        self.assertEqual(t.pivotIndex([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
