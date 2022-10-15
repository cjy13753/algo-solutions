// Time Complexity: O(n) where n is the number of elements in the given array
// Runtime: 252 ms, faster than 48.91% of C# online submissions for Remove Duplicates from Sorted Array.

// Space Complexity: O(1)
// Memory Usage: 44.9 MB, less than 48.67% of C# online submissions for Remove Duplicates from Sorted Array.


public class Solution {
    public int RemoveDuplicates(int[] nums) {
        var indexToFill = 1;
        var pointer = 1;
        var prev = nums[0];
        
        while (pointer < nums.Length)
        {
            if (nums[pointer] == prev)
            {
                pointer++;
            }
            else
            {
                nums[indexToFill] = nums[pointer];
                prev = nums[indexToFill];
                indexToFill++;
                pointer++;
                
            }
        }
        
        return indexToFill;
        
    }
}