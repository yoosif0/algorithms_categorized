"""
https://leetcode.com/problems/next-greater-element-ii/
121
2:1 [1] ans -1
1:2 [2] pop 1 since greater ans -1
0:1 [2,1] ans 2
2:1 [2,1] pop 1 ans 2 
1:2 [2] pop all ans -1
0:1 ans 2

pop if what in stack is equal or less
"""
import unittest


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # store only num (no need to store index)
        stack = []
        ans = [-1 for _ in range(len(nums))]
        # loop twice because it's circular
        # iterating in reverse
        for j in range(len(nums) * 2 - 1, -1, -1):
            i = j % len(nums)
            num = nums[i]
            while len(stack) > 0 and stack[-1] <= num:
                stack.pop()
            ans[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(num)
        return ans


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
