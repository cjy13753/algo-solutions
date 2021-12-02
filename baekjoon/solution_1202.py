import sys
from collections import deque
import heapq
INF = sys.maxsize
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numJewels, numSacks = map(int, input().split())
        jewels = []
        for _ in range(numJewels):
            weight, value = map(int, input().split())
            jewels.append([weight, value]) # jewels[i] = [weight, value]

        sacks = []
        for _ in range(numSacks):
            sacks.append(int(input()))
        
        self.maxValue(jewels, sacks)

    def maxValue(self, jewels: list, sacks: list) -> None:
        jewels.sort()
        jewelsDequeue = deque(jewels)
        sacks.sort()

        tmpSackMaxHeap = []

        maxPrice = 0

        for sack in sacks:
            while jewelsDequeue and jewelsDequeue[0][0] <= sack:
                _, value = jewelsDequeue.popleft()
                heapq.heappush(tmpSackMaxHeap, -value)
            
            if tmpSackMaxHeap:
                maxPrice += heapq.heappop(tmpSackMaxHeap)

        print(-maxPrice)

Solution()