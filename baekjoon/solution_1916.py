import sys
import copy
from collections import defaultdict, deque
input = sys.stdin.readline


if __name__ == '__main__':
    numCities = int(input())
    numBuses = int(input())
    graph = defaultdict(list)
    for _ in range(numBuses):
        start, arrive, nxtCost = map(int, input().split())
        graph[start].append((arrive, nxtCost)) # graph = [start: (arrive, cost)]
    start, finalDst = map(int, input().split())
    visited = [False] * (numCities + 1)

    # BFS를 쓰는데, 각 경로가 다른 경로와 visited 정보를 공유하지 않고 독자적으로 관리함.
    queue = deque()
    visited[start] = True
    queue.append([start, visited, 0]) # queue: [destination, accumulated visited, accumulated cost]

    minCost = float('inf')
    while queue:
        dst, visited, total = queue.pop()
        if dst == finalDst:
            minCost = min(minCost, total)
            continue
        for nxtDst, nxtCost in graph[dst]:
            if nxtDst not in visited:
                newVisited = copy.deepcopy(visited)
                newVisited[nxtDst] = True
                queue.append([nxtDst, newVisited, total + nxtCost])

    print(minCost)