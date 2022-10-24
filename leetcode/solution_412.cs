// Time Complexity: O(n) where n is the given integer
// Runtime: 235 ms, faster than 58.16% of C# online submissions for Fizz Buzz.

// Space Complexity: O(1) not accounting for the data structure to return answer
// Memory Usage: 47.3 MB, less than 28.31% of C# online submissions for Fizz Buzz.


public class Solution {
    public IList<string> FizzBuzz(int n) {
        var holder = new List<string>();
        
        for (int i = 1; i <= n; i++)
        {
            if (i % 3 == 0)
            {
                if (i % 5 == 0)
                {
                    holder.Add("FizzBuzz");
                    continue;
                }
                
                else
                {
                    holder.Add("Fizz");
                    continue;
                }
            }
            
            if (i % 5 == 0)
            {
                holder.Add("Buzz");
                continue;
            }
            
            holder.Add(i.ToString());
        }
        
        return holder;
    }
}