"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

"""
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        window_size = len(p)
        if window_size > len(s):
            return ans

        # build ideal char freq
        p_char_freq = {}
        for i in range(len(p)):
            char = p[i]
            p_char_freq[char] = p_char_freq.get(char, 0) + 1

        window_char_freq = {}
        # difference between window char_char_freq and p_char_freq. Whenever this is empty we know the window is ideal
        diff_char_freq = {}

        def update_diff_char_freq(char: str):
            diff_char_freq[char] = window_char_freq[char] - p_char_freq.get(char, 0)
            if diff_char_freq[char] == 0:
                diff_char_freq.pop(char)

        def add_to_char_freq(index: int):
            char = s[index]
            window_char_freq[char] = window_char_freq.get(char, 0) + 1
            update_diff_char_freq(char)

        def remove_from_cur_sum(index: int):
            char = s[index]
            window_char_freq[char] = window_char_freq[char] - 1
            update_diff_char_freq(char)

        def update_ans_if_window_is_ideal(index: int):
            if len(diff_char_freq) == 0:
                ans.append(index)

        # initial window
        for i in range(window_size):
            add_to_char_freq(i)
        update_ans_if_window_is_ideal(0)

        # Slide window
        for i in range(window_size, len(s)):
            add_to_char_freq(i)
            remove_from_cur_sum(i - window_size)
            update_ans_if_window_is_ideal(i - window_size + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findAnagrams("cbaebabacd", "abc"),
            [0, 6],
        )
        self.assertEqual(
            t.findAnagrams("abab", "ab"),
            [0, 1, 2],
        )


if __name__ == "__main__":
    unittest.main()
