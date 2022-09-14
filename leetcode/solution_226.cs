// Time Complexity: O(n) where n is the number of nodes in the binary tree because you need to consider only the number of times you enqueue and dequeue the nodes 
// and you can only enqueue and dequeue a node at maximum once.
// Runtime: 141 ms, faster than 33.22% of C# online submissions for Invert Binary Tree.

// Space Complexity: O(n) when the given binary tree is a perfect binary tree.
// Memory Usage: 36.6 MB, less than 96.33% of C# online submissions for Invert Binary Tree.

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
    public TreeNode InvertTree(TreeNode root) {
        if (root is null)
        {
            return root;
        }
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while (queue.Count != 0)
        {
            var popped = queue.Dequeue();
            
            var leftChild = popped.left;
            var rightChild = popped.right;
            
            popped.left = rightChild;
            popped.right = leftChild;
            
            if (leftChild is not null)
            {
                queue.Enqueue(leftChild);
            }
            
            if (rightChild is not null)
            {
                queue.Enqueue(rightChild);
            }
        }
        
        return root;
    }
}