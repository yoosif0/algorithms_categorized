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


[100,80,60,70,60,75,85]

"""
import unittest


class StockSpanner:
    def __init__(self):
        self.st = []

    def next(self, x: int) -> int:
        ans = 1
        while self.st and x >= self.st[-1][0]:
            ans += self.st.pop()[1]
        self.st.append((x, ans))
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
