// Time Complexity: O(h) where h is the height of the binary search tree
// Runtime: 182 ms, faster than 27.58% of C# online submissions for Lowest Common Ancestor of a Binary Search Tree.

// Space Complexity: O(1)
// Memory Usage: 41.4 MB, less than 97.39% of C# online submissions for Lowest Common Ancestor of a Binary Search Tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        var pointer = root;
        
        while (true)
        {
            int pDecider;
            int qDecider;
            
            var pDifference = p.val - pointer.val;
            if (pDifference > 0)
            {
                pDecider = 1;   
            }
            else if (pDifference == 0)
            {
                pDecider = 0;
            }
            else
            {
                pDecider = -1;
            }
            
            var qDifference = q.val - pointer.val;
            if (qDifference > 0)
            {
                qDecider = 1;   
            }
            else if (qDifference == 0)
            {
                qDecider = 0;
            }
            else
            {
                qDecider = -1;
            }
            
            var decider = pDecider * qDecider;
            
            if (decider == 0 || decider < 0)
            {
                break;
            }
            
            if (pDecider > 0)
            {
                pointer = pointer.right;
                continue;
            }
            
            if (pDecider < 0)
            {
                pointer = pointer.left;
                continue;
            }
        }
        
        return pointer;
    }
}