// Time Complexity: O(n) where n is the number of elements in the given array
// Runtime: 499 ms, faster than 6.63% of C# online submissions for Best Time to Buy and Sell Stock.

// Space Complexity: O(1)
// Memory Usage: 47.2 MB, less than 44.94% of C# online submissions for Best Time to Buy and Sell Stock.

public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length <= 1)
        {
            return 0;
        }

        var prevPurchasePrice = Convert.ToInt32(Math.Pow(10, 5));
        var lowestNegativeDifference = 0;
        
    
        foreach (var price in prices)
        {
            if (price < prevPurchasePrice)
            {
                prevPurchasePrice = price;
            }
            else
            {
                lowestNegativeDifference = Math.Min(lowestNegativeDifference, prevPurchasePrice - price);
            }
        }
        
        return Math.Abs(lowestNegativeDifference);
        
    }
}