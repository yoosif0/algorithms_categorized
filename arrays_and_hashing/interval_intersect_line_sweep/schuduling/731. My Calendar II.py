"""
https://leetcode.com/problems/my-calendar-ii
[
    [5,10]:1,
    [20,25]:1,
    [55,60]:1,
    [10,20]:2,
    [25,55]:2
]
"""

import unittest


class MyCalendarTwo:
    def __init__(self):
        self.m = {}

    def book(self, start: int, end: int) -> bool:
        self.m[start] = self.m.get(start, 0) + 1
        self.m[end] = self.m.get(end, 0) - 1
        cur = 0
        for k in self.m:
            if start <= k < end:
                cur += self.m[k]
                if cur > 2:
                    self.m[start] -= 1
                    self.m[end] += 1
                    return False
        return True


"""
{10: 2, 20: -1, 50: 1, 60: -1, 40: -1}
[[10,20],[50,60],[10,40]]
"""


class Test(unittest.TestCase):
    def test(self):
        obj = MyCalendarTwo()
        self.assertEqual(obj.book(10, 20), True)
        self.assertEqual(obj.book(50, 60), True)
        self.assertEqual(obj.book(10, 40), True)
        self.assertEqual(obj.book(5, 15), False)
        self.assertEqual(obj.book(5, 10), True)
        self.assertEqual(obj.book(25, 55), True)


if __name__ == "__main__":
    unittest.main()
