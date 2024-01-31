__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

# from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()  # key: nums, value: nums_index
        for index, value in enumerate(nums):
            if nums_dict.__contains__(target - value):
                return [nums_dict[target - value], index]
            else:
                nums_dict[value] = index
        return [-1, -1]


"""
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
"""
