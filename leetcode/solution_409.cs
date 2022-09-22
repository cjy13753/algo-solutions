// Time Complexity: O(n) where n is the number of characters in a given string
// Runtime: 97 ms, faster than 52.86% of C# online submissions for Longest Palindrome.

// Space Complexity: O(1) because the characters in a given string are limited to lowercase and uppercase English letters
// Memory Usage: 35 MB, less than 46.70% of C# online submissions for Longest Palindrome.

/*
approach

We don't need to keep the order of the given string.
In order to put a letter in a palindrome we are building, we need at least one pair of that letter.
Only one letter can be put into the palindrome without violating the invariant.

I wil keep three pieces of information.
1. result: integer variable that contains the length of the palindrome.
2. counter: dictionary that keeps track of each letter as a key and its count as a value.
3. remaining: integer variable that holds the number of letters that remain

algorithm
iterate through each character in the given string.
increase the remaining by 1
find the value in the dictionary whose key corresponds to the character.
if it is 1
 - deduct 1 from that value
 - increase the result by 2
 - deduct 2 from remaining
else
 - increase the value by 1
 - 

if the remaining is more than or equal to 1, increase result by 1
*/


public class Solution {
    public int LongestPalindrome(string s) {
        if (s.Length == 1)
        {
            return 1;
        }
        
        var result = 0;
        var counter = new Dictionary<char, int>();
        var remaining = 0;
        
        foreach (var c in s)
        {
            remaining++;
            
            var val = counter.GetValueOrDefault(c);
            if (val == 1)
            {
                counter[c] = 0;
                result += 2;
                remaining -= 2;
            }
            else
            {
                counter[c] = 1;
            }
        }
        
        if (remaining > 0)
        {
            result += 1;
        }
        
        return result;
    }
}