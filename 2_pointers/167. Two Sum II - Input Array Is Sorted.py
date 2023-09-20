"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
[1,2,3,4,5,7,11,15] 9

The array is sorted so we can move the right pointer to the left if the sum is more than target
and move the left pointer to the right when the sum is less than target

Notice that they require that the solution must use only constant extra space so we can't use a hashmap
to store numbers seen.
"""
import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        return [l, r]

    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
    #     num_to_index_hash = {}
    #     for i, num in enumerate(numbers):
    #         if (target - num) in num_to_index_hash:
    #             return [num_to_index_hash[target - num] + 1, i + 1]
    #         num_to_index_hash[num] = i
    #     return []


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.twoSum([2, 7, 11, 15], 9), [1, 2])


if __name__ == "__main__":
    unittest.main()
