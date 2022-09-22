// Time Complexity: O(n) where n is the steps it takes to reach the top
// Runtime: 50 ms, faster than 7.79% of C# online submissions for Climbing Stairs.

// Space Complexity: O(1)
// Memory Usage: 24.9 MB, less than 95.05% of C# online submissions for Climbing Stairs.

public class Solution {
    public int ClimbStairs(int n) {
        
        if (n < 2)
        {
            return 1;
        }
        
        var twoAhead = 1;
        var oneAhead = 1;
        var result = 2;
        
        var curPos = 2;
        
        while (curPos < n)
        {
            curPos++;
            twoAhead = oneAhead;
            oneAhead = result;
            result = twoAhead + oneAhead;
        }
        
        return result;
    }
}