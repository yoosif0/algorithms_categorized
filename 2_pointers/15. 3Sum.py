"""
https://leetcode.com/problems/3sum/
"""


import unittest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans: list[list[int]] = []
        for i in range(len(nums) - 2):
            # to eliminate duplication
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # to eliminate duplication
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return ans


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         store = set()
#         ans: list[list[int]] = []
#         for i in range(len(nums)):
#             store.add(nums[i])

#         tuple_store = {}
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 complement = -(nums[i] + nums[j])
#                 tuple_store[(nums[i], nums[j])] = complement

#         for t in tuple_store:
#             complement = tuple_store[t]
#             if complement in store:
#                 if complement < t[0] or complement < t[1]:
#                     continue
#                 ans.append([t[0], t[1], complement])
#         return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(t.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(t.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])


if __name__ == "__main__":
    unittest.main()
