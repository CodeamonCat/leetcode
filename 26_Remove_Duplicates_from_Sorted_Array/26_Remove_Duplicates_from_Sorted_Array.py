__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ptr = 1

        for idx in range(1, len(nums)):
            if nums[idx] != nums[ptr - 1]:
                nums[ptr] = nums[idx]
                ptr += 1

        return ptr
