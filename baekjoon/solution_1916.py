import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline


if __name__ == '__main__':
    INF = float('inf')
    
    numCities = int(input())
    numBuses = int(input())
    connectedCities = defaultdict(list)
    for _ in range(numBuses):
        depart, arrive, cost = map(int, input().split())
        connectedCities[depart].append((arrive, cost)) # graph = [depart: (arrive, cost)]
    start, end = map(int, input().split())
    visited = [False] * (numCities + 1)
    costTable = [INF] * (numCities + 1)
    minHeap = []

    # 시작도시 초기화
    costTable[start] = 0
    heapq.heappush(minHeap, (0, start)) # minHeap: [(accumCost, now)]

    while minHeap:
        accumCost, now = heapq.heappop(minHeap)
        if visited[now] == True:
            if now == end:
                break
            continue
        visited[now] = True

        for arrive, cost in connectedCities[now]:
            newAccumCost = accumCost + cost
            if newAccumCost < costTable[arrive]:
                costTable[arrive] = newAccumCost
                heapq.heappush(minHeap, (newAccumCost, arrive))

    # 출발점에서 도착점으로 무조건 도착할 수 있는 경우만 입력으로 주어지기 때문에 별도의 필터링 없이 출력
    print(costTable[end])