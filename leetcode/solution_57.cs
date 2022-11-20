// Fail to solve

/*

The core concept of the approach to this problem is to not insert the new interval until when it's certain to insert the new interval and how it should be merged with neighbors.


if newInterval end < interval start
     put newInterval and, put the rest
     return res
else
    merged's left is min of newInterval left and iteration's left

if newInterval start > interval's end
    just put the interval in the res

else
    end merg's right is max of newInterval's end and iterations'right

put the last in the res

return



*/

public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        var res = new List<int[]>();
        var start = 0;
        
        for (int i = 0; i < intervals.Length; i++)
        {
            var interval = intervals[i];
            
            if (newInterval[1] < interval[0])
            {
                res.Add(newInterval);
                if (i < intervals.Length - 1)
                {
                    var rest = intervals[i..].Select(e => (int[])e.Clone()).ToArray();
                    res.Add(rest);
                }
                return res;
            }
            else if (interval[1] < newInterval[0])
            {
                res.Add((int[])interval.Clone());
            }
            else
            {
                start = Math.Min(interval[0], newInterval[0]);
            }
        }
        
        res.Add(new int[]{start, });
        
        return res.ToArray();
}