// Time Complexity: O(n) where n is the input parameter, amount
// Space Complexity: O(n) where n is the input parameter, amount

/*
amount = 11
min(dp[10], dp[9], dp[6]) + 1
dp[0] = 0
dp[1] = min(dp[0], dp[-1], dp[-4]) + 1 <= if all the indices are negative integer or all dp values are -1, just put -1 in the array for the index 1
dp[2] = 
dp[3] = 
dp[4] = 
dp[5] = 
dp[6] = 
*/

public class Solution {
    public int CoinChange(int[] coins, int amount) {
        var dp = new int[amount + 1];
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++)
        {
            var indexCandidates = new List<int>();
            foreach (var coin in coins)
            {
                if (i - coin >= 0)
                {
                    indexCandidates.Add(i - coin);
                }
            }
            
            if (indexCandidates.Count == 0)
            {
                dp[i] = -1;
                continue;
            }
            
            var dpCandidates = new List<int>();
            foreach (var candidate in indexCandidates)
            {
                if (dp[candidate] != -1)
                {
                    dpCandidates.Add(dp[candidate]);
                }
            }
            
            if (dpCandidates.Count == 0)
            {
                dp[i] = -1;
                continue;
            }
            
            dp[i] = dpCandidates.Min() + 1;
        }
        
        
        return dp[amount];
    }
}