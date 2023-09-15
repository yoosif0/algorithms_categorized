"""
https://leetcode.com/problems/time-based-key-value-store/
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
from dataclasses import dataclass
from typing import Dict


@dataclass
class TimedVal:
    timestamp: int
    value: str


class TimeMap:
    def __init__(self):
        self.o: Dict[str, list[TimedVal]] = {}

    def bisect_left(self, key: str, target: int) -> int:
        timed_vals = self.o[key]
        lo = 0
        hi = len(timed_vals)
        while lo < hi:
            mid = (hi + lo) // 2
            mid_val = timed_vals[mid].timestamp
            if mid_val < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.o:
            self.o[key] = []
        self.o[key].append(TimedVal(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.o:
            return ""
        arr = self.o[key]
        index = self.bisect_left(key, timestamp)
        if index == len(arr) or timestamp < arr[index].timestamp:
            if index - 1 < 0:
                return ""
            return arr[index - 1].value
        return arr[index].value


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
