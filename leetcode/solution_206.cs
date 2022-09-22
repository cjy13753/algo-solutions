// Time Complexity: O(n) where n is the number of nodes in the linked list
// Runtime: 88 ms, faster than 93.21% of C# online submissions for Reverse Linked List.

// Space Complexity: O(1)
// Memory Usage: 39.1 MB, less than 6.51% of C# online submissions for Reverse Linked List.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head is null)
        {
            return head;
        }
        ListNode prev = null;
        var cur = head;
        while (cur is not null)
        {
            var next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}