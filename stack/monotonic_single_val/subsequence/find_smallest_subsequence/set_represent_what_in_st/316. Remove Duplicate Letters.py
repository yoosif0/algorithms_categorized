"""
like 1081
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        st = []
        # set that represents what's in the stack.
        st_set = set()
        for i in range(len(s)):
            if s[i] in st_set:
                continue
            while st and s[i] < st[-1] and last[st[-1]] > i:
                st_set.remove(st.pop())
            st.append(s[i])
            st_set.add(s[i])
        return "".join(st)
