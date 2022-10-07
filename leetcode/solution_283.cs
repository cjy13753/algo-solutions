// Time Complexity: O(n) where n is the number of elements in the given array.
// Runtime: 211 ms, faster than 77.26% of C# online submissions for Move Zeroes.

// Space Complexity: O(1)
// Memory Usage: 47.3 MB, less than 32.20% of C# online submissions for Move Zeroes.


/*
new approach

how about using two pointers?
one pointer(i) looks for the position holding 0, another(j) looks for  the position holding non-zero
we start the code by first finding appropriate i.
and then find appropriate j that starts from the next of i.

replace the value in i with the value in j.


    i j
1 2 0 3 4 0 5

      i j
1 2 3 0 4 0 5

        i   j
1 2 3 4 0 0 5

    i j
1 2 0 3 4 5

      i j
1 2 3 0 4 5

i for next 0, j for next non-zero
is there any case where i meets or exceeds j? never

*/


public class Solution {
    public void MoveZeroes(int[] nums) {
        var zero = MoveToNextZero(nums, 0);
        var nonZero = MoveToNextNonZero(nums, zero + 1);
        
        while (nonZero < nums.Length)
        {
            Swap(nums, zero, nonZero);
            zero = MoveToNextZero(nums, zero);
            nonZero = MoveToNextNonZero(nums, nonZero);
        }
    }
    
    private void Swap(int[] nums, int i, int j)
    {
        var temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    private int MoveToNextZero(int[] nums, int zero)
    {
        while (zero < nums.Length)
        {
            if (nums[zero] == 0)
            {
                break;
            }
            zero++;
        }
        
        return zero;
    }
    
    private int MoveToNextNonZero(int[] nums, int nonZero)
    {
        while (nonZero < nums.Length)
        {
            if (nums[nonZero] != 0)
            {
                break;
            }
            nonZero++;
        }
        
        return nonZero;
    }
}