// Time Complexity: not confident
// Space Complexity: O(m * n) where m is the height and n is the width of the given 2d array

/*
- make a list of all the coordinates of lands
- make a 2d array of the same size as the given grid to remember that a land has been visited
- count = 0
- Iterate through the list while doing the following
  - if the land has been visited, continue
  - do a bfs for non-visited land with the element and mark visited
  - increase the count 

return count

*/


public class Solution {
    public int NumIslands(char[][] grid) {
        var rows = grid.Length;
        var cols = grid[0].Length;
        var visited = new HashSet<(int, int)>();
        int count = 0;
        var directions = new List<(int, int)>{(0, 1), (0, -1), (1, 0), (-1 , 0)};

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == '0')
                {
                    continue;
                }

                var land = (i, j);

                if (visited.Contains(land))
                {
                    continue;
                }
                
                var queue = new Queue<(int, int)>();
                queue.Enqueue(land);
                visited.Add(land);

                while (queue.Count > 0)
                {
                    var position = queue.Dequeue();
                    var (row, col) = position;
                    foreach (var (dRow, dCol) in directions)
                    {
                        var newRow = row + dRow;
                        var newCol = col + dCol;
                        var newPosition = (newRow, newCol);
                        if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == '1' && !visited.Contains(newPosition))
                        {
                            queue.Enqueue(newPosition);
                            visited.Add(newPosition);
                        }
                    }
                    
                }
                count++;
            }
        }

        return count;
    }
}