"""
https://leetcode.com/problems/next-greater-element-i/description/

[2,1,3,4,2]
4:2[2] 
3:4[4] one popped [-1,-1]
2:3[4,3] 
1:1[4,3,1] ret 3 
0:2[4,3,2] popped 1 ret 3

pop if num is greater than stack

"""
import unittest


# iterating in reverse
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # no need to store the index in the stack (just the num). that's easier btw
        stack = []
        num_to_next_greater = {}
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()
            num_to_next_greater[num] = -1 if len(stack) == 0 else stack[-1]
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(num_to_next_greater[num])

        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]),
            [-1, 3, -1],
        )


if __name__ == "__main__":
    unittest.main()
