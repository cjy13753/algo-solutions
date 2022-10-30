// Time Complexity: O(n), where n is the number of elements in the given array
// Space Complexity: O(1)


public class Solution {
    public int MaxSubArray(int[] nums) {
        var localMax = 0;
        var globalMax = nums[0];
        
        var front = 0;
        var end = 0;
        
        while (end < nums.Length)
        {
            localMax += nums[end];
            globalMax = Math.Max(globalMax, localMax);
            
            if (localMax <= 0)
            {
                front = end + 1;
                end = front;
                localMax = 0;
            }
            else
            {
                end++;
            }
        }
        
        return globalMax;
    }
}