// Time Complexity: O(n) where n is the number of bits in the given unsigned integer
// Runtime: 29 ms, faster than 82.09% of C# online submissions for Reverse Bits.

// Space Complexity: O(1)
// Memory Usage: 22.7 MB, less than 57.05% of C# online submissions for Reverse Bits.

/*

identify the lsb of n and put it to the result variable's least lsb.
apply bitwise right shift operator on n by 1 and bitwise left shift operator on the result variable by 1.
DO the same 32 times.

*/

public class Solution {
    public uint reverseBits(uint n) {
        var result = 0u;
        
        for (int i = 0; i < 32; i++)
        {
            result <<= 1;
            var lsb = n & 1;
            result += lsb;
            n >>= 1;
        }
        
        return result;
    }
}