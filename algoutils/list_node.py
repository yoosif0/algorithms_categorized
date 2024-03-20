from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def arr(self):
        a = []
        while self:
            a.append(self.val)
            self = self.next
        return a

    def __repr__(self):
        return str(self.arr())


# converts an array to a linkedlist
def ll(a: list[int]):
    d = ListNode(None)
    b = d
    for n in a:
        b.next = ListNode(n)
        b = b.next
    return d.next


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ListNode(4, ListNode(3, ListNode(1))).arr(), [4, 3, 1])
        self.assertEqual(
            ll([4, 3, 1]).arr(), ListNode(4, ListNode(3, ListNode(1))).arr()
        )


if __name__ == "__main__":
    unittest.main()
