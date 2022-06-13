//Runtime: 140 ms, faster than 93.36 % of C# online submissions for Binary Tree Inorder Traversal.
//Memory Usage: 42.4 MB, less than 6.59 % of C# online submissions for Binary Tree Inorder Traversal.
 
 public class TreeNode {
     public int val;
     public TreeNode left;
     public TreeNode right;
     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

public class Solution {
    static void Main()
	{
		TreeNode root = new TreeNode(1);
		root.left = null;
		root.right = new TreeNode(2);
		root.right.left = new TreeNode(3);
		
		new Solution().InorderTraversal(root).Dump();
	}
	
	public IList<int> InorderTraversal(TreeNode root)
	{
		var ans = new List<int> {};
				
		Recur(root, ans);
		
		return ans;
	}
	
	private static void Recur(TreeNode root, List<int> content)
	{
		if (root == null) {
			return;
		}
		
		Recur(root.left, content);
		content.Add(root.val);
		Recur(root.right, content);
	}
}
