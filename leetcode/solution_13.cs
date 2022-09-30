// Time Complexity: O(n) where n is the number of charaters in a given string
// Runtime: 141 ms, faster than 20.05% of C# online submissions for Roman to Integer.

// Space Complexity: O(1)
// Memory Usage: 36.9 MB, less than 61.74% of C# online submissions for Roman to Integer.

public class Solution {
    public int RomanToInt(string s) {
        var result = 0;
        var pair = new Dictionary<char, List<char>>(){{'I', new List<char>{'V', 'X'}}, {'X', new List<char>{'L', 'C'}}, {'C', new List<char>{'D', 'M'}}};
        var table = new Dictionary<char, int>(){{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        
        
        int i = 0;
        while (i < s.Length)
        {
            var roman = s[i];
            if (pair.ContainsKey(roman))
            {
                var target = pair[roman];
                if (i + 1 < s.Length && target.Contains(s[i+1]))
                {
                    var cal = table[s[i + 1]] - table[roman];
                    result += cal;
                    i += 2;
                    continue;
                }
                
            }
            result += table[roman];
            i += 1;
        }
        
        return result;
    }
}