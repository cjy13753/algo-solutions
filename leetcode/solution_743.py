'''
Summary - Attempt #3

Your own answer?: No
Reference: https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions

Runtime: 492 ms, faster than 43.93% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.3 MB, less than 25.06% of Python3 online submissions for Network Delay Time.

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
        adj_list = defaultdict(list)
        for src, dst, cost in times:
            adj_list[src].append((dst, cost))
        distance = {}
        minheap = [(0, k)]

        while minheap:
            cost, src = heapq.heappop(minheap)

            if src not in distance:
                distance[src] = cost
                for dst, newCost in adj_list[src]:
                    heapq.heappush(minheap, (cost + newCost, dst))
        
        return max(distance.values()) if len(distance) == n else -1

Solution()