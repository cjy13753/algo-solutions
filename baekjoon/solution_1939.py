import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


# 다익스트라 최단 거리 알고리즘을 살짝 변형하여 최대 중량을 구할 수 있도록 한다.
# 다리가 버티는 중량을 minHeap 대신에 maxHeap에 저장하도록 하며, 
# 중량은 누적이 아니라 전 섬까지의 누적 중량과 다음 섬으로 가는 다리의 중량 중 최소값으로 다음 섬에 할당하도록 한다.

if __name__ == '__main__':
    numIslands, numBridges = map(int, input().split())
    weightTable = [-1e10] * (numIslands + 1)
    graph = defaultdict(list)
    visited = [False] * (numIslands + 1)
    maxHeap = []
    for _ in range(numBridges):
        src, dst, weight = list(map(int, input().split()))
        graph[src].append([-weight, dst])
        graph[dst].append([-weight, src])
    
    start, end = map(int, input().split())
    weightTable[start] = 1e10
    heapq.heappush(maxHeap, (-1e10, start))

    while maxHeap:
        negWeight, src = heapq.heappop(maxHeap)
        visited[src] = True
        
        for newNegWeight, dst in graph[src]:
            if visited[dst] == False:
                if abs(negWeight) > weightTable[dst]:
                    weightTable[dst] = min(abs(newNegWeight), abs(negWeight))
                heapq.heappush(maxHeap, [newNegWeight, dst])
    
    print(weightTable[end])