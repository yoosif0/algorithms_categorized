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


def circ_ll(a: list[int]):
    d = ListNode(None)
    b = d
    for n in a:
        b.next = ListNode(n)
        b = b.next
    b.next = d.next
    return d.next


class Test(unittest.TestCase):
    def test_arr(self):
        self.assertEqual(ListNode(4, ListNode(3, ListNode(1))).arr(), [4, 3, 1])

    def test_ll(self):
        self.assertEqual(
            ll([4, 3, 1]).arr(), ListNode(4, ListNode(3, ListNode(1))).arr()
        )

    def test_circ_ll(self):
        l = circ_ll([1, 2])
        self.assertEqual(l.val, 1)
        self.assertEqual(l.next.val, 2)
        self.assertEqual(l.next.next.val, 1)


if __name__ == "__main__":
    unittest.main()
