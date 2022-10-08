// Time Complexity: O(V + E) where V is the total number of vertices and E is the total number of Edges in the tree
// Runtime: 161 ms, faster than 45.99% of C# online submissions for Symmetric Tree.

// Space Complexity: O(V) where V is the total number of vertices
// Memory Usage: 39.1 MB, less than 84.38% of C# online submissions for Symmetric Tree.

/*
do a breeadth first search.
Add one more information, which is the depth of each node.
within the same depth, find out if the values are palindrome.

level to investigate: 2
2, 2 -> palindrome
put all of their children nodes in the queue.
update the the level to investigate by plus 1.
data structure
class wrapper {
    TreeNode node;
    int depth;
}

before while loop
nullValue = -101;
queue: root's left child and right child with depth of 1
levelToInvestigate

while loop until no nodes to pop from the queue
    List of values 
    while the folloowing is true: peek to see if the next node to pop from the queue has the same depth as levelToInvestigate
        extract the value and store it in the list of values. if the node is null, store nullValue predefined.
    figure out if the list of values has a palindrome elements

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
    public bool IsSymmetric(TreeNode root) {
        var nullValue = -101;
        var levelToInvestigate = 1;

        var queue = new Queue<Wrapper>();
        queue.Enqueue(new Wrapper(root.left, levelToInvestigate));
        queue.Enqueue(new Wrapper(root.right, levelToInvestigate));
        
        while (queue.Count > 0)
        {
            var list = new List<int>();
            
            while (queue.Count > 0)
            {
                
                var wrapper = queue.Peek();
                var node = wrapper.node;
                var depth = wrapper.depth;
                if (depth != levelToInvestigate)
                {
                    break;
                }
                
                wrapper = queue.Dequeue();
                node = wrapper.node;
                depth = wrapper.depth;
                
                if (node is not null)
                {
                    queue.Enqueue(new Wrapper(node.left, levelToInvestigate + 1));
                    queue.Enqueue(new Wrapper(node.right, levelToInvestigate + 1));
                }
                
                list.Add(node?.val ?? nullValue);
            }
            
            var array = list.ToArray();
            var start = 0;
            var end = array.Length - 1;
            
            while (start < end)
            {
                if (array[start] != array[end])
                {
                    return false;
                }
                start++;
                end--;
            }
            
            levelToInvestigate++;
        }
        
        return true;
    }
    
    private class Wrapper
    {
        public TreeNode node;
        public int depth;
        
        public Wrapper(TreeNode node, int depth)
        {
            this.node = node;
            this.depth = depth;
        }
    }
}