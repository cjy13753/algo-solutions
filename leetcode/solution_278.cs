// Time Complexity: O(log n) thanks to binary search
// Runtime: 20 ms, faster than 96.32% of C# online submissions for First Bad Version.

// Space Complexity: O(1)
// Memory Usage: 26.6 MB, less than 11.31% of C# online submissions for First Bad Version.


/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        var left = 1;
        var right = n;
        int result = Int32.MaxValue;
        
        while (left <= right)
        {
            var mid = left + (right - left) / 2;
            var isBadVersion = IsBadVersion(mid);
            if (isBadVersion)
            {
                result = mid;
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        
        return result;
    }
}