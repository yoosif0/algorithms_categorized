import functools
import unittest


@functools.cache
def set_bits_count_for_int(number: int) -> int:
    if number == 0:
        return 0
    return int(number & 1) + set_bits_count_for_int(number // 2)


def set_bits_count(number: int) -> list[int]:
    arr = []
    for i in range(number + 1):
        arr.append(set_bits_count_for_int(i))
    return arr


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        self.assertEqual(set_bits_count(1), [0, 1])
        self.assertEqual(set_bits_count(2), [0, 1, 1])
        self.assertEqual(set_bits_count(3), [0, 1, 1, 2])
        self.assertEqual(set_bits_count(4), [0, 1, 1, 2, 1])
        self.assertEqual(set_bits_count(5), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
