import sys

def unionParent(parent: list, weight: int, v1: int, v2: int) -> int:
    v1 = findParent(parent, v1)
    v2 = findParent(parent, v2)

    if v1 == v2:
        return 0
    else:
        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1
        return weight

def findParent(parent: list, v: int) -> int:
    if parent[v] != v:
        parent[v] = findParent(parent, parent[v])
    return parent[v]

if __name__ == '__main__':
    numVertices, numEdges = map(int, sys.stdin.readline().split())
    graph = []
    parent = [i for i in range(numVertices + 1)]
    for _ in range(numEdges):
        v1, v2, weight= map(int, sys.stdin.readline().split())
        graph.append([weight, v1, v2])
    graph.sort()

    sumWeight = 0
    for weight, v1, v2 in graph:
        sumWeight += unionParent(parent, weight, v1, v2)

    print(sumWeight)
