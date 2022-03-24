""" 
Attempt #5

Runtime: 583 ms, faster than 63.74% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.6 MB, less than 33.34% of Python3 online submissions for Network Delay Time.
"""

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 1_000_000_000
        distances = [INF] * (n + 1)
        distances[0] = 0
        distances[k] = 0
        minheap = []
        adjList = [[] for _ in range(n + 1)]
        visited = set()
        for source, target, weight in times:
            adjList[source].append((target, weight))
        heapq.heappush(minheap, (0, k))
        
        while minheap:
            _, now = heapq.heappop(minheap)
            visited.add(now)
            for adjNode, weight in adjList[now]:
                if not adjNode in visited and weight + distances[now] < distances[adjNode]:
                    distances[adjNode] = weight + distances[now]
                    heapq.heappush(minheap, (distances[adjNode], adjNode))
        
        maxDist = max(distances)
        return -1 if maxDist == INF else maxDist