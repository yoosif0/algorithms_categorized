"""
https://leetcode.com/problems/design-twitter/
"""


import unittest


class Twitter:
    def __init__(self):
        self.u = {}
        self.t = []

    def postTweet(self, k: int, t: int) -> None:
        if k not in self.u:
            self.u[k] = {k}
        self.t.append((k, t))

    def getNewsFeed(self, k: int) -> list[int]:
        a = []
        for i in range(len(self.t)):
            u, t = self.t[-1 - i]
            if u in self.u[k]:
                a.append(t)
            if len(a) == 10:
                break
        return a

    def follow(self, k: int, f: int) -> None:
        if k not in self.u:
            self.u[k] = {k}
        self.u[k].add(f)

    def unfollow(self, k: int, f: int) -> None:
        if f in self.u[k]:
            self.u[k].remove(f)


class Test(unittest.TestCase):
    def test(self):
        obj = Twitter()
        obj.postTweet(1, 20)
        obj.postTweet(2, 21)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [20])
        obj.follow(1, 2)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [21, 20])
        obj.unfollow(1, 2)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [20])


if __name__ == "__main__":
    unittest.main()
