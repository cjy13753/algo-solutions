// Time Complexity: O(n) where n is the number of elements in the 2d array
// Runtime: 161 ms, faster than 87.30% of C# online submissions for Flood Fill.

// Space Complexity: O(log n) where n is the number of elements in the 2d array
// Memory Usage: 46 MB, less than 7.36% of C# online submissions for Flood Fill.

public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color)
        {
            return image;
        }
        
        var originColor = image[sr][sc];
        var q = new Queue<Tuple<int, int>>();
        var start = new Tuple<int, int>(sr, sc);
        q.Enqueue(start);
        var visited = new HashSet<Tuple<int,int>>();
        visited.Add(start);
        
        var deltas = new List<Tuple<int, int>>{new Tuple<int, int>(0, 1), new Tuple<int, int>(1, 0), new Tuple<int, int>(0, -1), new Tuple<int, int>(-1, 0)};
        
        while (q.Count != 0)
        {
            var rc = q.Dequeue();
            var row = rc.Item1;
            var col = rc.Item2;
            image[row][col] = color;
            
            foreach (var delta in deltas)
            {
                var newRow = row + delta.Item1;
                var newCol = col + delta.Item2;
                var newRC = new Tuple<int, int>(newRow, newCol);
                if (newRow >= 0 && newRow < image.Length && newCol >= 0 && newCol < image[0].Length && image[newRow][newCol] == originColor && !visited.Contains(newRC))
                {
                    q.Enqueue(newRC);
                    visited.Add(newRC);
                }
            }
        }
        
        return image;
    }
}