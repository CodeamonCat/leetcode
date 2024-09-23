__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_s = 0, 0
        last_index = dict()

        for right, value in enumerate(s):
            left = max(left, last_index[value] +
                       1) if value in last_index else left
            max_s = max(max_s, right - left + 1)
            last_index[value] = right

        return max_s
