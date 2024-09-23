/**
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

#define max(a, b) ((a > b) ? a : b)

int lengthOfLongestSubstring(char* s) {
    int max_s = 0;
    int len = strlen(s);
    int hash[128] = {0};  // ASCII

    for (int left = 0, right = 0; right < len; right++) {
        left = max(left, hash[s[right]]);
        max_s = max(max_s, right - left + 1);
        hash[s[right]] = right + 1;
    }

    return max_s;
}