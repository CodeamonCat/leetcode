/**
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* current = dummy;
    int carry = 0;

    while(l1 != NULL || l2 != NULL || carry != 0){
        int l1_val = (l1 == NULL) ? 0 : l1->val;
        int l2_val = (l2 == NULL) ? 0 : l2->val;
        int sum = l1_val + l2_val + carry;
        carry = sum / 10;

        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = NULL;
        current->next = node;
        current = current->next;

        l1 = (l1 == NULL) ? NULL : l1->next;
        l2 = (l2 == NULL) ? NULL : l2->next;
    }
    
    return dummy->next;
}