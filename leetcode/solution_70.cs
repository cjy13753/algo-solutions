//Runtime: 29 ms, faster than 61.33 % of C# online submissions for Climbing Stairs.
//Memory Usage: 25 MB, less than 92.51 % of C# online submissions for Climbing Stairs.

void Main()
{
	new Solution().ClimbStairs(4).Dump();
}

public class Solution
{
	int[] dp = new int[46];

	public Solution()
	{
		Array.Fill(dp, -1);
		dp[1] = 1;
		dp[2] = 2;
	}

	
	public int ClimbStairs(int n)
	{
		if (dp[n] != -1)
		{
			return dp[n];
		}
		
		int oneAhead = 0;
		int twoAhead = 0;
		
		dp[n] = ClimbStairs(n-1) + ClimbStairs(n-2);
		
		return dp[n];
	}
}
