/*
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

class Solution {
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> hashtable = new HashMap<>();
    for (int index = 0; index < nums.length; index++) {
      int complement = target - nums[index];
      if (hashtable.containsKey(complement)) {
        return new int[] {hashtable.get(complement), index};
      }
      hashtable.put(nums[index], index);
    }
    return new int[] {};
  }
}
