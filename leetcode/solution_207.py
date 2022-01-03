'''
Summary

Attempt #1
Status: Failed - "Wrong Answer"
Approach: BFS (if there is a cycle, return False)
'''


import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numCourses = 5
        prerequisites = [[1,4],[2,4],[3,1],[3,2]]
        print(self.canFinish(numCourses, prerequisites))

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {src: [] for src in range(numCourses)}
        for prereq in prerequisites:
            dst, src = prereq
            graph[src].append(dst)
        
        visited = [False] * numCourses
        
        for i in range(numCourses):
            if not graph[i]:
                continue
            
            queue = deque()
            queue.append(i)

            while queue:
                popped = queue.popleft()
                visited[i] = True

                for dst in graph[popped]:
                    if visited[dst] == True:
                        return False
                    else:
                        queue.append(dst)

        return True

Solution()