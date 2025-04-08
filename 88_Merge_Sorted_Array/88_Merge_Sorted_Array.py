__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_m, ptr_n = m - 1, n - 1
        ptr = m + n - 1

        while ptr_n >= 0:
            if ptr_m >= 0 and nums1[ptr_m] > nums2[ptr_n]:
                nums1[ptr] = nums1[ptr_m]
                ptr_m -= 1
            else:
                nums1[ptr] = nums2[ptr_n]
                ptr_n -= 1
            ptr -= 1
        # return is not required
