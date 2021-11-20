import sys

n, m = map(int, sys.stdin.readline().split())
edges = {}
vertices = set()
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    vertices.add(u)
    vertices.add(v)
    if u not in edges.keys():
        edges[u] = []
    if v not in edges.keys():
        edges[v] = []
    edges[u].append(v)
    edges[v].append(u)

 
count = 0
visited = set()
for vertex in vertices:
    if vertex not in visited:
        count += 1

        stack = []
        stack.append(vertex)

        while len(stack) != 0:
            popped = stack.pop()
            if popped not in visited:
                visited.add(popped)
                for v in edges[popped]:
                    stack.append(v)

print(count + n - len(vertices))