// Time Complexity: O(n) where n is the number of nodes in the linked list
// Runtime: 134 ms, faster than 43.14% of C# online submissions for Middle of the Linked List.

// Space Complexity: O(1)
// Memory Usage: 36.5 MB, less than 80.80% of C# online submissions for Middle of the Linked List.


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
    public ListNode MiddleNode(ListNode head) {
        var dummy = new ListNode();
        dummy.next = head;
        
        var slow = dummy;
        var fast = dummy;
        
        while (fast.next is not null && fast.next.next is not null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow.next;
        
    }
}