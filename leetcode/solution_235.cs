// Time Complexity: O(h) where h is the height of the binary search tree
// Runtime: 105 ms, faster than 97.48% of C# online submissions for Lowest Common Ancestor of a Binary Search Tree.

// Space Complexity: O(1)
// Memory Usage: 46 MB, less than 10.44% of C# online submissions for Lowest Common Ancestor of a Binary Search Tree.

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
            if (p.val > pointer.val && q.val > pointer.val)
            {
                pointer = pointer.right;
                continue;
            }
            
            if (p.val < pointer.val && q.val < pointer.val)
            {
                pointer = pointer.left;
                continue;
            }
            
            break;
        }
        
        return pointer;
    }
}