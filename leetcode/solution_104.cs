// Time Complexity: O(n) where n is the number of nodes in the give binary tree
// Runtime: 155 ms, faster than 30.82% of C# online submissions for Maximum Depth of Binary Tree.

// Space Complexity: O(h) where h is the height of the given tree because recursive approach takes up the call stack
// Memory Usage: 37.6 MB, less than 95.56% of C# online submissions for Maximum Depth of Binary Tree.

/*
approach

brute force
recursively move down the tree to reach every leaf node.
when you reach the leaf node, start climbing back up the tree. In the meanwhile, the child node needs to return how many descendent nodes it had plus itself to its parent node. the parent node who gets node counts from its left subtree and right subtree, and return to its own parent the bigger count plus itself.
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
    public int MaxDepth(TreeNode root) {
        if (root is null)
        {
            return 0;
        }
        
        var left = MaxDepth(root.left);
        var right = MaxDepth(root.right);
        
        var result = Math.Max(left, right) + 1;
        
        return result;
    }
}