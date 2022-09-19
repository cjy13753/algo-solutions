// Time Complexity: O(n) where n is the number of nodes in the linked list
// Runtime: 156 ms, faster than 51.98% of C# online submissions for Linked List Cycle.

// Space Complexity: O(1)
// Memory Usage: 41.2 MB, less than 77.56% of C# online submissions for Linked List Cycle.

/* Thought process memo
brute force approach:
save every node in a data structure and check if a node is already saved in the data structure.
How do you determine if the data structure contains a node?
By comparing the memory address of each node.
TC: O(n), SC: O(n)

But can we improve the SC?

what if we use two pointers?
one pointer starts iterating through the linked list,
and when the first node reaches the second node, the next pointer starts iterating through the linked list.

if the first pointer reaches a null, then there is no cycle in the linked list.
but if there is a cycle in the list, the second pointer will be caught by the first pointer.
but here's what's important. The first pointer should move faster than the second pointer. Otherwise, the first pointer would never catch up with the second pointer.

let me describe the thought process I explained in a more logical way so that I can code based off it.

edge case: if there is less than or equal to one node in the linked list, there is not cycle.
declare two pointers, the fast pointer, and the slow pointer.
declare and initialize a dummy node in front of the head, so that the two pointers can start from the dummy node instead of the head. this is a little trick to make the logic more understandable
first pointer starts from the head and for its turn, jump twice.
if there is no next node, or if the node that it jumps twice to is a null node, there is no cycle.
slow pointer starts fromt he head node as well, and it jumps just once.

the fast pointer and the slow pointer take turns, and whenever the fast pointer moves, it checks if it points to the same node as the slow pointer
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
        if (head is null)
        {
            return false;
        }
        
        if (head.next is null)
        {
            return false;
        }
        
        var dummy = new ListNode(0);
        dummy.next = head;
        
        var fast = dummy;
        var slow = dummy;
        
        while (true)
        {
            if (fast.next is null || fast.next.next is null)
            {
                return false;
            }
            
            fast = fast.next.next;
            
            if (fast == slow)
            {
                break;
            }
            
            slow = slow.next;
        }
        
        return true;
    }
}