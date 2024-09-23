/*
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

class Solution {
  public int lengthOfLongestSubstring(String s) {
    int max_s = 0;
    HashMap<Character, Integer> hashtable = new HashMap<>();

    for (int left = 0, right = 0; right < s.length(); right++) {
      if (hashtable.containsKey(s.charAt(right))) {
        left = Math.max(left, hashtable.get(s.charAt(right)));
      }
      max_s = Math.max(max_s, right - left + 1);
      hashtable.put(s.charAt(right), right + 1);
    }

    return max_s;
  }
}
