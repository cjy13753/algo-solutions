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
    if parent[vertex] != vertex:
        parent[vertex] = findParent(parent, parent[vertex])
    return parent[vertex]

if __name__ == '__main__':
    numVertices, numEdges = map(int, sys.stdin.readline().split())
    parent = [i for i in range(numVertices + 1)]
    
    for _ in range(numEdges):
        src, dst = map(int, sys.stdin.readline().split())
        unionFind(parent, src, dst)
    
    for i in range(1, numVertices + 1):
        findParent(parent, i)

    print(len(Counter(parent)) - 1)
    print(parent)