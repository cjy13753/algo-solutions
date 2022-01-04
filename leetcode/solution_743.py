import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2

        print(self.networkDelayTime(times, n, k))

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        for time in times:
            src, dst, cost = time
            graph[src][dst] = cost

        maxTime = [float('inf')]
        visited = [0] * (n + 1)

        def dfs(src, accum):
            visited[src] = 1
            
            if sum(graph[src]) == 0:
                maxTime[0] = min(maxTime[0], accum)
                return

            for dst, cost in enumerate(graph[src]):
                if cost > 0:
                    if visited[dst] == 1:
                        maxTime[0] = min(maxTime[0], accum)
                    else:
                        dfs(dst, accum + cost)

        dfs(k,0)
        
        return maxTime[0] if sum(visited) == n else -1


Solution()