"""
https://leetcode.com/problems/time-based-key-value-store
{"foo": ["bar", "bar2"]}
{"foo": [1,4]}

#bisect_right
#bisect_post_process
#bisect_pre_process
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
        i = bisect.bisect_right(self.t[k], t) - 1
        if i < 0:
            return ""
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
