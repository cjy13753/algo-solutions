// Time Complexity: O(V) where V is the number of verties in the given binary tree
// Space Complexity: O(V) where V is the number of verties in the given binary tree

/*
create a gloabl queue
create a local queue
create a global list
while global queue is not empty
    while global queue is not empty
        pop every node left in the global queue and put them in local queue
    create a new local list
    while local queue is not empty
        pop node from local queue, and extract value from the popped node, and put its left and right children to the global queue
    Add the local list to the global list
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
    public IList<IList<int>> LevelOrder(TreeNode root) {
        if (root == null)
        {
            return new List<IList<int>>();
        }
        var globalQueue = new Queue<TreeNode>();
        var localQueue = new Queue<TreeNode>();
        IList<IList<int>> globalList = new List<IList<int>>();
        
        globalQueue.Enqueue(root);
        
        while (globalQueue.Count > 0)
        {
            while (globalQueue.Count > 0)
            {
                var poppedNode = globalQueue.Dequeue();
                localQueue.Enqueue(poppedNode);
            }
            
            IList<int> localList = new List<int>();
            
            while (localQueue.Count > 0)
            {
                var poppedNode = localQueue.Dequeue();
                localList.Add(poppedNode.val);
                if (poppedNode.left != null)
                {
                    globalQueue.Enqueue(poppedNode.left);
                }
                if (poppedNode.right != null)
                {
                    globalQueue.Enqueue(poppedNode.right);
                }
            }
            
            globalList.Add(localList);
        }

        return globalList;
    }
}