// Time Complexity: O(n) where n is the given integer because I need to find the maximum possible candidate to be a square root of the given integer.
// Runtime: 56 ms, faster than 25.19% of C# online submissions for Sqrt(x).

// Space Complexity: O(1)
// Memory Usage: 25.7 MB, less than 20.69% of C# online submissions for Sqrt(x).

public class Solution
{
	public int MySqrt(int x)
	{
        var finder = (int)Math.Pow(2, 15);
        var maxSquareRoot = 0;
        while (finder * finder > 0)
        {
            maxSquareRoot = finder;
            finder++;
        }
        
        var res = 0;
        var start = 0;
        var end = maxSquareRoot;
        
        while (start <= end)
        {
            var mid = start + (end - start) / 2;
            var square = mid * mid;
            if (square > x)
            {
                end = mid - 1;
            }
            else if (square == x)
            {
                return mid;
            }
            else
            {
                res = Math.Max(res, mid);
                start = mid + 1;
            }
        }
        
        return res;
	}
}