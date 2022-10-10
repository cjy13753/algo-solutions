// Time Complexity: O(logn) where n is the given integer
// Runtime: 86 ms, faster than 43.43% of C# online submissions for Palindrome Number.

// Space Complexity: O(logn) where n is the given integer
// Memory Usage: 29.4 MB, less than 25.67% of C# online submissions for Palindrome Number.

/*
Requirements:
- solve it without converting the integer into string

approach
idea 1: remainder
121 = 12 * 10 + 1
12 = 1 * 10 + 2
1 = 0 * 10 + 1
0 = end
we get, {1, 2, 1}
then use double pointers to traverse from start to end and end to start.
TC: O(logn), SC: O(logn)
*/

public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0)
        {
            return false;
        }
        var store = new List<int>();
        
        while (x != 0)
        {
            store.Add(x % 10);
            x = x / 10;
        }
        
        var start = 0;
        var end = store.Count - 1;
        
        while (start < end)
        {
            if (store[start] == store[end])
            {
                start++;
                end--;
                continue;
            }
            return false;
        }
        
        return true;
    }
}