""" 
Attempt #4

Runtime: 673 ms, faster than 48.28% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.5 MB, less than 47.12% of Python3 online submissions for Network Delay Time.
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
        for source, target, weight in times:
            adjList[source].append((target, weight))
        heapq.heappush(minheap, (0, k))
        
        while minheap:
            minDistance, now = heapq.heappop(minheap)
            if distances[now] < minDistance:
                continue
            for adjNode, weight in adjList[now]:
                if weight + distances[now] < distances[adjNode]:
                    distances[adjNode] = weight + distances[now]
                    heapq.heappush(minheap, (distances[adjNode], adjNode))
        
        maxDist = max(distances)
        return -1 if maxDist == INF else maxDist