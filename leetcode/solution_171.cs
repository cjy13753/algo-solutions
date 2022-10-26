// Time Complexity: O(n) where n is the number of characters in a given string
// Runtime: 108 ms, faster than 53.65% of C# online submissions for Excel Sheet Column Number.

// Space Complexity: O(1)
// Memory Usage: 36.9 MB, less than 38.28% of C# online submissions for Excel Sheet Column Number.

/*
A = 1
Z = 26

AA = 26 + 1
AZ = 26 + 26

BA = 26 + 26 + 1
BZ = 26 + 26 + 26

AAA = 

how about we think of this as base 26 number?
How can we convert the uppercase English letter to a corresponding integer without using a hash table?
ASCII English uppercase letter has a corresponding number. we can convert a ASCII character to a corresponding integer, and subtract integer-converted ASCII 'A' from it and plus 1.
*/


public class Solution {
    public int TitleToNumber(string columnTitle) {
        var A = (int) 'A';
        var sum = 0;
        var count = 0;
        
        for (var i = columnTitle.Length - 1; i >= 0; i--)
        {
            var letter = (int) columnTitle[i];
            var temp = 0;
            var num = (letter - A + 1) * ((int)Math.Pow(26, count++));
            sum += num;
        }

        return sum;
    }
}