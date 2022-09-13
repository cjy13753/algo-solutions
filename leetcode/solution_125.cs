// Time Complexity: O(n) where cleaning the string takes O(n) and comparing forward with backward takes O(n)
// Runtime: 142 ms, faster than 31.54% of C# online submissions for Valid Palindrome.

// Space Complexity: O(n) due to using string builder.
// Memory Usage: 38.6 MB, less than 73.19% of C# online submissions for Valid Palindrome.

public class Solution {
    public bool IsPalindrome(string s) {
        
        var cleanS = CleanseString(s);
        Console.WriteLine(cleanS);
        
        if (cleanS.Length < 2)
        {
            return true;
        }
        
        var forward = 0;
        var backward = cleanS.Length - 1;
        
        while (forward < backward)
        {
            if (cleanS[forward] != cleanS[backward])
            {
                return false;
            }
            
            forward++;
            backward--;
        }
        
        return true;
    }
    
    private string CleanseString(string s)
    {
        var sb = new StringBuilder();
        
        foreach (var c in s)
        {
            if (!Char.IsLetterOrDigit(c))
            {
                continue;
            }
            
            if (Char.IsNumber(c))
            {
                sb.Append(c);
                continue;
            }
            
            if (Char.IsUpper(c))
            {
                sb.Append(Char.ToLower(c));
                continue;
            }
            
            sb.Append(c);
        }
        
        return sb.ToString();
    }
}