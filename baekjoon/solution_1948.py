import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(graph: defaultdict, indegree: dict, numCities: int, start: int, end: int):
    itinerary = {i: [] for i in range(numCities + 1)} # dst: [[total hours, path]]
    itinerary[start].append([0, [start]])

    queue = deque()
    for i in range(1, numCities + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()

        for dst, hour in graph[now]:
            for totalHours, path in itinerary[now]:
                totalHours += hour
                newPath = []
                for i in path:
                    newPath.append(i)
                newPath.append(dst)
                itinerary[dst].append([totalHours, newPath])
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)

    maxHours = int(-1e10)
    possibleRoutes = set()
    for candidate in itinerary[end]:
        maxHours = max(maxHours, candidate[0])
    for candidate in itinerary[end]:
        if candidate[0] == maxHours:
            for i in candidate[1]:
                possibleRoutes.add(i)
    
    print(maxHours)
    print(len(possibleRoutes))


if __name__ == '__main__':
    numCities = int(input())
    numRoads = int(input())

    indegree = {i: 0 for i in range(1, numCities + 1)}
    
    graph = defaultdict(list)
    for _ in range(numRoads):
        src, dst, hour = map(int, input().split())
        graph[src].append((dst, hour)) # graph: [dst, hour]
        indegree[dst] += 1

    start, end = map(int, input().split())

    solution(graph, indegree, numCities, start, end)