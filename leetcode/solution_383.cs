// Time Complexity: O(n + m) where n is the number of characters in ransomNote and m is the number of characters in magazine
// Runtime: 139 ms, faster than 42.89% of C# online submissions for Ransom Note.

// Space Complexity: O(1) because ransomNote and magazine consist of lowercase English letters only.
// Memory Usage: 40.4 MB, less than 50.66% of C# online submissions for Ransom Note.

public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        if (ransomNote.Length > magazine.Length)
        {
            return false;
        }
        
        var dictionary = new Dictionary<char, int>();
        foreach (var c in magazine)
        {
            var count = dictionary.GetValueOrDefault(c);
            dictionary[c] = ++count;
        }
        
        foreach (var c in ransomNote)
        {
            var count = dictionary.GetValueOrDefault(c);
            if (count == 0)
            {
                return false;
            }
            dictionary[c] = --count;
        }
        
        return true;
    }
}