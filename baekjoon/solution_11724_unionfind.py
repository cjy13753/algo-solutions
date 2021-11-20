import sys
from collections import Counter

def unionFind(parent: list, src: int, dst: int) -> None:
    srcParent = findParent(parent, src)
    dstParent = findParent(parent, dst)

    if srcParent != dstParent:
        if srcParent < dstParent:
            parent[dst] = srcParent
        else:
            parent[src] = dstParent

def findParent(parent: list, vertex: int) -> int:
    if parent[vertex] == vertex:
        return vertex
    
    return findParent(parent, parent[vertex])

if __name__ == '__main__':
    numVertices, numEdges = map(int, sys.stdin.readline().split())
    parent = [i for i in range(numVertices + 1)]
    
    graph = []
    for _ in range(numEdges):
        src, dst = map(int, sys.stdin.readline().split())
        if src > dst:
            src, dst = dst, src
        graph.append([src, dst])
    graph.sort()
    for src, dst in graph:
        unionFind(parent, src, dst)

    print(len(Counter(parent)) - 1)
