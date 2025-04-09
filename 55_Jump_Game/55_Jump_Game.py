__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for idx, num in enumerate(nums):
            if idx > max_reach:
                return False
            max_reach = max(max_reach, idx + num)
        return True