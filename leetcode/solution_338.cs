// Time Complexity: O(nlogn) where n is the given integer because you have to iterate n times and for each iteration, you need to do division by 2 at most logn times
// Runtime: 196 ms, faster than 13.54% of C# online submissions for Counting Bits.

// Space Complexity: O(1)
// Memory Usage: 38.4 MB, less than 48.66% of C# online submissions for Counting Bits.

public class Solution {
    public int[] CountBits(int n) {
        var ans = new int[n+1];
        
        for (int i = 0; i < n + 1; i++)
        {
            var count = 0;
            var divdend = i;
            
            while (divdend > 0)
            {
                count += divdend % 2;
                divdend = divdend / 2;
            }
            
            ans[i] = count;
        }
        
        return ans;
        
    }
}