"""
https://leetcode.com/problems/min-stack/
Save the current min with the value in the same stack in a tuple


[-2],[0],[-3]
[-2]
[(-2,-2),(0,-2),(-3,-3)]

"""


import unittest


class MinStack:
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        ans = val if not self.st else min(self.st[-1][1], val)
        self.st.append((val, ans))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


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
