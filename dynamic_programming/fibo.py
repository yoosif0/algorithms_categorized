import unittest
import functools

# 0,1,2,3,4,5,6, 7, 8
# 0,1,1,2,3,5,8,13,21


def fibo_memoize(val: int, cache={0: 1, 1: 1}) -> int:
    if val in cache:
        return cache[val]
    cache[val] = fibo_memoize(val - 1) + fibo_memoize(val - 2)
    return cache[val]


@functools.cache
def fibo_memoize_functools(val: int) -> int:
    if val == 0:
        return 1
    if val == 1:
        return 1
    return fibo_memoize_functools(val - 1) + fibo_memoize_functools(val - 2)


def fibo_tabulate(val: int) -> int:
    dp = (val + 1) * [0]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, val + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[val]


class TestFibo(unittest.TestCase):
    def test_memoize(self):
        self.assertEqual(fibo_memoize(5), 8)
        self.assertEqual(fibo_memoize(6), 13)

    def test_memoize_f(self):
        self.assertEqual(fibo_memoize_functools(5), 8)
        self.assertEqual(fibo_memoize_functools(6), 13)
        self.assertEqual(fibo_memoize_functools(35), 14930352)

    def test_tabulate(self):
        self.assertEqual(fibo_tabulate(5), 8)
        self.assertEqual(fibo_tabulate(6), 13)


if __name__ == "__main__":
    unittest.main()
