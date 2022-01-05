import sys
from typing import List
import heapq
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
        price = [INF] * n
        visited = [False] * n
        graph = [[] for _ in range(n)]
        for start, end, p in flights:
            graph[start].append((end, p))
        
        minheap = [(0, src, 0)] # (price, src, stop_cnt)
        price[src] = 0

        while minheap:
            p, start, stop_cnt = heapq.heappop(minheap)

            if visited[start] == True:
                continue
            
            visited[start] = True
        
            if stop_cnt > k:
                continue

            for end, newP in graph[start]:
                accumP = p + newP
                if accumP < price[end]:
                    price[end] = accumP
                    heapq.heappush(minheap, (accumP, end, stop_cnt +1))

        return -1 if price[dst] == INF else price[dst]

Solution()