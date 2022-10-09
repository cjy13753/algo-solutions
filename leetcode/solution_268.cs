// Time Complexity: O(n) where n is the number of elemnts in the given array
// Runtime: 179 ms, faster than 47.67% of C# online submissions for Missing Number.

// Space Complexity: O(1)
// Memory Usage: 40 MB, less than 61.05% of C# online submissions for Missing Number.

/*
requirements check
- TC: O(n), SC: O(1)
- the numbers in the array are unique
- n <= 10^4

approach 1
brute-force: sort the array and traverse the array from the beginning to find which number is missing
TC: O(nlogn), SC: O(1)

approach 2
sum up the numbers that should be in the range [0, n].
sum up all the numbers in the array.
subtract the latter from the former.
and you get the answer
TC: O(n), SC: O(1) where n is the number of elements in the given array
This apporach was possible because n <= 10^4;

If n <= 2^31 - 1, what would I do instead?
I would use the long type instead of int type. Using this approach also has TC: O(n), SC: O(1)
*/


public class Solution {
    public int MissingNumber(int[] nums) {
        var length = nums.Length;
        
        var fullSum = (length * (length + 1)) / 2;
        var missingSum = 0;
        foreach (var num in nums)
        {
            missingSum += num;
        }
        
        return fullSum - missingSum;
    }
}