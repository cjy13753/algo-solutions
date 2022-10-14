// Time Complexity: O(n), where n is the number of elements in the given array
// Runtime: 265 ms, faster than 66.08% of C# online submissions for Squares of a Sorted Array.

// Space Complexity: O(n)
// Memory Usage: 48.4 MB, less than 93.67% of C# online submissions for Squares of a Sorted Array.

/*
traverse the given integer array and find the first non-negative integer.
if you can't find any non-negative integer, return the given array right away.
if the first non-negative integer is at the beginning of the array, return the given array right away.

Create a new list to hold integers.
Declare two variables to point to the first non-negative integer and the number left of it.

Do the following in a while loop:

If both pointers are not out of the boundary of the array, 
Compare the absolute values that the two pointers are pointing to, and store the square of the value whose absolute value was smaller in the list created previously.
If the right value was smaller, move the pointer to the right by 1.
If the left value was smaller, move the pointer to the left by 1.

If both pointers are out of boundary,
break the loop

If left pointer is out of boundary,
just store the square of the remaining values in the right part.

*/

public class Solution {
    public int[] SortedSquares(int[] nums) {
        if (nums[0] >= 0)
        {
            return nums.Select(x => x * x).ToArray();
        }
        
        int nonNegative = 0;
        
        for (var i = 0; i < nums.Length; i++)
        {
            if (nums[i] >= 0)
            {
                nonNegative = i;
                break;
            }
        }
        
        if (nonNegative == 0)
        {
            var list = new List<int>();
            for (var i = nums.Length - 1; i >= 0; i--)
            {
                list.Add(nums[i]);
            }
            return list.Select(x => x * x).ToArray();
        }
        
        int negative = nonNegative - 1;
        var holder = new List<int>();
        
        while (negative >= 0 || nonNegative < nums.Length)
        {
            if (negative >= 0 && nonNegative < nums.Length)
            {
                var left = Math.Abs(nums[negative]);
                var right = Math.Abs(nums[nonNegative]);
                if (right < left)
                {
                    nonNegative++;
                }
                else
                {
                    negative--;
                }
                var small = Math.Min(left, right);
                holder.Add(small * small);
                continue;
            }
            
            if (negative >= 0)
            {
                var left = Math.Abs(nums[negative]);
                holder.Add(left * left);
                negative--;
            }
            
            if (nonNegative < nums.Length)
            {
                var right = Math.Abs(nums[nonNegative]);
                holder.Add(right * right);
                nonNegative++;
            }
        }
        
        return holder.ToArray();
    }
}