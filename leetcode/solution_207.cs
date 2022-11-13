// Time Complexity: O(V+E) 
// Space Complexity: O(N^2) where n is the given numCoures

/*
Assume that we represent the relationship of prerequisites as a directed graph.
prerequisite is the starting vertex and the target is the arriving vertex.
If there is no cycle in the directed graph, we could return true.

Then, how can we figure out if the graph has no cycle?
I'm going to keep track of the number of times each vertex is referenced by another vertex.
starting with the vertex with 0 reference, I'm going to do a level by level dereferencing operation until there is no element left in the queue.
If there are vertices that still have no less than 1 reference count, I will return false. Otherwise, return true

*/

public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var directions = new Dictionary<int, List<int>>();
        for (int i = 0; i < numCourses; i++)
        {
            directions[i] = new List<int>();
        }
        var referenceCounts = new int[numCourses];
        var queue = new Queue<int>();
        
        foreach (var prerequisite in prerequisites)
        {
            var departure = prerequisite[1];
            var arrival = prerequisite[0];
            
            directions[departure].Add(arrival);
            referenceCounts[arrival] += 1;
        }
        
        for (int i = 0; i < numCourses; i++)
        {
            if (referenceCounts[i] == 0)
            {
                queue.Enqueue(i);
            }
        }
        
        if (queue.Count == 0)
        {
            return false;
        }
        
        while (queue.Count > 0)
        {
            var start = queue.Dequeue();
            var arrivals = directions[start];
            foreach (var arrival in arrivals)
            {
                referenceCounts[arrival]--;
                if (referenceCounts[arrival] == 0)
                {
                    queue.Enqueue(arrival);
                }
            }
            
        }
        
        return !referenceCounts.Any(x => x > 0);
        
    }
}