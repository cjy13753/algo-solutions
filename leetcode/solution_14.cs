// Time Complexity: O(n * m) where n is the number of strings in the array and m is the length of the shortest string.
// Runtime: 106 ms, faster than 89.10% of C# online submissions for Longest Common Prefix.

// Space Complexity: O(1)
// Memory Usage: 39.7 MB, less than 24.41% of C# online submissions for Longest Common Prefix.


/*
Access the same position of every word in the given array of strings.
Move to the next position for every string for each turn.

How do you figure out a point when you can no more iterate through each string because the index boundary is going to be exceeded?
*/


public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int i = 0;
        var flag = false;
        
        while (true)
        {
            char letter = '0';
            
            foreach (var str in strs)
            {
                if (i >= str.Length)
                {
                    flag = true;
                    break;
                }
                
                if (letter == '0')
                {
                    letter = str[i];
                    continue;
                }
                
                if (letter != str[i])
                {
                    flag = true;
                    break;
                }
            }
            
            if (flag)
            {
                break;
            }
            
            i++;
        }
        
        var prefixLength = i;
        return strs[0].Substring(0, i);
    }
}