"""
https://leetcode.com/problems/top-k-frequent-elements/
To have O(n) time, you don't sort. Instead you bucket sort
"""


from typing import Dict
import unittest


# O(nlogn)
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         ans = []
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#         freqs_with_num = []
#         for num in freq:
#             freqs_with_num.append((num, freq[num]))
#         freqs_with_num.sort(key=lambda x: -x[1])

#         for i in range(k):
#             ans.append(freqs_with_num[i][0])
#         return ans


# O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = []
        char_counter = {}
        highest_frequency = 0
        for num in nums:
            char_counter[num] = char_counter.get(num, 0) + 1
            highest_frequency = max(highest_frequency, char_counter[num])

        freq_to_nums: Dict[int, list[int]] = {}
        for num in char_counter:
            freq = char_counter[num]
            if freq not in freq_to_nums:
                freq_to_nums[freq] = []
            freq_to_nums[freq].append(num)

        for i in range(highest_frequency, 0, -1):
            if len(ans) == k:
                break
            if i not in freq_to_nums:
                continue
            for num in freq_to_nums[i]:
                ans.append(num)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(obj.topKFrequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
