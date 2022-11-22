// Time Complexity: O(n^2) where n is the number of elements in the given array
// Space Complexity: O(1) if not accounting for the output list

public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        var res = new List<IList<int>>();
        
        var prevNum = int.MinValue;
        var i = 0;
        
        while (i < nums.Length)
        {
            if (nums[i] == prevNum)
            {
                i++;
                continue;
            }
            
            prevNum = nums[i];
            
            var target = (-1) * nums[i];
            var start = i + 1;
            var end = nums.Length - 1;
            
            while (start < end)
            {
                var twoSum = nums[start] + nums[end];
                if (twoSum > target)
                {
                    end--;
                }
                else if (twoSum == target)
                {
                    res.Add(new List<int>{nums[i], nums[start], nums[end]});
                    var prevStart = nums[start];
                    var prevEnd = nums[end];
                    start++;
                    end--;
                    
                    while (start < nums.Length)
                    {
                        if (nums[start] == prevStart)
                        {
                            start++;
                            continue;
                        }
                        break;
                    }
                    
                    while (end > start)
                    {
                        if (nums[end] == prevEnd)
                        {
                            end--;
                            continue;
                        }
                        break;
                    }
                }
                else
                {
                    start++;
                }
            }
        }
        
        return res;
        
    }
}