"""
[ 5, 7, 1, 4, 3, 6, 2, 9, 2 ]
5: 5
7: 12
1: 13
4: 17
3: 20 a20
6: 21 a19
"""


import unittest


class Solution:
    def sol(self, arr: list[int], k: int) -> int:
        cur_count = 0
        ans = 0

        def add_to_window(index: int):
            nonlocal cur_count
            cur_count += arr[index]

        def remove_from_window(index: int):
            nonlocal cur_count
            cur_count -= arr[index]

        def update_ans_if_applicable():
            nonlocal ans
            ans = max(ans, cur_count)

        for i in range(k):
            add_to_window(i)
        update_ans_if_applicable()

        for i in range(k, len(arr)):
            add_to_window(i)
            remove_from_window(i - k)
            update_ans_if_applicable()
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sol([5, 7, 1, 4, 3, 6, 2, 9, 2], 5), 24)


if __name__ == "__main__":
    unittest.main()
