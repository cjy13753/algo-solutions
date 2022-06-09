//Runtime: 54 ms, faster than 98.06% of C# online submissions for Split a String in Balanced Strings.
//Memory Usage: 36 MB, less than 16.13% of C# online submissions for Split a String in Balanced Strings.
public class Solution
{
	public int BalancedStringSplit(string s)
	{
		int left = 0;
		int right = 0;
		int ans = 0;
		
		foreach (char letter in s)
		{
			if (letter == 'L')
			{
				left += 1;
			}
			else
			{
				right += 1;
			}
			
			if (left == right)
			{
				ans += 1;
				left = 0;
				right = 0;
			}
		}
		
		return ans;

	}
}
