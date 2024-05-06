"""
https://leetcode.com/problems/time-based-key-value-store
{"foo": ["bar", "bar2"]}
{"foo": [1,4]}
"""

import unittest


class TimeMap:
    def __init__(self):
        self.t = {}
        self.v = {}

    def set(self, k: str, v: str, t: int) -> None:
        if k not in self.t:
            self.t[k] = [0]
            self.v[k] = [""]
        self.t[k].append(t)
        self.v[k].append(v)

    def get(self, k: str, t: int) -> str:
        if k not in self.t:
            return ""
        a = self.t[k]
        l = 0
        r = len(a) - 1
        while l < r:
            m = (l + r + 1) // 2
            if a[m] > t:
                r = m - 1
            else:
                l = m
        return self.v[k][r]


class Test(unittest.TestCase):
    def test_0(self):
        obj = TimeMap()
        obj.set("foo", "bar", 1)
        self.assertEqual(obj.get("foo", 1), "bar")
        self.assertEqual(obj.get("foo", 3), "bar")
        obj.set("foo", "bar2", 4)
        self.assertEqual(obj.get("foo", 4), "bar2")
        self.assertEqual(obj.get("foo", 5), "bar2")
        self.assertEqual(obj.get("b", 3), "")

    def test_1(self):
        obj = TimeMap()
        obj.set("foo", "zzz", 1)
        self.assertEqual(obj.get("foo", 1), "zzz")
        self.assertEqual(obj.get("foo", 3), "zzz")
        obj.set("foo", "bar2", 4)
        self.assertEqual(obj.get("foo", 4), "bar2")
        self.assertEqual(obj.get("foo", 5), "bar2")

    def test_2(self):
        obj = TimeMap()
        obj.set("love", "high", 10)
        obj.set("love", "low", 20)
        self.assertEqual(obj.get("love", 5), "")


if __name__ == "__main__":
    unittest.main()
