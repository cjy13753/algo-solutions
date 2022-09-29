// Time Complexity: O(n) where n is the number of elements in the given array
// Runtime: 191 ms, faster than 91.39% of C# online submissions for Contains Duplicate.

// Space Complexity: O(n) where n is the number of elements in the given array
// Memory Usage: 52.9 MB, less than 6.99% of C# online submissions for Contains Duplicate.

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var set = new HashSet<int>();
        
        foreach (var num in nums)
        {
            if (set.Contains(num))
            {
                return true;
            }
            set.Add(num);
        }
        
        return false;
    }
}