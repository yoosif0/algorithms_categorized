"""
https://leetcode.com/problems/daily-temperatures/
73,74,75,71,69,72,76,73

73: m73 waiting=[(73,0)]
74: stack.pop() arr[tup[1]] = temp - tup[0]. stack.append((74,1))
75: 

Btw, we don't need to store temperatures again in the stack. We can just store the index since we can get the
temp easily by knowing the index
"""
import unittest


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(
            obj.dailyTemperatures([30, 40, 50, 60]),
            [1, 1, 1, 0],
        )
        self.assertEqual(
            obj.dailyTemperatures([30, 60, 90]),
            [1, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
