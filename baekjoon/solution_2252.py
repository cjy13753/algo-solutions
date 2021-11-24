import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    numPeople, numCompare = map(int, input().split())
    graph = [[] for _ in range(numPeople + 1)]
    indegree = [0] * (numPeople + 1)
    for _ in range(numCompare):
        big, small = map(int, input().split())
        graph[big].append(small)
        indegree[small] += 1
    
    queue = deque()
    for i in range(1, numPeople + 1):
        if indegree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        now = queue.popleft()
        ans.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in ans:
        print(i, end=' ')