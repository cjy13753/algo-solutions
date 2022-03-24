from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adjList = [set() for _ in range(n)]
        leavesQueue = deque()
        indegree = [0] * n
        
        for src, dest in edges:
            adjList[src].add(dest)
            adjList[dest].add(src)
            indegree[src] += 1
            indegree[dest] += 1
        
        for i in range(n):
            if indegree[i] == 1:
                leavesQueue.append(i)
        
        while n > 2:
            leavesLen = len(leavesQueue)
            n -= leavesLen
            for _ in range(leavesLen):
                now = leavesQueue.popleft()
                neighbor = adjList[now].pop()
                adjList[neighbor].remove(now)
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 1:
                    leavesQueue.append(neighbor)
        
        
        return list(leavesQueue)
            
        