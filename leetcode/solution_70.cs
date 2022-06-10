//Runtime: 21 ms, faster than 91.26% of C# online submissions for Climbing Stairs.
//Memory Usage: 26.4 MB, less than 22.12% of C# online submissions for Climbing Stairs.
//https://leetcode.com/problems/climbing-stairs/

void Main()
{
	new Solution().ClimbStairs(4).Dump();
}

public class Solution
{
	int[] dp = new int[46];
	
	public int ClimbStairs(int n)
	{
		if (n == 1)
		{
			return 1;
		}
		
		if (n == 2)
		{
			return 2;
		}
		
		int oneAhead = 0;
		int twoAhead = 0;
		
		if (dp[n-1] == 0)
		{
			dp[n-1] = ClimbStairs(n-1);
		}
		oneAhead = dp[n-1];
		
		if (dp[n-2] == 0)
		{
			dp[n-2] = ClimbStairs(n-2);
		}
		twoAhead = dp[n-2];
		
		return oneAhead + twoAhead;
	}
}
