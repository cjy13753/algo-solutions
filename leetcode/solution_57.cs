// Fail to solve

/*

leftMost
rightMost

case 1: newLeft < newRight < interval[0] < interval[1] => Add
case 2: newLeft < interval[0] < newRight < interval[1] => 
case 3: interval[0] < newLeft < newRight < interval[1] =>
case 4: interval[0] < newLeft < interval[1] < newRight => 
case 5: interval[0] < interval[1] < newLeft < newRight => 

*/


public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        if (intervals.Length == 0)
        {
            return intervals;
        }
        
        var res = new List<int[]>();
        var newLeft = newInterval[0];
        var newRight = newInterval[1];
        
        var left = int.MaxValue;
        var right = 0;
        
        for (var interval in intervals)
        {
            left = Math.Min(left, interval[0]);
            if (newLeft >= interval[0])
            {
                if (newLeft <= interval[1])
                {
                    
                }
                else
                {
                    right = interval[1];
                    res.Add(new int[2]{left, right});
                }
            }
            else
            {
                left = newLeft;
                if (newRight <= interval[1])
                {
                    right = interval[1];
                    res.Add(new int[2]{left, right});
                }
                else
                {
                    right = newRight;
                }
            }
        }
        
        
        
        return res.ToArray();
    }
}