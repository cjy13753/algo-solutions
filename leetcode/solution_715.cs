// Wrong Answer

public class RangeModule {

    private int[][] intervals = new int[0][];

    public RangeModule() {
    }
    
    public void AddRange(int left, int right) {
        var result = new List<int[]>();
        var newInterval = new int[] { left, right };
        var inserted = false;

        foreach (var interval in intervals)
        {
            var oldHead = interval[0];
            var oldTail = interval[1];
            var newHead = newInterval[0];
            var newTail = newInterval[1];

            if (newTail < oldHead)
            {
                if (inserted)
                {
                    result.Add(interval);
                }
                else
                {
                    result.Add(newInterval);
                    result.Add(interval);
                    inserted = true;
                }
            }
            else if (newHead > oldTail)
            {
                result.Add(interval);
            }
            else
            {
                newInterval[0] = Math.Min(newHead, oldHead);
                newInterval[1] = Math.Max(newTail, oldTail);
            }
        }

        if (inserted == false)
        {
            result.Add(newInterval);
        }

        intervals = result.ToArray();

        Console.WriteLine($"addRange left: {left}, right: {right}");
        foreach (var interval in intervals)
        {
            Console.WriteLine($"{interval[0]}, {interval[1]}");
        }
    }
    
    public bool QueryRange(int left, int right) {
        foreach (var interval in intervals)
        {
            var oldLeft = interval[0];
            var oldRight = interval[1];
            
            if (right < oldLeft)
            {
                break;
            }

            if (left >= oldLeft && right <= oldRight)
            {
                return true;
            }
        }

        return false;
    }
    
    public void RemoveRange(int left, int right) {
        var result = new List<int[]>();
        var removeInterval = new int[] { left, right };

        foreach (var interval in intervals)
        {
            var oldHead = interval[0];
            var oldTail = interval[1];
            var removeHead = removeInterval[0];
            var removeTail = removeInterval[1];

            if (removeTail <= oldHead)
            {
                Console.WriteLine("1");
                result.Add(interval);
            }
            else if (removeHead <= oldHead && removeTail >= oldTail)
            {
                Console.WriteLine("2");
                continue;
            }
            else if (removeHead <= oldHead && removeTail < oldTail)
            {
                Console.WriteLine("3");
                result.Add(new int[]{ removeHead, oldTail });
            }
            else if (removeHead > oldHead && removeTail < oldTail)
            {
                Console.WriteLine("4");
                result.Add(new int[]{ oldHead, removeHead });
                result.Add(new int[]{ removeTail, oldTail });
            }
            else if (removeHead > oldHead && removeHead < oldTail && removeTail >= oldTail)
            {
                Console.WriteLine("5");
                result.Add(new int[]{ oldHead, removeHead });
            }
            else
            {
                Console.WriteLine("6");
                result.Add(interval);
            }
        }

        intervals = result.ToArray();
        Console.WriteLine($"removeRange left: {left}, right: {right}");
        foreach (var interval in intervals)
        {
            Console.WriteLine($"{interval[0]}, {interval[1]}");
        }
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.AddRange(left,right);
 * bool param_2 = obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */