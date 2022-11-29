// Time Complexity: O(n), where n is the number of elements in the given array
// Space Complexity: O(1), not accounting for the output array

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var res = Enumerable.Repeat(1, nums.Length).ToArray();
        
        var prefix = 1;
        for (int i = 0; i < nums.Length - 1; i++)
        {
            prefix *= nums[i];
            res[i + 1] *= prefix;
        }
            
            
        var postfix = 1;
        for (int i = nums.Length - 1; i > 0; i--)
        {
            postfix *= nums[i];
            res[i - 1] *= postfix;
        }
        
        return res;
    }
}