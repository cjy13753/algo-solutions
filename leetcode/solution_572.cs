// Time Complexity: O(V^2) where V is the number of vertices in the given tree in the case where a huge root tree and a huge subtree has almost the same structure except for a single leaf node
// Runtime: 194 ms, faster than 46.14% of C# online submissions for Subtree of Another Tree.

// Space Complexity: O(V)
// Memory Usage: 41.2 MB, less than 55.22% of C# online submissions for Subtree of Another Tree.

/*

apply bfs on the root tree so that you put every node that holds the same value as subRoot in a queue.
do a while loop:
    you pop out a node from the queue and validate if the subtree starting from the popped node is the same as subroot tree
if you reach here, return false

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
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        var queue = new Queue<TreeNode>();
        
        queue.Enqueue(root);
        
        while (queue.Count > 0)
        {
            var popped = queue.Dequeue();
            
            if (Validate(popped, subRoot))
            {
                return true;
            }
            
            if (popped.left is not null)
            {
                queue.Enqueue(popped.left);
            }
            
            if (popped.right is not null)
            {
                queue.Enqueue(popped.right);
            }
            
        }
                              
      return false;
        
    }
    
    private bool Validate(TreeNode root, TreeNode subRoot)
    {
        if (root is not null && subRoot is not null && root.val != subRoot.val)
        {
            return false;
        }
        
        if (root is null && subRoot is not null)
        {
            return false;
        }
        
        if (subRoot is null && root is not null)
        {
            return false;
        }
        
        if (root is null && subRoot is null)
        {
            return true;
        }
        
        if (!Validate(root.left, subRoot.left))
        {
            return false;
        }
        
        if (!Validate(root.right, subRoot.right))
        {
            return false;
        }
        
        return true;
    }
}