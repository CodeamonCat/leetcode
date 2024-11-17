/**
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2,
                              int nums2Size) {
    // nums1Size <= nums2Size is required
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }

    int median = (nums1Size + nums2Size + 1) / 2;
    int left = 0;
    int right = nums1Size;

    while (left < right) {
        int mid = left + (right - left) / 2;
        int mid2 = median - mid;

        if (nums1[mid] < nums2[mid2 - 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    int mid = left;
    int mid2 = median - left;

    int nums1_left_max = mid == 0 ? INT_MIN : nums1[mid - 1];
    int nums2_left_max = mid2 == 0 ? INT_MIN : nums2[mid2 - 1];
    int nums1_right_min = mid == nums1Size ? INT_MAX : nums1[mid];
    int nums2_right_min = mid2 == nums2Size ? INT_MAX : nums2[mid2];

    if ((nums1Size + nums2Size) % 2 == 1) {
        return fmax(nums1_left_max, nums2_left_max);
    } else {
        return (fmax(nums1_left_max, nums2_left_max) +
                fmin(nums1_right_min, nums2_right_min)) /
               2.0;
    }
}
