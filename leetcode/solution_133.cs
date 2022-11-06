// Time Complexity: O(V + E) where V is the number of nodes in the graph and E is the number of edges in the graph
// Space Complexity: O(V) where V is the number of nodes in the connected graph

/*

if the node is empty:
    return null

make an array of Node with the size of 100.
make an array of bool with the size of 100 for visited
make a queue of Node

<will do a bfs from here>
clone the given node(A), copying only the value.
put the cloned node in the array in the index corresponding to the value.
put the given node and cloned node into the queue. This order is important

while queue is not empty:
    popped original node
    popped cloned node
    put original's value in the visited array
    
    
    for each neighbor of the original node:
        if neighbor is visited:
            fetch the corresponding cloned node and put it in the clonded node's adjacent list
        if neighbor is not visited
            if the corresponding cloned node of the neighbor is in the array:
                put the cloned node in the cloned node's adjacent list
            else:
                create a new node with the neighbor's value
                put the newly created node in the right index in the array
            put it in the visited array
            put the neighbor and cloned node in the queue
            
return the cloned node(A)

*/



/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
        if (node is null)
        {
            return null;
        }
        var cache = new Node[101];
        var visited = new bool[101];
        var queue = new Queue<Node>();
        
        var cloned = new Node(node.val);
        cache[node.val] = cloned;
        visited[node.val] = true;
        
        queue.Enqueue(node);
        queue.Enqueue(cloned);
        
        while (queue.Count > 0)
        {
            var poppedOriginal = queue.Dequeue();
            var poppedCloned = queue.Dequeue();
            
            foreach (var neighbor in poppedOriginal.neighbors)
            {
                if (visited[neighbor.val] == true)
                {
                    poppedCloned.neighbors.Add(cache[neighbor.val]);
                }
                else
                {
                    Node clonedNeighbor;
                    if (cache[neighbor.val] is null)
                    {
                        clonedNeighbor = new Node(neighbor.val);
                        cache[neighbor.val] = clonedNeighbor;
                    }
                    else
                    {
                        clonedNeighbor = cache[neighbor.val];
                    }
                    
                    poppedCloned.neighbors.Add(clonedNeighbor);
                    visited[neighbor.val] = true;
                    queue.Enqueue(neighbor);
                    queue.Enqueue(clonedNeighbor);
                }
            }
        }
        
        return cloned;
    }
}