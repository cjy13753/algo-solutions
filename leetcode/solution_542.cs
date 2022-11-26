// Time Complexity: ?
// Space Complexity: O(m * n) where m is the row count, and n is the col count because in the worst case, all the cells in the mat contain 0

/*
find at level 1
find at level 2
find at level 3
and do this step for all 0 at the same time.

what if one 0's bfs encounter a path that another 0's path?
if the number already in the cell is bigger than what the other 0 has to offer, replace it with the lower one and keep going.
if that number is smaller, the other 0's stop bfs
if that number is 0, stop bfs

100 100
011 010
000
*/

/*


find at level 1
find at level 2
find at level 3
and do this step for all 0 at the same time.

what if one 0's bfs encounter a path that another 0's path?
if the number already in the cell is bigger than what the other 0 has to offer, replace it with the lower one and keep going.
if that number is smaller, the other 0's stop bfs
if that number is 0, stop bfs

100 100
011 010
000

*/

public class Solution {
    public int[][] UpdateMatrix(int[][] mat)
    {
        var colCount = mat[0].Length;
        var rowCount = mat.Length;
        
        var res = new int[rowCount][];
        for (int i = 0; i < rowCount; i++)
        {
            res[i] = new int[colCount];
        }
        
        var queue = new Queue<(int, int, int)>(); // row, col, distance
        for (int row = 0; row < rowCount; row++)
        {
            for (int col = 0; col < colCount; col++)
            {
                res[row][col] = int.MaxValue;
                if (mat[row][col] == 0)
                {
                    queue.Enqueue((row, col, 0));
                }
            }
        }
        
        while (queue.Count > 0)
        {
            var (row, col, distance) = queue.Dequeue();
            if (res[row][col] <= distance)
            {
                continue;
            }
            
            res[row][col] = distance;
            foreach (var (dRow, dCol) in new List<(int, int)>{(1, 0), (-1, 0), (0, 1), (0, -1)})
            {
                var newRow = row + dRow;
                var newCol = col + dCol;
                if (newRow >= 0 && newRow < rowCount && newCol >= 0 && newCol < colCount && res[newRow][newCol] > distance + 1)
                {
                    queue.Enqueue((newRow, newCol, distance + 1));
                }
            }
        }
        
        return res;
    }
}