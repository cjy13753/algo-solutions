// Time Limit Exceeded

/*
BFS for each cell until finding 0?
I think this approach is too wasteful in terms of time complexity, but can't think of any alternative.
*/

public class Solution {
    public int[][] UpdateMatrix(int[][] mat) {
        var width = mat.Length;
        var height = mat[0].Length;
        var res = new int[width][];
        
        for (int i = 0; i < width; i++)
        {
            res[i] = new int[height];
        }
        
        for (var row = 0; row < width; row++)
        {
            for (var col = 0; col < height; col++)
            {
                if (mat[row][col] == 0)
                {
                    res[row][col] = 0;
                }
                else
                {
                    res[row][col] = bfs(mat, row, col);
                }
            }
        }
        
        return res;
    }
    
    private int bfs(int[][] mat, int _row, int _col)
    {
        var width = mat.Length;
        var height = mat[0].Length;
        
        var queue = new Queue<(int, int, int)>();
        var directions = new List<(int, int )> { (0, 1), (1, 0), (0, -1), (-1, 0)};
        var visited = new HashSet<(int, int)>();
        
        var _distance = 0;
        
        queue.Enqueue((_row, _col, 0));
        visited.Add((_row, _col));
        
        while (queue.Count > 0)
        {
            var (row, col, distance) = queue.Dequeue();
            foreach (var (dRow, dCol) in directions)
            {
                var newRow = row + dRow;
                var newCol = col + dCol;
                
                if (newRow >= 0 && newRow < width && newCol >= 0 && newCol < height && !visited.Contains((newRow, newCol)))
                {
                    if (mat[newRow][newCol] == 0)
                    {
                        return distance + 1;
                    }
                    else
                    {
                        queue.Enqueue((newRow, newCol, distance + 1));
                        visited.Add((newRow, newCol));
                    }
                }
            }
        }
        
        return _distance;
    }
}