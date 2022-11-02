// Time Complexity: O(nlogn) where n is the number of elements in the given array
// Space Complexity: O(n)

/*
brute-force approach would take TC O(nlogn)
*/

public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        var storage = new List<(int, int)>();
        
        for (int i = 0; i < points.Length; i++)
        {
            var x = points[i][0];
            var y = points[i][1];
            var distance = x * x + y * y;
            storage.Add((distance, i));    
        }
        
        storage.Sort();
        
        var res = new int[k][];
        
        for (var i = 0; i < k; i++)
        {
            var (distance, index) = storage[i];
            res[i] = points[index];
        }
        
        return res;
    }
}