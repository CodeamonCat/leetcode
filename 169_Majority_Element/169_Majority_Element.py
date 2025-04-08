__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
