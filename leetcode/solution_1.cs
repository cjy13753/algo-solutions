public class Solution
{
	public int[] TwoSum(int[] nums, int target)
	{
		var result = new int[2];
		
		var hash = new Dictionary<int, int>();
		hash.Add(nums[0], 0);
		
		for (int i = 1; i < nums.Length; i++)
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