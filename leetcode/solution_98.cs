/*
left subtree root key is less than root
right subtree root key is bigger than root

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
    public bool IsValidBST(TreeNode root) {
        if (!IsLeftSubTreeBST(root.left, root.val, root.val))
        {
            return false;
        }

        return IsRightSubTreeBST(root.right, root.val, root.val);
    }

    private bool IsLeftSubTreeBST(TreeNode root, int parent, int greatParent)
    {
        if (root == null)
        {
            return true;
        }

        if (root.val >= parent)
        {
            return false;
        }

        if (root.val >= greatParent)
        {
            return false;
        }

        if (!IsLeftSubTreeBST(root.left, root.val, parent))
        {
            return false;
        }

        return IsRightSubTreeBST(root.right, root.val, parent);
    }

    private bool IsRightSubTreeBST(TreeNode root, int parent, int greatParent)
    {
        if (root == null)
        {
            return true;
        }

        if (parent >= root.val)
        {
            return false;
        }

        if (greatParent >= root.val)
        {
            return false;
        }

        if (!IsLeftSubTreeBST(root.left, root.val, parent))
        {
            return false;
        }

        return IsRightSubTreeBST(root.right, root.val, parent);
    }
}