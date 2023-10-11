"""
https://leetcode.com/problems/implement-stack-using-queues/

 back => [] <= front
fns: appendleft, pop

[2,5,3,4]

7
"""


from collections import deque
import unittest


class MyStack:
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x: int) -> None:
        self.q2.appendleft(x)
        while len(self.q1) > 0:
            self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


class Test(unittest.TestCase):
    def test(self):
        obj = MyStack()
        obj.push(5)
        obj.push(2)
        self.assertEqual(obj.pop(), 2)
        self.assertEqual(obj.top(), 5)
        self.assertEqual(obj.empty(), False)


if __name__ == "__main__":
    unittest.main()
