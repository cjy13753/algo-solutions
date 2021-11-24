import sys
from collections import deque
input = sys.stdin.readline

def calcPartsNum(graph: list, indegree: list, numParts: int) -> list:
    queue = deque()
    sumPerPart = {i: 0 for i in range(1, numParts + 1)}

    for i in range(1, numParts + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        src = queue.popleft()
        for dst, cost in graph[src]:
            indegree[dst] -= 1
            val = 1 if sumPerPart[src] == 0 else sumPerPart[src]
            sumPerPart[dst] += val * cost
            if indegree[dst] == 0:
                queue.append(dst)

    ans = []
    for i in range(1, numParts + 1):
        if len(graph[i]) == 0:
            ans.append((i, sumPerPart[i]))

    return sorted(ans)

if __name__ == '__main__':
    numParts = int(input())
    numPairs = int(input())

    indegree = [0] * (numParts + 1)
    graph = [[] for _ in range(numParts + 1)]

    for _ in range(numPairs):
        src, dst, cost = map(int, input().split())
        graph[src].append((dst, cost)) # graph = [(dst, cost)]
        indegree[dst] += 1

    for part, num in calcPartsNum(graph, indegree, numParts):
        print(part, num)
