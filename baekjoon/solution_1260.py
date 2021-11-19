import sys
from collections import deque

def dfs(edges: dict, v: int) -> None:
    if v not in edges:
        print(v, end='') # 완전 관련 없는 시작점 주어질 경우 대비
        return
    stack = []
    visited = set()

    stack.append(v)
    while len(stack) != 0:
        popped = stack.pop()
        if popped not in visited:
            visited.add(popped)
            print(popped, end=' ')
            for vertex in edges[popped]:
                stack.append(vertex)

def bfs(edges: dict, v: int) -> None:
    if v not in edges:
        print(v, end='')
        return
    queue = deque()
    visited = set()

    queue.append(v)
    while len(queue) != 0:
        popped = queue.popleft()
        if popped not in visited:
            visited.add(popped)
            print(popped, end=' ')
            for vertex in edges[popped]:
                queue.append(vertex)
    
n, m, v = map(int, sys.stdin.readline().split())
edges = {}
for _ in range(m):
    src, dst = map(int, sys.stdin.readline().split())
    if src not in edges.keys():
        edges[src] = []
    if dst not in edges.keys():
        edges[dst] = []
    edges[src].append(dst)
    edges[dst].append(src)

for src in edges.keys():
    edges[src].sort(reverse=True)
dfs(edges, v)
print()

for src in edges.keys():
    edges[src].sort()
bfs(edges, v)