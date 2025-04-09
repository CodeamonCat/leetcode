__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def jump(self, nums: List[int]) -> int:
        steps = 0
        jump_end = 0
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == jump_end:
                steps += 1
                jump_end = max_reach
        return steps
