// Time Complexity: O(n + m) where n and m are the number of characters in s and t
// Runtime: 133 ms, faster than 20.23% of C# online submissions for Backspace String Compare.

// Space Complexity: O(n + m) where n and m are the number of characters in s and t
// Memory Usage: 37.2 MB, less than 36.68% of C# online submissions for Backspace String Compare.

public class Solution {
    public bool BackspaceCompare(string s, string t) {
        var sStack = new Stack<char>();
        var tStack = new Stack<char>();
        
        foreach (var c in s)
        {
            if (c == '#')
            {
                if (sStack.Count() > 0)
                {
                    sStack.Pop();
                }
            }
            else
            {
                sStack.Push(c);
            }
        }
        
        foreach (var c in t)
        {
            if (c == '#')
            {
                if (tStack.Count() > 0)
                {
                    tStack.Pop();
                }
            }
            else
            {
                tStack.Push(c);
            }
        }
        
        if (sStack.Count() == tStack.Count())
        {
            while (sStack.Count() != 0)
            {
                if (sStack.Pop() != tStack.Pop())
                {
                    return false;
                }
            }
            
            return true;
        }
        
        return false;
        
    }
}