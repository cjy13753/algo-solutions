// Time Complexity: O(m * n) where m is the width, and n is the height of the 2d array.
// Runtime: 161 ms, faster than 87.30% of C# online submissions for Flood Fill.

// Space Complexity: not very sure
// Memory Usage: 46 MB, less than 7.36% of C# online submissions for Flood Fill.

public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color)
        {
            return image;
        }
        var height = image.Length;
        var width = image[0].Length;
        
        var originalColor = image[sr][sc];
        image[sr][sc] = color;

        var q = new Queue<int[]>();
        q.Enqueue(new int[]{sr, sc});
        
        var deltas = new List<int[]>{new int[]{0, 1}, new int[]{1, 0}, new int[]{0, -1}, new int[]{-1, 0}};
        
        while (q.Count != 0)
        {
            var rc = q.Dequeue();
            var row = rc[0];
            var col = rc[1];
            
            foreach (var delta in deltas)
            {
                var newRow = row + delta[0];
                var newCol = col + delta[1];
                if (newRow < 0 || newRow >= height || newCol < 0 || newCol >= width || image[newRow][newCol] != originalColor) continue;
                image[newRow][newCol] = color;
                q.Enqueue(new int[]{newRow, newCol});
            }
        }
        
        return image;
    }
}