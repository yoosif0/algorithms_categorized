import unittest


def dec2bin(n: int):
    m = []
    while n:
        m.append(n & 1)
        n = n // 2
    return "".join(map(str, m[::-1]))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dec2bin(1), "1")
        self.assertEqual(dec2bin(2), "10")
        self.assertEqual(dec2bin(3), "11")
        self.assertEqual(dec2bin(4), "100")
        self.assertEqual(dec2bin(5), "101")
        self.assertEqual(dec2bin(6), "110")
        self.assertEqual(dec2bin(7), "111")
        self.assertEqual(dec2bin(8), "1000")
        self.assertEqual(dec2bin(9), "1001")
        self.assertEqual(dec2bin(10), "1010")
        self.assertEqual(dec2bin(11), "1011")
        self.assertEqual(dec2bin(12), "1100")
        self.assertEqual(dec2bin(13), "1101")
        self.assertEqual(dec2bin(14), "1110")
        self.assertEqual(dec2bin(15), "1111")
        self.assertEqual(dec2bin(16), "10000")
        self.assertEqual(dec2bin(17), "10001")
        self.assertEqual(dec2bin(18), "10010")
        self.assertEqual(dec2bin(19), "10011")
        self.assertEqual(dec2bin(20), "10100")
        self.assertEqual(dec2bin(21), "10101")
        self.assertEqual(dec2bin(22), "10110")
        self.assertEqual(dec2bin(23), "10111")
        self.assertEqual(dec2bin(24), "11000")
        self.assertEqual(dec2bin(25), "11001")
        self.assertEqual(dec2bin(26), "11010")
        self.assertEqual(dec2bin(27), "11011")


if __name__ == "__main__":
    unittest.main()
