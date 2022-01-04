'''
Summary - Attempt #2

Runtime: 957 ms, faster than 10.38% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.4 MB, less than 25.06% of Python3 online submissions for Network Delay Time.

Basic approach: dijkstra with priority queue
'''


import sys
from typing import List
from collections import defaultdict
import heapq
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2

        print(self.networkDelayTime(times, n, k))

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 1e10
        adj_list = defaultdict(list) # adj_list = {src: [(dst, cost), ...]}
        for src, dst, cost in times:
            adj_list[src].append((dst, cost))
        distance = {} # {dst: shorted distance up to dst}
        visited = {}
        for i in range(1, n + 1):
            distance[i] = INF
            visited[i] = False

        minheap = []
        distance[k] = 0
        heapq.heappush(minheap, (0, k))

        while minheap:
            cost, src = heapq.heappop(minheap)

            if visited[src] == True:
                continue

            visited[src] = True

            for dst, newCost in adj_list[src]:
                accumCost = cost + newCost
                if accumCost < distance[dst]:
                    distance[dst] = accumCost
                    heapq.heappush(minheap, (accumCost, dst))

        return max(distance.values()) if sum(visited.values()) == n else -1

Solution()