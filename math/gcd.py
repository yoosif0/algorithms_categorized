"""
1000  50
1000/50 = 200
if r==0:
    return n2
50 1000

divide bigger number with smaller number and if r==0, return smaller number. otherwise
32/20 = 1r12
20/12 = 1r8
12/8 =  1r4
8 /4 =  2

divide bigger by smaller till remainder goes to 0, then return smaller number


"""
import unittest


class Solution:
    def gcd(self, n, n2):
        if n < n2:
            n, n2 = n2, n
        while True:
            r = n % n2
            if not r:
                return n2
            else:
                n, n2 = n2, r


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.gcd(25, 30), 5)
        self.assertEqual(t.gcd(25, 31), 1)
        self.assertEqual(t.gcd(1000, 50), 50)
        self.assertEqual(t.gcd(50, 1000), 50)
        self.assertEqual(t.gcd(32, 20), 4)


if __name__ == "__main__":
    unittest.main()
