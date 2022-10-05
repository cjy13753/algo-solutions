// Time Complexity: O(n) where n is the number of nodes in the give linked list
// Runtime: 501 ms, faster than 20.06% of C# online submissions for Palindrome Linked List.

// Space Complexity: O(n) where n is the number of nodes in the give linked list
// Memory Usage: 53.5 MB, less than 48.17% of C# online submissions for Palindrome Linked List.


/*

brute-force approach
store every value in the singly linked list in a separate array, and determine if it's palindrome using two pointerser, one from the start and another from the end of the array.
TC: O(n), SC: O(n)

ex) thought experiment
1, 2, 3, 4, 5, 6, 4, 6, 5, 4, 3, 2, 1 : it's palindrom
slow and fast pointers?

*/


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
    public bool IsPalindrome(ListNode head) {
        var container = new List<int>();
        var pointer = head;
        while (pointer is not null)
        {
            container.Add(pointer.val);
            pointer = pointer.next;
        }
        
        var array = container.ToArray();
        var start = 0;
        var end = array.Length - 1;
        
        while (start <= end)
        {
            if (array[start] != array[end])
            {
                return false;
            }
            start += 1;
            end -= 1;
        }
        
        return true;
    }
}