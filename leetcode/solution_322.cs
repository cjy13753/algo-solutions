/*

sort coins in the ascending manner.
discard elements that are bigger than amount in the sorted array.
create a dictionary to hold calculated value;
*/

public class Solution {
    public int CoinChange(int[] coins, int amount) {
        Array.Sort(coins);
        var newCoins = coins.Where((val, idx) => val <= 10000).ToArray();
        var dictionary = new Dictionary<int, int>();
        var result = recursive(newCoins, amount, dictionary);
        return result == -1 ? -1 : result - 1;
    }
    
    private int recursive(int[] coins, int n, Dictionary<int, int> dictionary)
    {
        if (n < 0)
        {
         return -1;
        }
        if (n == 0)
        {
            return 1;
        }
        
        if (dictionary.ContainsKey(n))
            return dictionary[n];
        var minValue = int.MaxValue;
        var flag = false;
        foreach (var e in coins)
        {
            var val = recursive(coins, n-e, dictionary);
            if (val != -1)
            {
                val++;
                minValue = Math.Min(minValue, val);
                flag = true;
            }
        }
            
            
        if (flag == true)
        {
            dictionary[n] = minValue;
            return minValue;
        }
        else
        {
            return -1;
        }
    }
}