// Time Complexity: O(n) where n is the sum of the numbers of characters in s and t
// Runtime: 133 ms, faster than 37.34% of C# online submissions for Valid Anagram.

// Space Complexity: O(1) because there are only a constant number of lowercase English letters
// Memory Usage: 38.2 MB, less than 98.82% of C# online submissions for Valid Anagram.

public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        {
            return false;
        }
        
        var sDict = new Dictionary<char, int>();
        foreach (var c in s)
        {
            var count = sDict.GetValueOrDefault(c);
            sDict[c] = ++count;
        }
        
        foreach (var c in t)
        {
            var count = sDict.GetValueOrDefault(c);
            if (count == 0)
            {
                return false;
            }
            sDict[c] = --count;
        }
        
        return true;
    }
}