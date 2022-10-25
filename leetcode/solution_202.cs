// Time Complexity: O(n) where n is the number of digits of the given integer
// Runtime: 51 ms, faster than 70.09% of C# online submissions for Happy Number.

// Space Complexity: O(1) because you need only constant extra space for the hashset
// Memory Usage: 27.6 MB, less than 66.74% of C# online submissions for Happy Number.

/*
2
4 = 4
16 = 16
1 + 36 = 37
9 + 49 = 58
25 + 64 = 89
64 + 81 = 145
1 + 16 + 25 = 42
16 + 4 = 20
4 + 0 = 4

when the calculation process returns to the original number, we could say that we are in an endless loop.
*/


public class Solution {
    public bool IsHappy(int n) {
        var existing = new HashSet<int>();
        existing.Add(n);
        
        while (true)
        {
            var temp = 0;
            
            // calculate the sum of the squares of its digits
            while (n > 0)
            {
                var remainder = n % 10;
                temp += (remainder * remainder);
                n /= 10;
            }
            
            // Is the number the same as 1? break the loop
            if (temp == 1)
            {
                break;
            }
            
            // Is the sum the same as the initial number, n? if yes, return false
            if (existing.Contains(temp))
            {
                return false;
            }
            
            existing.Add(temp);
            n = temp;
        }
        
        return true;
    }
}

