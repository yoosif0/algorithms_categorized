"""
https://leetcode.com/problems/time-based-k-value-store/
[0,1,2,3,4,5,6,7,10,16,17,18,19,20]
l=0 m=6; mv=6; r=13; rv=20 
l=6 lv=6; m=9; mv=16;r=13; rv=20
l=6 lv=6; m=7; mv=7 r=8; rv=10


l=7 lv=7; m=10; mv=17;r=13; rv=20
r=10 rv=17

[1,4]
l=0 m=0 mv=1 r=1 rv=4

Note: time limit exceeded
"""

import unittest
import bisect


class TimeMap:
    def __init__(self):
        self.t = {}
        self.v = {}

    def set(self, k: str, v: str, t: int) -> None:
        if k not in self.t:
            self.t[k] = []
            self.v[k] = []
        self.t[k].append(t)
        self.v[k].append(v)

    def get(self, k: str, t: int) -> str:
        if k not in self.t:
            return ""
        i = bisect.bisect_left(self.t[k], t)
        if i == len(self.t[k]) or t < self.t[k][i]:
            if i - 1 < 0:
                return ""
            return self.v[k][i - 1]
        return self.v[k][i]


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


if __name__ == "__main__":
    unittest.main()
