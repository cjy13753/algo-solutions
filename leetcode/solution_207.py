'''
Summary

Attempt #2
Your own answer?: No
Reference: https://leetcode.com/problems/course-schedule/discuss/58509/C%2B%2B-BFSDFS
Basic approach: Topological sort

Time Complexity: O(V + E) because you loop through all vertices to find ones with 0 indegree 
    and then remove edges extending from 0 indgree node.
Runtime: 96 ms, faster than 78.18% of Python3 online submissions for Course Schedule.
Space Complexity: O(V) where V is the number of courses
Memory Usage: 15.5 MB, less than 85.37% of Python3 online submissions for Course Schedule.
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
        degree = [0] * numCourses
        for prereq in prerequisites:
            dst, src = prereq
            graph[src].append(dst)
            degree[dst] += 1

        queue = deque([course for course in range(numCourses) if degree[course] == 0])

        while queue:
            src = queue.popleft()

            for dst in graph[src]:
                degree[dst] -= 1
                if degree[dst] == 0:
                    queue.append(dst) 

        return sum(degree) == 0
        
Solution()