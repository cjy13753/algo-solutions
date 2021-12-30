'''
Summary

Attempt #1
Your own anwer?: No, https://www.youtube.com/watch?v=ZyB_gQ8vqGA
Time Complexity: O(E^2)
Runtime: 123 ms, faster than 15.67% of Python3 online submissions for Reconstruct Itinerary.
Space Complexity: O(E)
Memory Usage: 15.4 MB, less than 6.64% of Python3 online submissions for Reconstruct Itinerary.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        print(self.findItinerary(tickets))

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = {src: [] for src, _ in tickets}
        for src, dst in tickets:
            graph[src].append(dst)

        ans = ["JFK"]

        def dfs(src: str) -> bool:
            if len(ans) == len(tickets) + 1:
                return True
            if src not in graph:
                return False
            
            temp = list(graph[src])
            for idx, dst in enumerate(temp):
                graph[src].pop(idx)
                ans.append(dst)
                if dfs(dst):
                    return True
                graph[src].insert(idx, dst)
                ans.pop()

        dfs("JFK")
        return ans
        
Solution()