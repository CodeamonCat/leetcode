/*
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

class Solution {
	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		if (nums1.length > nums2.length) {
			return findMedianSortedArrays(nums2, nums1);
		}
		int low = 0;
		int high = nums1.length;

		while (low <= high) {
			int partitionNums1 = (low + high) / 2;
			int partitionNums2 = (nums1.length + nums2.length + 1) / 2 - partitionNums1;

			int maxLeftNums1 = (partitionNums1 == 0) ? Integer.MIN_VALUE : nums1[partitionNums1 - 1];
			int minRightNums1 = (partitionNums1 == nums1.length) ? Integer.MAX_VALUE : nums1[partitionNums1];

			int maxLeftNums2 = (partitionNums2 == 0) ? Integer.MIN_VALUE : nums2[partitionNums2 - 1];
			int minRightNums2 = (partitionNums2 == nums2.length) ? Integer.MAX_VALUE : nums2[partitionNums2];

			if (maxLeftNums1 <= minRightNums2 && maxLeftNums2 <= minRightNums1) {
				if ((nums1.length + nums2.length) % 2 == 0) {
					return ((double) Math.max(maxLeftNums1, maxLeftNums2) + Math.min(minRightNums1, minRightNums2)) / 2;
				} else {
					return (double) Math.max(maxLeftNums1, maxLeftNums2);
				}
			} else if (maxLeftNums1 > minRightNums2) {
				high = partitionNums1 - 1;
			} else {
				low = partitionNums1 + 1;
			}
		}
		return 0;
	}
}
