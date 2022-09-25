// Time Complexity: O(n + m) where they are each length of the given strings
// Runtime: 131 ms, faster than 45.16% of C# online submissions for Add Binary.

// Space Complexity: O(1) because the data structure to hold the result isn't counted
// Memory Usage: 38 MB, less than 19.38% of C# online submissions for Add Binary.

public class Solution {
    public string AddBinary(string a, string b) {
        var result = "";
        var carrier = 0;
        
        var aLength = a.Length;
        var bLength = b.Length;
        
        var aPointer = aLength - 1;
        var bPointer = bLength - 1;
        
        while (aPointer >= 0 && bPointer >= 0)
        {
            var aVal = Int32.Parse(a[aPointer].ToString());
            var bVal = Int32.Parse(b[bPointer].ToString());
            var sum = aVal + bVal + carrier;
            
            if (sum == 3)
            {
                result = "1" + result;
                carrier = 1;
            }
            else if (sum == 2)
            {
                result = "0" + result;
                carrier = 1;
            }
            else if (sum == 1)
            {
                result = "1" + result;
                carrier = 0;
            }
            else
            {
                result = "0" + result;
                carrier = 0;
            }
            aPointer--;
            bPointer--;
        }
        
        while (aPointer >= 0)
        {
            var aVal = Int32.Parse(a[aPointer].ToString());
            var sum = aVal + carrier;
            
            if (sum == 2)
            {
                result = "0" + result;
                carrier = 1;
            }
            else if (sum == 1)
            {
                result = "1" + result;
                carrier = 0;
            }
            else
            {
                result = "0" + result;
                carrier = 0;
            }
            aPointer--;
        }
        
        while (bPointer >= 0)
        {
            var bVal = Int32.Parse(b[bPointer].ToString());
            var sum = bVal + carrier;
            
            if (sum == 2)
            {
                result = "0" + result;
                carrier = 1;
            }
            else if (sum == 1)
            {
                result = "1" + result;
                carrier = 0;
            }
            else
            {
                result = "0" + result;
                carrier = 0;
            }
            bPointer--;
        }
        
        if (carrier == 1)
        {
            result = "1" + result;
        }
        
        return result;
    }
}