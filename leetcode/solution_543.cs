// Time Complexity: O(n) where n is the number of nodes in a binary tree
// Runtime: 150 ms, faster than 40.71% of C# online submissions for Diameter of Binary Tree.

// Space Complexity: O(1)
// Memory Usage: 38.4 MB, less than 36.97% of C# online submissions for Diameter of Binary Tree.

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
    private int diameter = 0;
    
    public int DiameterOfBinaryTree(TreeNode root) {
        SetDiameter(root);
        
        return diameter;
    }
    
    private int SetDiameter(TreeNode node)
    {
        if (node is null)
        {
            return 0;
        }
        
        var left = SetDiameter(node.left);
        var right = SetDiameter(node.right);
        
        var sum = left + right;
        
        diameter = Math.Max(diameter, sum);
        
        return Math.Max(left, right) + 1;
    }
}