__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        ptr = 2
        for idx in range(2, len(nums)):
            if nums[idx] != nums[ptr - 2]:
                nums[ptr] = nums[idx]
                ptr += 1

        return ptr
