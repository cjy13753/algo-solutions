// Wrong Answer


/*
x = y * y, then y is square root of x.
2^31 - 1 < 2^30 * 2^30
therefore, the biggest candidate for y is (2^30 - 1)
0 <= y <= 2^30 - 1
y^2 <= x 
do a binary search to find the biggest number whose squared value is smaller than or equal to x.
*/

public class Solution
{
	public int MySqrt(int x)
	{
		var start = Convert.ToInt32(Math.Pow(2, 15));
		var end = Convert.ToInt32(Math.Pow(2, 16));
		var boundary = 0;
		
		while (start <= end)
		{
			var mid = start + (end - start) / 2;
			var val = Convert.ToInt32(mid * mid);
			if (val == 0)
			{
				end = mid - 1;
			}
			else
			{
				boundary = Math.Max(boundary, mid);
				start = mid + 1;
			}
		}

		start = 0;
		end = boundary;
		
		var ans = 0;

		while (start <= end)
		{
			var mid = start + (end - start) / 2;
			if (mid * mid < x)
			{
				ans = Math.Max(ans, mid);
				start = mid + 1;
			}
			else if (mid * mid == x)
			{
				return mid;
			}
			else
			{
				end = mid - 1;
			}
		}

		return ans;

	}
}