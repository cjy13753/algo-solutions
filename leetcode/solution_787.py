'''
Summary - attempt #2

Your own answer?: No
Basic approach: BFS(dijkstra ends up with time limit exceeded)
Reference: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686774/SUGGESTION-FOR-BEGINNERS-BFS-or-DIJKSHTRA-or-DP
Runtime: 148 ms, faster than 51.94% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 15.3 MB, less than 71.37% of Python3 online submissions for Cheapest Flights Within K Stops.
'''

import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1

        print(self.findCheapestPrice(n, flights, src, dst, k))

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e10)
        distance = [INF] * n
        graph = [[] for _ in range(n)]
        for start, end, p in flights:
            graph[start].append((end, p))
        
        queue = deque()
        queue.append((src, 0, -1)) # (pos, accum, stop_cnt)

        while queue:
            pos, accum, stop_cnt = queue.popleft()

            if pos == dst:
                continue
            
            if stop_cnt == k:
                continue
            
            for nxt, newDistance in graph[pos]:
                newAccum = accum + newDistance
                if newAccum < distance[nxt]:
                    distance[nxt] = newAccum
                    queue.append((nxt, newAccum, stop_cnt + 1))

        return -1 if distance[dst] == INF else distance[dst]

Solution()