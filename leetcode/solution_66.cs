// Time Complexity: O(n), where n is the number of elements in the given array
// Runtime: 205 ms, faster than 65.97% of C# online submissions for Plus One.

// Space Complexity: O(1) extra space assuming that the problem demands that we do not alter any of the elements in the given array
// Memory Usage: 41.2 MB, less than 30.14% of C# online submissions for Plus One.

/*
Since digits.length can 100, I can not convent it to either int or long.
The concept, carry, might be of great use in this case.
*/

public class Solution {
    public int[] PlusOne(int[] digits) {
        var holder = new List<int>();
        var carry = 1;
        
        for (var i = digits.Length - 1; i >= 0; i--)
        {
            if (digits[i] + carry > 9)
            {
                holder.Add(0);
            }
            else
            {
                holder.Add(digits[i] + carry);
                carry = 0;
            }
        }
        
        if (carry == 1)
        {
            holder.Add(1);
        }
        
        var res = new int[holder.Count];
        int j = 0;
        for (var i = holder.Count - 1; i >= 0; i--)
        {
            res[i] = holder[j++];
        }
        return res;
    }
}