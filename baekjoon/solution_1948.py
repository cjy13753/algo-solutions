import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def solution(indegree: dict, graph: defaultdict, graphBackward: defaultdict, start: int, end: int) -> None:
    # forward
    res = [0] * (numCities + 1)
    
    queue = deque()
    queue.append(start)
    while queue:
        src = queue.popleft()
        for dst, hour in graph[src]:
            indegree[dst] -= 1
            res[dst] = max(res[dst], res[src] + hour)
            if indegree[dst] == 0:
                queue.append(dst)
    
    # backward
    visited = [False] * (numCities + 1)
    queue.append(end)
    count = 0
    while queue:
        dst = queue.popleft()
        for src, hour in graphBackward[dst]:
            if res[dst] - res[src] == hour:
                count += 1
                if visited[src] == False:
                    visited[src] = True
                    queue.append(src)
    
    print(res[end])
    print(count)


if __name__ == '__main__':
    numCities = int(input())
    numRoads = int(input())

    indegree = {i: 0 for i in range(1, numCities + 1)}
    
    graph = defaultdict(list)
    graphBackward = defaultdict(list)
    for _ in range(numRoads):
        src, dst, hour = map(int, input().split())
        graph[src].append((dst, hour)) # graph: [dst, hour]
        indegree[dst] += 1

        graphBackward[dst].append((src, hour))

    start, end = map(int, input().split())

    solution(indegree, graph, graphBackward, start, end)