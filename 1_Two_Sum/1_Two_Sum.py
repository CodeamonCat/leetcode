__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()  # key: nums, value: nums_index
        for index, value in enumerate(nums):
            if nums_dict.__contains__(target - value):
                return [nums_dict[target - value], index]
            else:
                nums_dict[value] = index
        return [-1, -1]
