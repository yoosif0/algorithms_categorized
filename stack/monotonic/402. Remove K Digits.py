"""
https://leetcode.com/problems/remove-k-digits/description/
4 removed k=1 3 removed k=2 2 removed k is complete. continue the number
1

num = "10200", k = 1
0200 if it starts with 0 remove the first char


The idea here is to pop from stack if the number is higher than what is in until you have popped enough (k)
then continue the number. This is a monotonically increasing stack (until k is reached). Monotonically increasing
means that we keep removing high numbers from stack.

How did we know that this requires a monotinic stack? Because this problems subscribes to removing the next higher number

"""
from collections import deque
import unittest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque([num[0]])
        removed = 0
        for i in range(1, len(num)):
            while stack and num[i] < stack[-1] and removed < k:
                stack.pop()
                removed += 1
            # do not add to an empty stack a leading 0
            if not stack and num[i] == "0":
                continue
            stack.append(num[i])
        # sometimes you did not remove enough like "129"
        while stack and removed < k:
            stack.pop()
            removed += 1
        if not stack:
            return "0"
        ans = "".join(stack)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.removeKdigits("1432219", 3), "1219")
        self.assertEqual(obj.removeKdigits("10200", 1), "200")
        self.assertEqual(obj.removeKdigits("10", 2), "0")
        self.assertEqual(obj.removeKdigits("129", 2), "1")
        self.assertEqual(obj.removeKdigits("9", 1), "0")
        self.assertEqual(obj.removeKdigits("10", 1), "0")


if __name__ == "__main__":
    unittest.main()
