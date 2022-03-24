"""
Attempt #1
Time spent: 1h45m
My own answer: yes

Time Complexity:
O(NlogN), where N is the number of buildings
Sorting takes O(NlogN)
Every event heappushed and heappopped at most once each, which amounts to O(NlogN)

Space Complexity:
O(N)

Runtime: 128 ms, faster than 86.03% of Python3 online submissions for The Skyline Problem.
Memory Usage: 20.8 MB, less than 11.32% of Python3 online submissions for The Skyline Problem.
"""


from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        events = [] # event = (start, end, height)
        for start, end, height in buildings:
            events.append((start, end, height))
            events.append((end, end, height))
        events.sort(key = lambda x: (x[0], -x[1], -x[2]))

        prevMaxHeight = 0
        maxHeap = [(0, events[-1][1])] # (negative height, end)

        for start, end, height in events:
            if start < end:
                heapq.heappush(maxHeap, (-height, end))
            while len(maxHeap) > 1 and maxHeap[0][1] <= start:
                heapq.heappop(maxHeap)
            currentMaxHeight = abs(maxHeap[0][0])
            if currentMaxHeight != prevMaxHeight:
                if len(ans) != 0 and ans[-1][0] == start:
                    ans.pop()
                ans.append([start, currentMaxHeight])
                prevMaxHeight = currentMaxHeight

        return ans

print(Solution().getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]))