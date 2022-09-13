// Time Complexity: O(n)
// Runtime: 139 ms, faster than 34.57% of C# online submissions for Valid Palindrome.

// Space Complexity: O(1)
// Memory Usage: 38.3 MB, less than 94.84% of C# online submissions for Valid Palindrome.

public class Solution {
    public bool IsPalindrome(string s) {
        if (s.Length < 2)
        {
            return true;
        }
        
        var forward = 0;
        var backward = s.Length - 1;
        
        while (forward < backward)
        {
            var fLetter = s[forward];
            var bLetter = s[backward];
            
            if (!Char.IsLetterOrDigit(fLetter))
            {
                forward++;
                continue;
            }
            
            if (!Char.IsLetterOrDigit(bLetter))
            {
                backward--;
                continue;
            }
            
            if (Char.IsLetter(fLetter))
            {
                fLetter = Char.ToLower(fLetter);
            }
            
            if (Char.IsLetter(bLetter))
            {
                bLetter = Char.ToLower(bLetter);
            }
            
            if (fLetter != bLetter)
            {
                return false;
            }
            
            forward++;
            backward--;
        }
        
        return true;
    }
}