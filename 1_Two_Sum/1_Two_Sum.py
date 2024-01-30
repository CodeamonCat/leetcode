__author__= "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"

# from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()   # key: nums, value: nums_index
        for idx, val in enumerate(nums):
            if numsDict.__contains__(target-val):
                return [numsDict[target-val], idx]
            else:
                numsDict[val] = idx

"""
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
"""