""" 
Attempt #3

Runtime: 216 ms, faster than 12.88% of Python3 online submissions for Course Schedule.
Memory Usage: 15.2 MB, less than 99.95% of Python3 online submissions for Course Schedule.
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        
        for dest, origin in prerequisites:
            indegree[dest] += 1
            adjList[origin].append(dest)
            
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            popped = queue.popleft()
            for i in adjList[popped]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return True if sum(indegree) == 0 else False