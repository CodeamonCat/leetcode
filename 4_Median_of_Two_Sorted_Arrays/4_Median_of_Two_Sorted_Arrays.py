__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:

        # len(nums1) <= len(nums2) is required
        if (len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1

        median = (len(nums1) + len(nums2) + 1) // 2
        left = 0
        right = len(nums1)

        while left < right:
            mid = left + (right - left) // 2
            mid2 = median - mid

            if nums1[mid] < nums2[mid2 - 1]:
                left = mid + 1
            else:
                right = mid

        mid = left
        mid2 = median - mid

        nums1_left_max = float('-inf') if mid == 0 else nums1[mid - 1]
        nums1_right_min = float('inf') if mid == len(nums1) else nums1[mid]
        nums2_left_max = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
        nums2_right_min = float('inf') if mid2 == len(nums2) else nums2[mid2]

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(nums1_left_max, nums2_left_max) +
                    min(nums1_right_min, nums2_right_min)) / 2
        else:
            return max(nums1_left_max, nums2_left_max)
