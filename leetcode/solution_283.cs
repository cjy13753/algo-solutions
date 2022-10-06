// Time Complexity: O(n^2) where n is the number of elements in the given array.
// Runtime: 339 ms, faster than 14.38% of C# online submissions for Move Zeroes.

// Space Complexity: O(1)
// Memory Usage: 47.1 MB, less than 54.27% of C# online submissions for Move Zeroes.

/*

replace all zeros with the biggest possible number and count the number of zeros.
Apply an in-place sorting algorithm on the array, and replace the biggest elements with 0 the counted number of times at the beginning.
TC: O(nlogn), SC: O(1)

what in-place sorting algorithms are out there?
quick sort!
bubble sort...

Since the follow-up suggeests we minimize the total number of operations done, it'd be sensible to go with the algorithm with less time complexity.

I realize a fatal error after implementing quick sort.
Quick sort sorts the whole array in either an ascending order or a descending order when what I was asked to do is to keep the relative order of the original element.

Then, I will use an approach similar to a bubble sort, which in the worst case may take O(n^2) time complexity.
*/


public class Solution {
    public void MoveZeroes(int[] nums) {
        var idx = 0;
        
        while (idx < nums.Length)
        {
            if (nums[idx] != 0)
            {
                idx++;
                continue;
            }
            
            var pointer = idx + 1;
            
            while (pointer < nums.Length)
            {
                if (nums[pointer] == 0)
                {
                    pointer++;
                    continue;
                }
                
                var temp = nums[idx];
                nums[idx] = nums[pointer];
                nums[pointer] = temp;
                break;
            }
            
            idx++;
        }
        
    }
}