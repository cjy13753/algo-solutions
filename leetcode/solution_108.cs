// Time to solve: 28m30s

// Time Complexity: O(n) where n is the number of elements in the given array
// Runtime: 147 ms, faster than 42.69% of C# online submissions for Convert Sorted Array to Binary Search Tree.

// Space Complexity: O(logn) because the maximum height of the tree to build is logn
// Memory Usage: 37.7 MB, less than 61.41% of C# online submissions for Convert Sorted Array to Binary Search Tree.

/*
recursive approach

given (cur, left range, right range)

if left range is not empty:
    mid number = mid number in the left range
    cur.left = new TreeNode(mid number);
    recur(cur.left, left's left, left's right)
if right range is not empty:
    mid number = mid number in the right range
    recur(cur.right, right's left, right's right)
*/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode SortedArrayToBST(int[] nums) {
        var startIndex = 0;
        var endIndex = nums.Length - 1;
        var midIndex = endIndex / 2;
        var head = new TreeNode(nums[midIndex]);
        
        dfs(head, nums, 0, midIndex - 1, midIndex + 1, endIndex);
        
        return head;
    }
    
    public void dfs(TreeNode cur, int[] nums, int leftStart, int leftEnd, int rightStart, int rightEnd)
    {
        if (leftStart <= leftEnd)
        {
            var startIndex = leftStart;
            var endIndex = leftEnd;
            var midIndex = leftStart + (leftEnd - leftStart) / 2;
            cur.left = new TreeNode(nums[midIndex]);
            dfs(cur.left, nums, leftStart, midIndex - 1, midIndex + 1, leftEnd);
        }
        
        if (rightStart <= rightEnd)
        {
            var startIndex = rightStart;
            var endIndex = rightEnd;
            var midIndex = rightStart + (rightEnd - rightStart) / 2;
            cur.right = new TreeNode(nums[midIndex]);
            dfs(cur.right, nums, rightStart, midIndex - 1, midIndex + 1, rightEnd);
        }
    }
}