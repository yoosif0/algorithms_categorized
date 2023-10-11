"""
https://leetcode.com/problems/min-stack/
The trick here is to keep another stack for each min value and pop from this stack when popping from the
original stack when needed

Another way to solve it is to save the current min with the value in the same stack in a tuple


[-2],[0],[-3]
[-2]
[(-2,-2),(0,-2),(-3,-3)]


#attach_solution_to_stack
"""


import unittest


class MinStack:
    def __init__(self):
        self.num_stack = []

    def push(self, val: int) -> None:
        min_val = val if len(self.num_stack) == 0 else min(self.num_stack[-1][1], val)
        self.num_stack.append((val, min_val))

    def pop(self) -> None:
        self.num_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1][0]

    def getMin(self) -> int:
        return self.num_stack[-1][1]


class Test(unittest.TestCase):
    def test(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        self.assertEqual(obj.getMin(), -3)
        obj.pop()
        self.assertEqual(obj.top(), 0)
        self.assertEqual(obj.getMin(), -2)
        obj = MinStack()
        obj.push(0)
        obj.push(1)
        obj.push(0)
        self.assertEqual(obj.getMin(), 0)
        obj.pop()
        self.assertEqual(obj.getMin(), 0)


if __name__ == "__main__":
    unittest.main()
