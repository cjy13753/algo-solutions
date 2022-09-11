// Time Complexity: O(n) where n is the number of all the nodes in the two given lists
// Runtime: 135 ms, faster than 41.48% of C# online submissions for Merge Two Sorted Lists.

// Space Complexity: O(1)
// Memory Usage: 37.5 MB, less than 99.51% of C# online submissions for Merge Two Sorted Lists.

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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        var dummy = new ListNode();
        var pointer = dummy;
        
        while (list1 is not null && list2 is not null)
        {
            if (list1.val <= list2.val)
            {
                pointer.next = list1;
                list1 = list1.next;
            }
            else
            {
                pointer.next = list2;
                list2 = list2.next;
            }
            pointer = pointer.next;
        }
        
        if (list1 is not null)
        {
            pointer.next = list1;
        }
        
        if (list2 is not null)
        {
            pointer.next = list2;
        }
        
        return dummy.next;
        
    }
}