// Time Complexity: O(logn) where n is the given integer n
// Runtime: 108 ms, faster than 40.16% of C# online submissions for Power of Three.

// Space Complexity: O(1)
// Memory Usage: 28.4 MB, less than 71.72% of C# online submissions for Power of Three.

public class Solution {
    public bool IsPowerOfThree(int n) {
        if (n <= 0)
        {
            return false;
        }
        
        while (n > 1)
        {
            if (n % 3 != 0)
            {
                return false;
            }
            
            n /= 3;
        }
        
        if (n % 3 == 1)
        {
            return true;
        }
        
        return false;
    }
}