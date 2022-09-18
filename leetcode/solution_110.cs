// Wrong answer

public class Solution {
    public bool IsBalanced(TreeNode root) {
        if (root is null)
        {
            return true;
        }
        
        var highestHeight = 0;
        var lowestHeight = 5000;
        
        var stack = new Stack<Container>();
        stack.Push(new Container(root, 1));
        
        while (stack.Count != 0)
        {
            var container = stack.Pop();
            var node = container.node;
            var height = container.height;
            
            if (node.left is null && node.right is null)
            {
                highestHeight = Math.Max(highestHeight, height);
                lowestHeight = Math.Min(lowestHeight, height);
                continue;
            }
            
            if (node.left is null )
            {
                lowestHeight = Math.Min(lowestHeight, height);
                stack.Push(new Container(node.right, height + 1));
                continue;
            }
            
            if (node.right is null)
            {
                lowestHeight = Math.Min(lowestHeight, height);
                stack.Push(new Container(node.left, height + 1));
                continue;
            }
            
            stack.Push(new Container(node.right, height + 1));
            stack.Push(new Container(node.left, height + 1));
        }
        
        return highestHeight - lowestHeight <= 1 ? true : false;
    }
}

public class Container
{
    public TreeNode node;
    public int height;
    public Container(TreeNode node, int height)
    {
        this.node = node;
        this.height = height;
    }
}