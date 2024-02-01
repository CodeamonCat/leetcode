/**
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(*returnSize * sizeof(int));

    // create hashtable structure
    int lucky_number = 1126;
    unsigned hashtable_size = numsSize * 2;
    typedef struct hashtable {
        int value;
        unsigned int index;
        bool filled;
    } Hashtable;
    Hashtable table[hashtable_size];
    memset(table, 0, sizeof(table));

    for (unsigned int index = 0; index < numsSize; index++) {
        int complement = target - nums[index];
        unsigned int hashvalue =
            (unsigned int)complement * lucky_number % hashtable_size;

        // find matched hashvalue in table
        while (table[hashvalue].filled) {
            if (table[hashvalue].value == complement &&
                table[hashvalue].index != index) {
                result[0] = table[hashvalue].index;
                result[1] = index;
                return result;
            }
            hashvalue++;
            if (hashvalue == hashtable_size) {
                hashvalue = 0;
            }
        }

        // insert hashvalue in table with linear probe
        hashvalue = (unsigned int)nums[index] * lucky_number % hashtable_size;
        while (table[hashvalue].filled) {
            hashvalue++;
            if (hashvalue == hashtable_size) {
                hashvalue = 0;
            }
        }

        table[hashvalue].value = nums[index];
        table[hashvalue].index = index;
        table[hashvalue].filled = true;
    }

    *returnSize = 0;
    return NULL;
}