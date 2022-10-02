// Time Complexity: O(min(n, m)) where n and m are the number of nodes in the given trees respectively.
// Runtime: 149 ms, faster than 51.42% of C# online submissions for Same Tree.

// Space Complexity: O(min(n, m))
// Memory Usage: 38.9 MB, less than 19.01% of C# online submissions for Same Tree.

/*
brute force approach
I want to do a breadth first search on both trees simultaneously, but I cannot figure out a way to do that.
prepare two pointers, one pointing to a node in the p tree, and another pointing to a node in the q tree.
I will also prepare two queues for both trees for bfs.
we are going to do a while loop until either queue is empty.

inside the loop
pop from both queues, find if the pointers are pointing to the "same" node.
push the left and right childern for both trees.


outside the loop
if both queues are empty, see if the pointers are the same. if same, return true, false otherwise.
otherwise, return false
*/

/*
brute force approach
I want to do a breadth first search on both trees simultaneously, but I cannot figure out a way to do that.
prepare two pointers, one pointing to a node in the p tree, and another pointing to a node in the q tree.
I will also prepare two queues for both trees for bfs.
we are going to do a while loop until either queue is empty.

inside the loop
pop from both queues, find if the pointers are pointing to the "same" node.
push the left and right childern for both trees.


outside the loop
if both queues are empty, see if the pointers are the same. if same, return true, false otherwise.
otherwise, return false
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
    public bool IsSameTree(TreeNode p, TreeNode q) {
        var queue = new Queue<TreeNode>();
        
        queue.Enqueue(p);
        queue.Enqueue(q);
        
        while (queue.Count() > 1)
        {
            var pPopped = queue.Dequeue();
            var qPopped = queue.Dequeue();
            
            if (pPopped is null && qPopped is null)
            {
                continue;
            }
            
            if (pPopped is not null && qPopped is not null && pPopped.val == qPopped.val)
            {
                    queue.Enqueue(pPopped.left);
                    queue.Enqueue(qPopped.left);
                    queue.Enqueue(pPopped.right);
                    queue.Enqueue(qPopped.right);
                    continue;
            }
            
            return false;
        }
        
        return queue.Count == 0;
    }
}