"""
https://leetcode.com/problems/find-the-winner-of-an-array-game/
#simulation
to make the solution faster, don't run the simulation using a queue and popping and appending. Rather, try to image what would happend using pointers only without changing the array (or deque)
"""


import unittest


# O(n) time
class Solution:
    def getWinner(self, a: list[int], k: int) -> int:
        # reduce k to be the length of arr if it is higher since the result won't change when simulating further
        k = min(k, len(a))
        p = 0
        wins = 0
        for p2 in range(1, len(a)):
            if a[p] < a[p2]:
                p = p2
                wins = 1
            else:
                wins += 1
            if wins == k:
                return a[p]
        return a[p]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(obj.getWinner([2, 1, 3, 5, 4, 6, 7], 2), 5)
        self.assertEqual(obj.getWinner([1, 25, 35, 42, 68, 70], 1), 25)


"""
70 50 60 61 62 63
p              p2



2, 1, 3, 5, 4, 6, 7
         w  n 
w_i = 0
w_i = 2
w_i = 2
"""
if __name__ == "__main__":
    unittest.main()
