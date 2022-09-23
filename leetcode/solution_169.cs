// Time Complexity: O(n)
// Runtime: 214 ms, faster than 13.33% of C# online submissions for Majority Element.

// Space Complexity: O(n)
// Memory Usage: 40.4 MB, less than 91.42% of C# online submissions for Majority Element.

public class Solution {
    public int MajorityElement(int[] nums) {
        var majorityElem = nums[0];
        var majorityCount = 0;
            
        var dictionary = new Dictionary<int, int>();
       
        foreach (var num in nums)
        {
            var count = dictionary.GetValueOrDefault(num);
            var newCount = ++count;
            dictionary[num] = newCount;
            if (newCount > majorityCount)
            {
                majorityCount = newCount;
                majorityElem = num;
            }
        }
        return majorityElem;
    }
}