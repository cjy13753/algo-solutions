// Time Complexity: O(nlogn) where n is the number of elements in the given array
// Runtime: 196 ms, faster than 30.15% of C# online submissions for Single Number.

// Space Complexity: O(1)
// Memory Usage: 39.9 MB, less than 77.00% of C# online submissions for Single Number.

/*

brute force approach
sort the array in an ascending manner, and iterate through the array with two assistant pointers to find the single number
TC: O(nlog), SC: O(1)


add and subtract cycle?
nums = [4, 1, 2, 1, 2]
4
-1
+2
-1
+2
=4

nums = [1, 4, 2, 1, 2]
1
-4
+2
-1
+2
=0

multiply and divide cycle?
4
*1
/2
*1
/2
= 1

there is a sorting alogrithm that takes only O(n) time complexity under certain conditions.
X

when the next number is less than or equal to the previous number, flip the operator.
start with the plus operator.
nums = [4,1,2,1,2]
4 - 1 - 2 + 1 + 2

nums = [2,2,1]
2 -2 + 1

nums = [1, 2, 3, 3, 2]
1 + 2 + 3 - 3 + 2

*/

public class Solution {
    public int SingleNumber(int[] nums) {
        Array.Sort(nums);
        var first = 0;
        var second = 1;
        
        while (second < nums.Length)
        {
            if (nums[first] != nums[second])
            {
                return nums[first];
            }
            
            first += 2;
            second += 2;
        }
        
        return nums[first];
    }
}