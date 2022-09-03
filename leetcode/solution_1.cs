// Time Complexity: O(N)
// Runtime: 249 ms, faster than 46.40% of C# online submissions for Two Sum.

// Space Complexity: O(N)
// Memory Usage: 43 MB, less than 48.54% of C# online submissions for Two Sum.

public class Solution
{
	public int[] TwoSum(int[] nums, int target)
	{
		var result = new int[2];
		
		var hash = new Dictionary<int, int>();
		for (int i = 0; i < nums.Length; i++)
		{
			if (hash.ContainsKey(target - nums[i]))
			{
				result[0] = hash[target - nums[i]];
				result[1] = i;
				break;
			}
			hash.TryAdd(nums[i], i);
		}
		
		return result;
	}
}