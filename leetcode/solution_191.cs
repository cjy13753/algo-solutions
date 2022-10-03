// Time Complexity: O(logn) where n is the given unsigned integer
// Runtime: 23 ms, faster than 91.81% of C# online submissions for Number of 1 Bits.

// Space Complexity: O(1)
// Memory Usage: 23.6 MB, less than 13.58% of C# online submissions for Number of 1 Bits.


public class Solution {
    public int HammingWeight(uint n) {
        var count = 0u;
        var dividend = n;
        
        while (dividend > 0)
        {
            count += dividend % 2u;
            dividend /= 2u;
        }
        
        return (int)count;
    }
}