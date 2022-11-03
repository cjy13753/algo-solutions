// Time Complexity: O(n) where n is the length of the given string
// Space Complexity: O(n) where n is the length of the given string


public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var start = 0;
        var end = 0;
        var localLength = 0;
        var globalLength = 0;
        var hashMap = new Dictionary<char, int>();
        
        while (end < s.Length)
        {
            var c = s[end];
            if (hashMap.TryGetValue(c, out int index) && index != -1)
            {
                globalLength = Math.Max(globalLength, localLength);
                localLength = 0;
                while (start < end)
                {
                    hashMap[s[start]] = -1;
                    start++;
                }
                start = index + 1;
                end = start;
                continue;
            }
            
            hashMap[c] = end;
            localLength++;
            end++;
        }
        
        return Math.Max(globalLength, localLength);
    }
}