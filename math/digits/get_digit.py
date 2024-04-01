import unittest


def digit(n: int, digit_order: int):
    r = None
    for _ in range(digit_order):
        r = n % 10
        n = n // 10
    return r


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit(13, 2), 1)
        self.assertEqual(digit(213, 2), 1)
        self.assertEqual(digit(213, 1), 3)
        self.assertEqual(digit(213, 3), 2)
        self.assertEqual(digit(213, 4), 0)


if __name__ == "__main__":
    unittest.main()
