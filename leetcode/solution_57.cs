// Time Complexity: O(n) when n is the number of elments in the given array
// Space Complexity: O(1) if not counting result array
public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        var result = new List<int[]>();
        var inserted = false;

        foreach (var oldInterval in intervals)
        {
            var oldHead = oldInterval[0];
            var oldTail = oldInterval[1];
            var newHead = newInterval[0];
            var newTail = newInterval[1];

            if (newTail < oldHead)
            {
                if (inserted)
                {
                    result.Add(new int[]{ oldHead, oldTail });
                }
                else
                {
                    result.Add(new int[] { newHead, newTail });
                    result.Add(new int[]{ oldHead, oldTail });
                    inserted = true;
                }
            }
            else if (newTail >= oldHead && newHead <= oldTail)
            {
                newInterval[0] = Math.Min(oldHead, newHead);
                newInterval[1] = Math.Max(oldTail, newTail);
            }
            else
            {
                result.Add(new int[] { oldHead, oldTail });
            }
        }

        if (!inserted)
        {
            result.Add(new int[] { newInterval[0], newInterval[1] });
        }
        
        return result.ToArray();
    }
}