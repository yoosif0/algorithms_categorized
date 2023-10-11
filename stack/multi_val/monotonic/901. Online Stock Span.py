"""
https://leetcode.com/problems/online-stock-span/

[100,80,60,70,60,75,85]
0:100:1 [(1,100)] 
1:80:1 [(1,100),(1,80)]
2:60:1 [(0,100),(1,80),(1,60)]
3:70:2 [(0,100),(1,80),(2,70)] one popped
4:60:1 [(0,100),(1,80),(2,70),(1,60)]
5:75:4 [(0,100),(1,80),(4,75)] 2 popped

never pop if less. pop if more, decreasing monostack
"""
import unittest


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and price >= self.stack[-1][1]:
            ans += self.stack.pop()[0]
        self.stack.append((ans, price))
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = StockSpanner()
        self.assertEqual(obj.next(100), 1)
        self.assertEqual(obj.next(80), 1)
        self.assertEqual(obj.next(60), 1)
        self.assertEqual(obj.next(70), 2)
        self.assertEqual(obj.next(60), 1)
        self.assertEqual(obj.next(75), 4)


if __name__ == "__main__":
    unittest.main()
