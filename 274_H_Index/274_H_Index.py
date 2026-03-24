__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for idx, val in enumerate(citations):
            if not (val > idx):
                return idx
        return len(citations)
