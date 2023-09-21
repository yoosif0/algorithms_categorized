"""
https://leetcode.com/problems/next-greater-element-ii/
[5,4,3,2,1]


12343
ans = [2,3,4,-1,4]
3:4[(3,4)]
4:3[(3,4),(4,3)]
0:1[(3,4),(4,3)]
1:2[(3,4),(4,3)]
2:3[(3,4),(4,3)]
3:4[(3,4)]


"""
import unittest


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            while len(stack) > 0 and num > nums[stack[-1]]:
                j = stack.pop()
                ans[j] = num
            stack.append(i)
        for i, num in enumerate(nums):
            while len(stack) > 0 and num > nums[stack[-1]]:
                j = stack.pop()
                ans[j] = num
        return ans


# class Solution:
#     def nextGreaterElements(self, nums: list[int]) -> list[int]:
#         stack = []
#         ans = [-1 for _ in range(len(nums))]
#         for i, num in enumerate(nums):
#             while len(stack) > 0 and num > nums[stack[-1]]:
#                 j = stack.pop()
#                 ans[j] = num
#             stack.append(i)
#         for i, num in enumerate(nums):
#             while len(stack) > 0 and num > nums[stack[-1]]:
#                 j = stack.pop()
#                 ans[j] = num
#         return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.nextGreaterElements([1, 2, 1]),
            [2, -1, 2],
        )
        self.assertEqual(
            obj.nextGreaterElements([1, 2, 3, 4, 3]),
            [2, 3, 4, -1, 4],
        )
        self.assertEqual(
            obj.nextGreaterElements([5, 4, 3, 2, 1]),
            [-1, 5, 5, 5, 5],
        )


if __name__ == "__main__":
    unittest.main()
