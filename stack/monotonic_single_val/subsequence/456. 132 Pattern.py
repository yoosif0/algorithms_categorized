"""
https://leetcode.com/problems/132-pattern/

Sliding window doesn't work here because the 3 values don't need to be consecutive. Also we can't just keep
track of min and max because the order of min, max, mid is relevant. You can't have the order switches to
(max, min, mid) for example.


Questions like this asing for three different instances are hard like the sum of 3.

Here we first try to find the "32" pair by maintaining a monotonically decreasing stack

not_my_solution_fully


"""

import sys
import unittest


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        st = []
        two = None
        for i in range(len(nums) - 1, -1, -1):
            if two and nums[i] < two:
                # found the 1_candidate
                return True
            while st and nums[i] > st[-1]:
                two = st.pop()
            st.append(nums[i])
        return False


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.find132pattern([3, 1, 4, 2]), True)
        self.assertEqual(obj.find132pattern([1, 2, 3, 4]), False)
        self.assertEqual(obj.find132pattern([-1, 3, 2]), True)
        self.assertEqual(obj.find132pattern([3, 5, 0, 3, 4]), True)
        self.assertEqual(obj.find132pattern([1, 0, 1, -4, -3]), False)


"""
pop when num > stack[-1]
1,2,3,4
[4] popped everything before

3,1,4,2
[4] popped 3 and 1 min_popped=1, waiting for increase that is <stack[-1] and >min_popped

-1,3,2
[3] popped -1

3,5,0,3,4
[5] popped 3. 
0 is not > than min_popped so does not satisfy condition
4 satisfy the condition

"""

if __name__ == "__main__":
    unittest.main()
