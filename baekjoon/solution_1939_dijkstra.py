import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


# 다익스트라 최단 거리 알고리즘을 살짝 변형하여 최대 중량을 구할 수 있도록 한다.
# 다리가 버티는 중량을 minHeap 대신에 maxHeap에 저장하도록 하며, 
# 중량은 누적이 아니라 전 섬까지의 누적 중량과 다음 섬으로 가는 다리의 중량 중 최소값으로 다음 섬에 할당하도록 한다.

if __name__ == '__main__':
    numIslands, numBridges = map(int, input().split())
    weightTable = [-1e10] * (numIslands + 1) # 양수값
    graph = defaultdict(list)
    visitedRoutes = set()
    maxHeap = []
    for _ in range(numBridges):
        src, dst, weight = list(map(int, input().split()))
        graph[src].append([-weight, dst]) # src: [-weight, dst]
        graph[dst].append([-weight, src])
    
    start, end = map(int, input().split())
    weightTable[start] = 1e10
    for negWeight, dst in graph[start]:
        heapq.heappush(maxHeap, (negWeight, start, dst))
        heapq.heappush(maxHeap, (negWeight, dst, start))

    while maxHeap:
        nowNegWeight, src, dst = heapq.heappop(maxHeap)
        
        if (nowNegWeight, src, dst) not in visitedRoutes:
            visitedRoutes.add((nowNegWeight, src, dst))
            if -nowNegWeight > weightTable[dst]: # 더 클 때만 갱신
                weightTable[dst] = min(-nowNegWeight, weightTable[src])
                for nextNegWeight, nextDst in graph[dst]:
                    heapq.heappush(maxHeap, (nextNegWeight, dst, nextDst))
                    heapq.heappush(maxHeap, (nextNegWeight, nextDst, dst))
    
    print(weightTable[end])