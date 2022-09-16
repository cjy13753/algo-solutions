// Time Complexity: O(log n) using binary search
// Runtime: 144 ms, faster than 80.17% of C# online submissions for Binary Search.

// Space Complexity: O(1)
// Memory Usage: 51.1 MB, less than 5.69% of C# online submissions for Binary Search.


public class Solution {
    public int Search(int[] nums, int target) {
        var left = 0;
        var right = nums.Length - 1;
        
        while (left <= right)
        {
            var mid = left + (right - left) / 2;
            var midNum = nums[mid];
            
            if (midNum > target)
            {
                right = mid - 1;
            }
            else if (midNum == target)
            {
                return mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        
        return -1;
    }
}