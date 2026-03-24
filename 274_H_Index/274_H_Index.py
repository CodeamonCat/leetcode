__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        c_len = len(citations)
        c_list = [0] * (c_len + 1)
        for c in citations:
            c_list[min(c, c_len)] += 1

        h_val = 0
        for i in range(c_len, 0, -1):
            h_val += c_list[i]
            if h_val >= i:
                return i
        return 0
